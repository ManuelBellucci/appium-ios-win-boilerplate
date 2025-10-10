# tools/start.ps1 - Universal Version (PowerShell 5.x Compatible)
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Load-Dotenv($path) {
  $out = @{}
  if (Test-Path $path) {
    Get-Content $path | ForEach-Object {
      if ($_ -match '^\s*#' -or $_.Trim() -eq '' -or $_ -notmatch '=') { return }
      $k,$v = $_ -split '=', 2
      $out[$k.Trim()] = $v.Trim().Trim("'`"")
    }
  }
  return $out
}

function Find-PythonPath {
  $pythonPaths = @()
  
  try { $cmd = Get-Command python -ErrorAction Stop; $pythonPaths += $cmd.Source } catch { }
  try { $cmd = Get-Command python3 -ErrorAction Stop; $pythonPaths += $cmd.Source } catch { }
  
  $pythonPaths += "$env:USERPROFILE\AppData\Local\Programs\Python\Python*\python.exe"
  $pythonPaths += "C:\Python*\python.exe"
  $pythonPaths += "C:\Program Files\Python*\python.exe"
  $pythonPaths += "C:\Program Files (x86)\Python*\python.exe"
  $pythonPaths += "$env:USERPROFILE\AppData\Local\Microsoft\WindowsApps\python.exe"
  
  foreach ($path in $pythonPaths) {
    if (-not $path) { continue }
    
    if ($path -like "*\**") {
      try {
        $found = Get-ChildItem $path -ErrorAction SilentlyContinue | Sort-Object Name -Descending | Select-Object -First 1
        if ($found -and (Test-Path $found.FullName)) {
          return $found.FullName
        }
      } catch { }
    } elseif (Test-Path $path) {
      return $path
    }
  }
  
  throw "Python non trovato. Installa Python 3.x e aggiungilo al PATH o verifica l'installazione."
}

function Get-PortFromUrl($url, $def=8200) {
  if ($url -match ':(\d+)(/|$)') { return [int]$Matches[1] } else { return $def }
}

function Wait-HttpOk($url, $tries=120) {
  for ($i=0; $i -lt $tries; $i++) {
    try { $r = Invoke-RestMethod -Uri $url -TimeoutSec 2; if ($r) { return $true } }
    catch { Start-Sleep -Milliseconds 800 }
  }
  return $false
}

# Percorsi base - Universal
$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..")
$envFile  = Join-Path $repoRoot "e2eios\config\.env"
$cfg      = Load-Dotenv $envFile

# go-ios e config
$GoIos = $cfg["GO_IOS_EXE"]; if (-not $GoIos) { $GoIos = "C:\tools\go-ios\ios.exe" }
$Udid  = $cfg["IOS_UDID"]
$WdaUrl = $cfg["WDA_URL"]; if (-not $WdaUrl) { $WdaUrl = "http://127.0.0.1:8200" }
$ForwardPort = Get-PortFromUrl $WdaUrl 8200
$Bundle = "com.yourwdaname.WebDriverAgentRunner"
$XcTest = "WebDriverAgentRunner.xctest"

if (-not $Udid) { throw "Manca IOS_UDID in $envFile" }
if (-not (Test-Path $GoIos)) { throw "Non trovo go-ios in $GoIos" }

# Log
$logs   = Join-Path $repoRoot "logs"
New-Item $logs -ItemType Directory -Force | Out-Null
$ts = Get-Date -Format "yyyyMMdd-HHmmss"
$imgOut = Join-Path $logs "image-$ts.out.log"
$imgErr = Join-Path $logs "image-$ts.err.log"
$wdaOut = Join-Path $logs "wda-$ts.out.log"
$wdaErr = Join-Path $logs "wda-$ts.err.log"
$fwOut  = Join-Path $logs "forward-$ts.out.log"
$fwErr  = Join-Path $logs "forward-$ts.err.log"

# === Developer Disk Image ===
Write-Host "== Montaggio Developer Disk Image ==" -ForegroundColor Cyan
$imgArgs = @("image","auto")
$imgProc = Start-Process -FilePath $GoIos -ArgumentList $imgArgs `
  -WindowStyle Hidden -PassThru -Wait `
  -RedirectStandardOutput $imgOut -RedirectStandardError $imgErr

Write-Host "   (log: $imgOut / $imgErr, uscita: $($imgProc.ExitCode))"
if ($imgProc.ExitCode -ne 0) {
  Write-Warning "image auto è uscito con codice $($imgProc.ExitCode) (è normale se era già montato)."
}

# Forward
Write-Host "== 1) Avvio FORWARD $ForwardPort -> 8100 ==" -ForegroundColor Cyan
$fwArgs = @("forward", $ForwardPort, "8100", "--udid", $Udid)
$fwProc = Start-Process -FilePath $GoIos -ArgumentList $fwArgs `
  -WindowStyle Minimized -PassThru `
  -RedirectStandardOutput $fwOut -RedirectStandardError $fwErr
Write-Host "   PID forward: $($fwProc.Id)  (log: $fwOut / $fwErr)"

# WDA
Write-Host "== 2) Avvio WDA in background ==" -ForegroundColor Cyan
$runArgs = @("runwda","--udid",$Udid,"--bundleid",$Bundle,"--testrunnerbundleid",$Bundle,"--xctestconfig",$XcTest,"--log-output","-")
$wdaProc = Start-Process -FilePath $GoIos -ArgumentList $runArgs `
  -WindowStyle Minimized -PassThru `
  -RedirectStandardOutput $wdaOut -RedirectStandardError $wdaErr
Write-Host "   PID WDA: $($wdaProc.Id)  (log: $wdaOut / $wdaErr)"

Write-Host "Attendo $WdaUrl/status ..." -ForegroundColor Yellow
if (-not (Wait-HttpOk "$WdaUrl/status")) {
  Write-Warning "WDA non risponde. Controlla i log."
} else {
  Write-Host "WDA OK." -ForegroundColor Green
}

# --- Python Dependencies (Universal) ---
Write-Host "== Ricerca Python ==" -ForegroundColor Cyan
try {
  $py = Find-PythonPath
  Write-Host "   Python trovato: $py" -ForegroundColor Green
} catch {
  Write-Host "   $_" -ForegroundColor Red
  throw
}

Write-Host "== Installazione dipendenze ==" -ForegroundColor Cyan
& $py -m pip install -r (Join-Path $repoRoot "requirements.txt")

# Import locali
$env:PYTHONPATH = "$repoRoot"

Write-Host "== 3) Smoke test: apri Impostazioni/Generali ==" -ForegroundColor Cyan
& $py (Join-Path $repoRoot "e2eios\scripts\open_settings.py")
$code = $LASTEXITCODE
if ($code -ne 0) { Write-Warning "Lo script ha restituito codice $code" }
else { Write-Host "Smoke OK" -ForegroundColor Green }
