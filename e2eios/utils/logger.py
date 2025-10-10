#!/usr/bin/env python3
"""
Centralized Logging Utility for Appium iOS Automation
Provides consistent logging with timestamps, levels, and error context
"""

import sys
import traceback
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any
import json

class AppiumLogger:
    """Centralized logger for all automation scripts"""
    
    LEVELS = {
        'DEBUG': '🔍',
        'INFO': 'ℹ️',
        'SUCCESS': '✅',
        'WARNING': '⚠️',
        'ERROR': '❌',
        'CRITICAL': '🚨'
    }
    
    COLORS = {
        'DEBUG': '\033[36m',     # Cyan
        'INFO': '\033[37m',      # White
        'SUCCESS': '\033[32m',   # Green
        'WARNING': '\033[33m',   # Yellow
        'ERROR': '\033[31m',     # Red
        'CRITICAL': '\033[35m',  # Magenta
        'RESET': '\033[0m'       # Reset
    }
    
    def __init__(self, component: str = "Unknown", enable_debug: bool = False):
        self.component = component
        self.enable_debug = enable_debug
        self.session_id = datetime.now().strftime("%Y%m%d-%H%M%S")
        
    def _format_message(self, level: str, message: str, context: Optional[Dict[str, Any]] = None) -> str:
        """Format log message with timestamp and level"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        icon = self.LEVELS.get(level, '📋')
        
        # Base message
        formatted = f"[{timestamp}] [{level}] {self.component}: {message}"
        
        # Add context if provided
        if context:
            context_str = ", ".join([f"{k}={v}" for k, v in context.items()])
            formatted += f" | {context_str}"
            
        return f"{icon} {formatted}"
    
    def _safe_print(self, message: str):
        """Safely print message handling Unicode encoding issues"""
        try:
            print(message)
        except UnicodeEncodeError:
            # Fallback for Windows terminals that don't support UTF-8
            safe_message = message.encode('ascii', 'replace').decode('ascii')
            print(safe_message)
    
    def debug(self, message: str, context: Optional[Dict[str, Any]] = None):
        """Log debug message (only if debug enabled)"""
        if self.enable_debug:
            self._safe_print(self._format_message('DEBUG', message, context))
    
    def info(self, message: str, context: Optional[Dict[str, Any]] = None):
        """Log info message"""
        self._safe_print(self._format_message('INFO', message, context))
    
    def success(self, message: str, context: Optional[Dict[str, Any]] = None):
        """Log success message"""
        self._safe_print(self._format_message('SUCCESS', message, context))
    
    def warning(self, message: str, context: Optional[Dict[str, Any]] = None):
        """Log warning message"""
        self._safe_print(self._format_message('WARNING', message, context))
    
    def error(self, message: str, context: Optional[Dict[str, Any]] = None, exc_info: bool = False):
        """Log error message with optional exception info"""
        self._safe_print(self._format_message('ERROR', message, context))
        
        if exc_info:
            tb = traceback.format_exc()
            if tb != "NoneType: None\n":
                try:
                    print(f"🔍 Exception details: {tb}")
                except UnicodeEncodeError:
                    print(f"[!] Exception details: {tb}")
    
    def critical(self, message: str, context: Optional[Dict[str, Any]] = None, exc_info: bool = True):
        """Log critical error with exception info"""
        print(self._format_message('CRITICAL', message, context))
        
        if exc_info:
            tb = traceback.format_exc()
            if tb != "NoneType: None\n":
                print(f"🚨 Critical exception: {tb}")
    
    def log_element_search(self, selector_type: str, selector_value: str, found: bool, attempts: int = 1):
        """Log element search results with debug info"""
        context = {
            'selector': f"{selector_type}='{selector_value}'",
            'attempts': attempts
        }
        
        if found:
            self.debug(f"Element found", context)
        else:
            self.warning(f"Element not found", context)
    
    def log_action(self, action: str, target: str, success: bool, duration: Optional[float] = None):
        """Log user action with result"""
        context = {'target': target}
        if duration:
            context['duration'] = f"{duration:.2f}s"
            
        if success:
            self.success(f"Action '{action}' completed", context)
        else:
            self.error(f"Action '{action}' failed", context)
    
    def log_session_start(self, session_type: str, config: Dict[str, Any]):
        """Log session start with configuration"""
        self.info(f"Starting {session_type} session", {'session_id': self.session_id})
        for key, value in config.items():
            self.info(f"Config: {key} = {value}")
    
    def log_session_stats(self, stats: Dict[str, Any]):
        """Log session statistics"""
        self.info("Session Statistics:", stats)
    
    def log_screen_state(self, screen: str, elements_found: Optional[list] = None):
        """Log current screen state detection"""
        context = {'screen': screen}
        if elements_found:
            context['elements'] = len(elements_found)
        self.info("Screen state detected", context)
    
    def log_api_call(self, api: str, method: str, status_code: int, response_time: Optional[float] = None):
        """Log API calls and responses"""
        context = {
            'api': api,
            'method': method,
            'status': status_code
        }
        if response_time:
            context['response_time'] = f"{response_time:.3f}s"
            
        if 200 <= status_code < 300:
            self.success("API call successful", context)
        elif 400 <= status_code < 500:
            self.warning("API client error", context)
        else:
            self.error("API server error", context)

def get_logger(component: str, enable_debug: bool = False) -> AppiumLogger:
    """Factory function to create logger instances"""
    return AppiumLogger(component, enable_debug)

# Convenience functions for quick logging
def log_info(component: str, message: str, **context):
    """Quick info log"""
    logger = get_logger(component)
    logger.info(message, context if context else None)

def log_error(component: str, message: str, exc_info: bool = False, **context):
    """Quick error log"""
    logger = get_logger(component)
    logger.error(message, context if context else None, exc_info)

def log_success(component: str, message: str, **context):
    """Quick success log"""
    logger = get_logger(component)
    logger.success(message, context if context else None)