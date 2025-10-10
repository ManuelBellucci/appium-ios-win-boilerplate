from time import sleep
from pathlib import Path
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from e2eios.utils.env import load_env

ROOT = Path(__file__).resolve().parents[2]
ENV = load_env(ROOT / "e2eios" / "config" / ".env")

APPIUM_URL = ENV.get("APPIUM_URL", "http://127.0.0.1:4723")
WDA_URL    = ENV.get("WDA_URL", "http://127.0.0.1:8200")
UDID       = ENV["IOS_UDID"]
BUNDLE_ID  = ENV.get("BUNDLE_ID", "com.apple.Preferences")  

opts = AppiumOptions()
opts.set_capability("platformName", "iOS")
opts.set_capability("appium:automationName", "XCUITest")
opts.set_capability("appium:udid", UDID)
opts.set_capability("appium:webDriverAgentUrl", WDA_URL)  # WDA ya levantado
opts.set_capability("appium:bundleId", BUNDLE_ID)
opts.set_capability("appium:noReset", True)
opts.set_capability("appium:autoAcceptAlerts", True)
opts.set_capability("appium:newCommandTimeout", 120)

driver = webdriver.Remote(APPIUM_URL, options=opts)

sleep(1)
driver.activate_app(BUNDLE_ID)

try:
    el = driver.find_element(AppiumBy.IOS_PREDICATE, 'label == "Generali" OR label == "General"')
    el.click()
    print("Tap su Generali/General OK")
except Exception as e:
    print("Elemento 'Generali/General' non trovato subito:", e)

driver.quit()
