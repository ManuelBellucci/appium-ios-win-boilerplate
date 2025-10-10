# Intenta cerrar procesos go-ios iniciados por nosotros
Get-Process | Where-Object { $_.Name -eq "ios" -or $_.Path -like "*go-ios\ios.exe" } |
  ForEach-Object { try { Stop-Process -Id $_.Id -Force -ErrorAction SilentlyContinue } catch {} }

Write-Host "Processi go-ios fermati (se c'erano)."
