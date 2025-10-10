#!/usr/bin/env python3
"""
Test Connection Script
Validates Appium and WebDriverAgent connectivity
Enhanced with structured logging
"""

import sys
from pathlib import Path
import requests
import time

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from e2eios.utils.env import load_env
from e2eios.utils.logger import get_logger

def test_connection():
    """Test connection to Appium and WebDriverAgent with detailed logging"""
    logger = get_logger("ConnectionTest", enable_debug=True)
    
    # Load environment
    logger.info("Starting connection test")
    env = load_env(ROOT / "e2eios" / "config" / ".env")
    
    appium_url = env.get("APPIUM_URL", "http://127.0.0.1:4723")
    wda_url = env.get("WDA_URL", "http://127.0.0.1:8200")
    udid = env.get("IOS_UDID")
    
    logger.info("Configuration loaded", {
        'appium_url': appium_url,
        'wda_url': wda_url,
        'udid': udid[:8] + "..." if udid else "NOT_SET"
    })
    
    if not udid:
        logger.error("IOS_UDID not found in environment configuration")
        return False
    
    # Test Appium
    logger.info("Testing Appium server connection")
    try:
        start_time = time.time()
        response = requests.get(f"{appium_url}/status", timeout=5)
        response_time = time.time() - start_time
        
        logger.log_api_call("Appium", "GET", response.status_code, response_time)
        
        if response.status_code == 200:
            data = response.json()
            logger.success("Appium server is responsive", {
                'build': data.get('value', {}).get('build', {}).get('version', 'unknown')
            })
            appium_ok = True
        else:
            logger.error("Appium server returned error status", {
                'status_code': response.status_code,
                'response': response.text[:100]
            })
            appium_ok = False
            
    except requests.exceptions.ConnectionError:
        logger.error("Cannot connect to Appium server", {'url': appium_url})
        appium_ok = False
    except Exception as e:
        logger.error("Appium connection test failed", exc_info=True)
        appium_ok = False
    
    # Test WebDriverAgent
    logger.info("Testing WebDriverAgent connection")
    try:
        start_time = time.time()
        response = requests.get(f"{wda_url}/status", timeout=5)
        response_time = time.time() - start_time
        
        logger.log_api_call("WebDriverAgent", "GET", response.status_code, response_time)
        
        if response.status_code == 200:
            data = response.json()
            logger.success("WebDriverAgent is responsive", {
                'device': data.get('value', {}).get('device', 'unknown')
            })
            wda_ok = True
        else:
            logger.error("WebDriverAgent returned error status", {
                'status_code': response.status_code,
                'response': response.text[:100]
            })
            wda_ok = False
            
    except requests.exceptions.ConnectionError:
        logger.error("Cannot connect to WebDriverAgent", {'url': wda_url})
        wda_ok = False
    except Exception as e:
        logger.error("WebDriverAgent connection test failed", exc_info=True)
        wda_ok = False
    
    # Summary
    if appium_ok and wda_ok:
        logger.success("All connections successful - ready for automation!", {
            'appium': '✅',
            'wda': '✅'
        })
        return True
    else:
        logger.error("Connection test failed", {
            'appium': '✅' if appium_ok else '❌',
            'wda': '✅' if wda_ok else '❌'
        })
        return False

if __name__ == "__main__":
    success = test_connection()
    sys.exit(0 if success else 1)