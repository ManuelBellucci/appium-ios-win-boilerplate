#!/usr/bin/env python3
"""
Control Panel - Simple iOS Automation Manager
Simplified control panel for the boilerplate project
"""

import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import threading
import time
import requests
import socket
import json
from pathlib import Path
import sys
import os

# Add project root to path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from e2eios.utils.env import load_env

class ControlPanel:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("📱 iOS Automation Control Panel")
        self.root.geometry("700x500")
        self.root.configure(bg='#f5f5f5')
        
        # Load configuration
        self.env = load_env(ROOT / "e2eios" / "config" / ".env")
        self.appium_url = self.env.get("APPIUM_URL", "http://127.0.0.1:4723")
        self.wda_url = self.env.get("WDA_URL", "http://127.0.0.1:8200")
        self.udid = self.env.get("IOS_UDID", "")
        self.go_ios_path = self.env.get("GO_IOS_EXE", "C:\\tools\\go-ios\\ios.exe")
        
        # Status variables
        self.is_connected = False
        self.services_running = False
        
        # Setup UI
        self.setup_ui()
        
        # Start status monitoring
        self.start_status_monitor()
    
    def setup_ui(self):
        """Setup user interface"""
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = tk.Label(main_frame, text="📱 iOS Automation Control Panel", 
                              font=("Arial", 16, "bold"), bg='#f5f5f5', fg='#333')
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Device info section
        info_frame = ttk.LabelFrame(main_frame, text="Device Information", padding="10")
        info_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # UDID display
        tk.Label(info_frame, text="Device UDID:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W)
        self.udid_var = tk.StringVar()
        self.update_udid_display()
        tk.Label(info_frame, textvariable=self.udid_var, font=("Arial", 10)).grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # Status indicators
        status_frame = ttk.LabelFrame(main_frame, text="Service Status", padding="10")
        status_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Appium status
        tk.Label(status_frame, text="Appium Server:", font=("Arial", 10, "bold")).grid(row=0, column=0, sticky=tk.W)
        self.appium_status = tk.Label(status_frame, text="❌ Disconnected", fg="red")
        self.appium_status.grid(row=0, column=1, sticky=tk.W, padx=(10, 0))
        
        # WDA status
        tk.Label(status_frame, text="WebDriverAgent:", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky=tk.W)
        self.wda_status = tk.Label(status_frame, text="❌ Disconnected", fg="red")
        self.wda_status.grid(row=1, column=1, sticky=tk.W, padx=(10, 0))
        
        # Device connection status
        tk.Label(status_frame, text="Device Connection:", font=("Arial", 10, "bold")).grid(row=2, column=0, sticky=tk.W)
        self.device_status = tk.Label(status_frame, text="❌ Not Connected", fg="red")
        self.device_status.grid(row=2, column=1, sticky=tk.W, padx=(10, 0))
        
        # Control buttons
        control_frame = ttk.LabelFrame(main_frame, text="Device Control", padding="10")
        control_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Start services button
        self.start_btn = ttk.Button(control_frame, text="🚀 Start Services", 
                                   command=self.start_services, width=18)
        self.start_btn.grid(row=0, column=0, padx=(0, 5))
        
        # Stop services button
        self.stop_btn = ttk.Button(control_frame, text="🛑 Stop Services", 
                                  command=self.stop_services, width=18)
        self.stop_btn.grid(row=0, column=1, padx=(0, 5))
        
        # Test connection button
        self.test_btn = ttk.Button(control_frame, text="🔍 Test Connection", 
                                  command=self.test_connection, width=18)
        self.test_btn.grid(row=0, column=2, padx=(0, 5))
        
        # Refresh devices button
        self.refresh_btn = ttk.Button(control_frame, text="🔄 Refresh", 
                                     command=self.refresh_devices, width=15)
        self.refresh_btn.grid(row=0, column=3, padx=(0, 5))
        
        # Clear console button
        self.clear_btn = ttk.Button(control_frame, text="🧹 Clear Console", 
                                   command=self.clear_console, width=15)
        self.clear_btn.grid(row=0, column=4)
        
        # Console output
        console_frame = ttk.LabelFrame(main_frame, text="Console Output", padding="10")
        console_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Text widget with scrollbar - Dark mode styling
        text_frame = ttk.Frame(console_frame)
        text_frame.pack(fill=tk.BOTH, expand=True)
        
        self.console_text = tk.Text(text_frame, height=10, width=70, wrap=tk.WORD,
                                  bg='#2f3349',  # Dark slate background
                                  fg='#ffffff',  # White text
                                  insertbackground='#ffffff',  # White cursor
                                  selectbackground='#404040',  # Dark selection
                                  selectforeground='#ffffff',  # White selected text
                                  font=('Consolas', 10))  # Monospace font
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.console_text.yview)
        self.console_text.configure(yscrollcommand=scrollbar.set)
        
        # Configure color tags for different message types
        self.console_text.tag_config("info", foreground="#ffffff")      # White for info
        self.console_text.tag_config("success", foreground="#4ade80")   # Green for success
        self.console_text.tag_config("warning", foreground="#fbbf24")   # Yellow for warnings
        self.console_text.tag_config("error", foreground="#ef4444")     # Red for errors
        self.console_text.tag_config("timestamp", foreground="#9ca3af") # Gray for timestamps
        
        self.console_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Configure grid weights
        main_frame.rowconfigure(4, weight=1)
        main_frame.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        
        # Keyboard shortcuts
        self.root.bind('<Control-l>', lambda e: self.clear_console())  # Ctrl+L to clear
        self.root.bind('<F5>', lambda e: self.refresh_devices())       # F5 to refresh
        
        # Initial status check
        self.log_console("🚀 iOS Automation Control Panel initialized")
        self.log_console("💡 Tip: Use Ctrl+L to clear console, F5 to refresh devices")
        self.refresh_devices()
    
    def update_udid_display(self):
        """Update UDID display with current device info"""
        if self.udid:
            # Show current UDID from config
            self.udid_var.set(self.udid)
        else:
            # Try to detect devices
            devices = self.list_devices()
            if devices:
                detected_udid = devices[0] if devices[0] else "Unknown"
                self.udid_var.set(f"{detected_udid}")
            else:
                self.udid_var.set("Not configured")
    
    def clear_console(self):
        """Clear the console output"""
        self.console_text.delete(1.0, tk.END)
        self.log_console("Console cleared")
    
    def log_console(self, message, msg_type="info"):
        """Log message to console with color coding"""
        timestamp = time.strftime("%H:%M:%S")
        
        # Insert timestamp with gray color
        self.console_text.insert(tk.END, f"[{timestamp}] ", "timestamp")
        
        # Determine message type and color
        if "✅" in message or "successful" in message.lower() or "ok" in message.lower():
            msg_type = "success"
        elif "❌" in message or "error" in message.lower() or "failed" in message.lower():
            msg_type = "error"
        elif "⚠️" in message or "warning" in message.lower() or "timeout" in message.lower():
            msg_type = "warning"
        
        # Insert message with appropriate color
        self.console_text.insert(tk.END, f"{message}\n", msg_type)
        self.console_text.see(tk.END)  # Auto-scroll to bottom
        self.root.update_idletasks()
    
    def run_go_ios_command(self, args, timeout=30):
        """Run go-ios command and return result"""
        try:
            result = subprocess.run([self.go_ios_path] + args, 
                                  capture_output=True, text=True, timeout=timeout)
            return result.returncode == 0, result.stdout, result.stderr
        except Exception as e:
            return False, "", str(e)
    
    def list_devices(self):
        """List connected iOS devices"""
        success, stdout, stderr = self.run_go_ios_command(["list"])
        if success and stdout.strip():
            try:
                # Parse JSON response from go-ios list command
                # Extract JSON from stdout (may contain warning messages before JSON)
                lines = stdout.strip().split('\n')
                json_line = None
                for line in lines:
                    if line.strip().startswith('{"deviceList"'):
                        json_line = line.strip()
                        break
                
                if json_line:
                    data = json.loads(json_line)
                    return data.get("deviceList", [])
                else:
                    # Fallback to old parsing for compatibility
                    devices = [line.strip() for line in lines if line.strip() and not line.startswith('{"level":')]
                    return devices
            except json.JSONDecodeError:
                # Fallback to old parsing
                devices = [line.strip() for line in stdout.strip().split('\n') if line.strip()]
                return devices
        return []
    
    def check_service_status(self, url, service_name):
        """Check if a service is running"""
        try:
            response = requests.get(f"{url}/status", timeout=5)
            return response.status_code == 200
        except Exception:
            return False
    
    def check_port_open(self, port):
        """Check if a port is open"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
            result = sock.connect_ex(('127.0.0.1', int(port)))
            sock.close()
            return result == 0
        except Exception:
            return False
    
    def update_status_display(self):
        """Update status indicators"""
        # Check Appium
        appium_running = self.check_service_status(self.appium_url, "Appium")
        if appium_running:
            self.appium_status.config(text="✅ Connected", fg="green")
        else:
            self.appium_status.config(text="❌ Disconnected", fg="red")
        
        # Check WDA (just port check since it might not have /status endpoint)
        wda_port = self.wda_url.split(':')[-1]
        wda_running = self.check_port_open(wda_port)
        if wda_running:
            self.wda_status.config(text="✅ Running", fg="green")
        else:
            self.wda_status.config(text="❌ Not Running", fg="red")
        
        # Check device connection
        if self.udid:
            devices = self.list_devices()
            device_connected = any(self.udid in device for device in devices)
            if device_connected:
                self.device_status.config(text="✅ Connected", fg="green")
                self.is_connected = True
            else:
                self.device_status.config(text="❌ Not Connected", fg="red")
                self.is_connected = False
        else:
            self.device_status.config(text="⚠️ UDID Not Configured", fg="orange")
            self.is_connected = False
        
        # Update services status
        self.services_running = appium_running and wda_running
    
    def start_status_monitor(self):
        """Start periodic status monitoring"""
        def monitor():
            while True:
                try:
                    self.update_status_display()
                    time.sleep(5)  # Check every 5 seconds
                except Exception as e:
                    print(f"Status monitor error: {e}")
                    time.sleep(10)
        
        monitor_thread = threading.Thread(target=monitor, daemon=True)
        monitor_thread.start()
    
    def refresh_devices(self):
        """Refresh device list and update UDID display"""
        def refresh():
            self.log_console("Refreshing device list...")
            devices = self.list_devices()
            
            if devices:
                self.log_console(f"Found {len(devices)} device(s):")
                for device in devices:
                    self.log_console(f"  - {device}")
                
                # Update UDID display
                self.update_udid_display()
                
                # Update UDID if not configured
                if not self.udid and devices:
                    first_device = devices[0] if devices[0] else ""
                    if first_device:
                        self.udid = first_device
                        self.udid_var.set(first_device)
                        self.log_console(f"Auto-detected device UDID: {first_device}")
            else:
                self.log_console("No devices found. Make sure your iOS device is connected and trusted.")
                self.udid_var.set("No devices found")
        
        # Run in thread to avoid blocking UI
        threading.Thread(target=refresh, daemon=True).start()
    
    def start_services(self):
        """Start required services using PowerShell script"""
        def start():
            self.log_console("Starting services...")
            
            if not self.udid:
                self.log_console("❌ No device UDID configured!")
                return
            
            # Run the PowerShell start script
            start_script = ROOT / "tools" / "start.ps1"
            
            if not start_script.exists():
                self.log_console("❌ Start script not found!")
                return
            
            try:
                self.log_console("Running start.ps1 script...")
                result = subprocess.run([
                    "powershell.exe", "-ExecutionPolicy", "Bypass", 
                    "-File", str(start_script)
                ], capture_output=True, text=True, timeout=120)
                
                if result.returncode == 0:
                    self.log_console("✅ Services startup completed!")
                    self.log_console("You can now run your automation scripts.")
                else:
                    self.log_console("❌ Service startup failed!")
                    if result.stderr:
                        self.log_console(f"Error: {result.stderr[:200]}...")
                        
            except subprocess.TimeoutExpired:
                self.log_console("⚠️ Service startup timed out")
            except Exception as e:
                self.log_console(f"❌ Error starting services: {e}")
        
        # Run in thread
        threading.Thread(target=start, daemon=True).start()
    
    def stop_services(self):
        """Stop running services"""
        def stop():
            self.log_console("Stopping services...")
            
            try:
                # Stop any running go-ios processes
                subprocess.run(["taskkill", "/f", "/im", "ios.exe"], 
                              capture_output=True, text=True)
                self.log_console("✅ Stopped go-ios processes")
                
                # Note: Appium should be stopped manually if running
                self.log_console("ℹ️ Please stop Appium server manually if running")
                
            except Exception as e:
                self.log_console(f"⚠️ Error stopping services: {e}")
        
        # Run in thread
        threading.Thread(target=stop, daemon=True).start()
    
    def test_connection(self):
        """Test connection to device and services"""
        def test():
            self.log_console("Testing connections...")
            
            # Test device connection
            if self.is_connected:
                self.log_console("✅ Device connected")
                
                # Try to get device info
                success, stdout, stderr = self.run_go_ios_command(["info", "--udid", self.udid])
                if success:
                    self.log_console("✅ Device info retrieved successfully")
                else:
                    self.log_console("⚠️ Could not retrieve device info")
            else:
                self.log_console("❌ Device not connected")
            
            # Test Appium service
            try:
                response = requests.get(f"{self.appium_url}/status", timeout=5)
                if response.status_code == 200:
                    self.log_console("✅ Appium server responding")
                else:
                    self.log_console("❌ Appium server not responding")
            except Exception:
                self.log_console("❌ Cannot connect to Appium server")
            
            # Test WDA service
            try:
                response = requests.get(f"{self.wda_url}/status", timeout=5)
                if response.status_code == 200:
                    self.log_console("✅ WebDriverAgent responding")
                else:
                    self.log_console("❌ WebDriverAgent not responding")
            except Exception:
                self.log_console("❌ Cannot connect to WebDriverAgent")
            
            self.log_console("Connection test completed")
        
        # Run in thread
        threading.Thread(target=test, daemon=True).start()
    
    def run(self):
        """Start the control panel"""
        self.log_console("🎯 Control panel ready. Click 'Start Services' to begin automation.")
        
        try:
            self.root.mainloop()
        except KeyboardInterrupt:
            self.log_console("👋 Control panel closed by user")
        except Exception as e:
            self.log_console(f"💥 Error: {e}")


if __name__ == "__main__":
    try:
        panel = ControlPanel()
        panel.run()
    except Exception as e:
        print(f"Failed to start control panel: {e}")
        input("Press Enter to exit...")