# 📱 iOS Automation Boilerplate

WARNING: This v1 of the framework is a lite version for run small scale in Windows. Is limited to 5 devices, rely on some unstable tech and lacks of complex architecture. 
Is a good one to start and save you time to run small automation on windows with ios devices.
for business inquiries, i use for my customers a pro framework that is highly more advanced and scalable.

> A comprehensive Windows-based iOS automation framework using Appium, WebDriverAgent, and go-ios for seamless iOS app testing and automation. This is a FULLY CUSTOMIZABLE base boilerplate and guide to set-up Appium on Windows. Something may seem hard for someone made so easy. From this, get your UI testing to another level and save time, only updating the scripts and panel.

[![Platform](https://img.shields.io/badge/platform-iOS-blue.svg)](https://developer.apple.com/ios/)
[![Framework](https://img.shields.io/badge/framework-Appium-green.svg)](https://appium.io/)
[![Language](https://img.shields.io/badge/language-Python-yellow.svg)](https://python.org/)
[![OS](https://img.shields.io/badge/os-Windows-lightgrey.svg)](https://microsoft.com/windows/)

## 🚀 Features

- ✅ **Complete iOS Device Management** - Automated device setup and WebDriverAgent deployment
- 🎮 **Enhanced GUI Control Panel** - User-friendly interface with dark mode console and advanced controls
- 🔧 **PowerShell Automation** - Streamlined service management scripts
- 📊 **Real-time Monitoring** - Live status checking for all services with health indicators
- 🧪 **Connection Testing** - Built-in validation tools with detailed diagnostics
- 📝 **Comprehensive Logging** - Detailed logging with timestamps and color coding
- 🔄 **Advanced Auto-Recovery** - Intelligent service restart, device reconnection, and health monitoring
- ⌨️ **Configurable Shortcuts** - Customizable keyboard shortcuts for all panel actions
- 🎯 **Service-Specific Recovery** - Individual service health monitoring and targeted recovery
- 💾 **Log Export & Management** - Export console logs and manage automation history
- 🔧 **Script Integration** - Direct execution of automation scripts from panel

## 📋 Prerequisites

### 🍎 iOS Development Requirements

#### 1. **Apple Developer Account**
- 💳 **Active Apple Developer Program membership** ($99/year)
- 📱 **iOS device** with iOS 12+ according to your app specifications.
- 🔒 **Valid certificates and provisioning profiles**

#### 2. **Development Certificates**
You need the following files:
- 📄 **`.p12` certificate file** (iOS Developer Certificate)
- 📄 **`.mobileprovision` file** (Development Provisioning Profile)
- 🔐 **Certificate password**

#### 3. **Xcode Setup**
- 💻 **Xcode 12.0+** installed on macOS (for WDA compilation)
- 🛠️ **Command Line Tools** installed
- ✅ **WebDriverAgent successfully compiled and installed on device**

> **⚠️ Critical**: WebDriverAgent MUST be compiled in Xcode ON A MAC with your developer certificates and installed on your iPhone before using this automation framework. Your devices UDIDs MUST be registered in the Dev Account. Contact with your Apple Dev to do this process.

### 🖥️ Windows Development Environment

#### 1. **Required Software**
```bash
# Core Requirements
- Python 3.8+
- Node.js 16+
- Git
```

#### 2. **Appium Ecosystem**
- 🧙‍♂️ **Appium Wizard** - For server management (https://github.com/mega6453/AppiumWizard)
- 🔍 **Appium Inspector** - For element inspection and capability testing
- 📡 **Appium Server** running on port 4723

#### 3. **go-ios Tool**
- 📥 **go-ios binary** installed at `C:\tools\go-ios\ios.exe`
- 🔗 Download from: [go-ios releases](https://github.com/danielpaulus/go-ios/releases)

## 🛠️ Installation & Setup

### Step 1: Clone Repository
```bash
git clone https://github.com/ManuelBellucci/appium-ios-win-boilerplate.git
cd appium-ios-win-boilerplate
```

### Step 2: Install Dependencies
```bash
# Install Python dependencies
pip install -r requirements.txt
```

### Step 3: Configure Environment
```bash
# Copy environment template
copy e2eios\config\.env.example e2eios\config\.env
```

Edit `e2eios/config/.env` with your device details:
```env
# Appium Server Configuration
APPIUM_URL=http://127.0.0.1:4723
WDA_URL=http://127.0.0.1:8200

# iOS Device Configuration
IOS_UDID=YOUR_DEVICE_UDID_HERE
BUNDLE_ID=com.apple.Preferences

# go-ios Path
GO_IOS_EXE=C:\tools\go-ios\ios.exe

# Optional: WebDriverAgent Bundle ID (if different from default in start.ps1)
# WDA_BUNDLE_ID=com.yourcompany.WebDriverAgentRunner
```

> **📝 Important**: After setting up WebDriverAgent, remember to update the bundle ID in `tools/start.ps1` line 69 to match your custom WebDriverAgent bundle identifier.

### Step 4: Setup Appium Inspector
Configure Appium Inspector with the capabilities from `inspector.txt`:
```json
{
  "platformName": "iOS",
  "appium:automationName": "XCUITest",
  "appium:udid": "YOUR_UDID",
  "appium:webDriverAgentUrl": "http://127.0.0.1:8200",
  "appium:bundleId": "YOUR_APP_BUNDLE_ID",
  "appium:noReset": true,
  "appium:autoAcceptAlerts": true,
  "appium:newCommandTimeout": 120,
  "appium:includeSafariInWebviews": true,
  "appium:connectHardwareKeyboard": true
}
```

## 🎯 Quick Start

### Method 1: GUI Control Panel (Recommended)
```bash
python e2eios\scripts\control_panel.py
```

The control panel provides:
- 📊 **Real-time service status**
- 🚀 **One-click service startup**
- 🔍 **Device detection and connection testing**
- 🧹 **Dark mode console with clear functionality**
- ⌨️ **Keyboard shortcuts** (Ctrl+L to clear, F5 to refresh)

### Method 2: PowerShell Scripts
```powershell
# Start all services
.\tools\start.ps1

# Test connections
python e2eios\scripts\test_connection.py

# Stop services
.\tools\stop.ps1
```

## 📁 Project Structure

```
appium-ios-win-boilerplate/
├── 📂 e2eios/
│   ├── 📂 config/
│   │   ├── 📄 .env.example          # Environment template
│   │   ├── 📄 .env                  # Your configuration
│   │   ├── 📄 shortcuts.json        # Configurable keyboard shortcuts
│   │   └── 📄 app_config.json       # Optional app-specific config
│   ├── 📂 scripts/
│   │   ├── 🎮 control_panel.py      # Enhanced GUI Control Panel with auto-recovery
│   │   ├── 🔍 test_connection.py    # Connection validator
│   │   └── ⚙️ open_settings.py      # Sample automation script
│   └── 📂 utils/
│       ├── 📝 logger.py             # Logging utilities
│       ├── 🔧 env.py                # Environment loader
│       ├── 🔄 auto_recovery.py      # Auto-recovery system
│       └── ⌨️ shortcuts.py          # Shortcuts manager
├── 📂 tools/
│   ├── 🚀 start.ps1                 # Service startup script
│   └── 🛑 stop.ps1                  # Service shutdown script
├── 📂 logs/                         # Auto-generated logs
├── 📂 devimages/                    # iOS Developer Disk Images
├── 📄 inspector.txt                 # Appium Inspector capabilities
├── 📄 requirements.txt              # Python dependencies
└── 📖 README.md                     # This file
```

## 🔧 Configuration Guide

### Finding Your Device UDID

#### Method 1: Using iTunes/Finder
1. Connect iPhone to computer
2. Open iTunes (Windows) or Finder (macOS)
3. Select your device
4. Click on device info to reveal UDID

#### Method 2: Using go-ios
```bash
C:\tools\go-ios\ios.exe list
```

#### Method 3: Using Control Panel
The GUI control panel will auto-detect connected devices and display UDIDs.

### WebDriverAgent Setup & Deployment Workflow
> **⚠️ Compilation MUST be done on macOS with Xcode, but deployment can be done on Windows**

#### 🔄 **Understanding the Workflow**

This process involves **two phases**:
1. **📦 Compilation Phase** (macOS with Xcode) - Build the WDA app
2. **📱 Deployment Phase** (Windows with iPhone) - Sideload and run automation

#### 📦 **Phase 1: Complete WebDriverAgent Compilation Guide (macOS)**

> **👨‍💻 This comprehensive guide covers the ENTIRE process from start to finish**

##### **Prerequisites**
- **macOS with Xcode 12.0+** installed
- **Active Apple Developer Account** ($99/year)
- **Command Line Tools** installed
- **Node.js 16+** installed

##### **Step 1: Download and Setup WebDriverAgent**

1. **Clone WebDriverAgent Repository**:
   ```bash
   git clone https://github.com/appium/WebDriverAgent.git
   cd WebDriverAgent
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   # Note: bootstrap.sh script may not exist in newer versions - npm install is sufficient
   ```

3. **Open Xcode Project**:
   ```bash
   open WebDriverAgent.xcodeproj
   ```

##### **Step 2: Apple Developer Account Setup**

1. **Create App IDs** (Apple Developer Portal):
   - Go to [Apple Developer Portal](https://developer.apple.com/account)
   - Navigate to **Certificates, Identifiers & Profiles** → **Identifiers**
   - Click **"+"** to create new App ID
   - Select **"App"** and click **"Continue"**
   - Create these App IDs:
     - Description: `WebDriverAgent Runner` | Bundle ID: `com.yourname.WebDriverAgentRunner`
     - Description: `WebDriverAgent Lib` | Bundle ID: `com.yourname.WebDriverAgentLib`

2. **Register Target Device UDIDs**:
   - In Developer Portal: **Certificates, Identifiers & Profiles** → **Devices**
   - Click **"+"** to register new device
   - Get UDID from: iTunes, go-ios, or Xcode (Window → Devices and Simulators)
   - Add all iPhones that will use this automation

3. **Create Provisioning Profile**:
   - Go to **Certificates, Identifiers & Profiles** → **Profiles**
   - Click **"+"** to create new profile
   - Select **"iOS App Development"**
   - Choose your App ID (`com.yourname.WebDriverAgentRunner`)
   - Select your development certificate
   - Select all target devices
   - Name it: `WebDriverAgent Development`
   - Download and install the profile

##### **Step 3: Xcode Project Configuration**

1. **Configure WebDriverAgentRunner Target**:
   - Select **WebDriverAgentRunner** target in project navigator
   - Go to **"Signing & Capabilities"** tab
   - **Team**: Select your Apple Developer team
   - **Bundle Identifier**: Change to `com.yourname.WebDriverAgentRunner`
   - **Automatically manage signing**: ✅ Checked
   - Verify: **Signing Certificate** shows "Apple Development: YOUR_NAME"
   - Verify: **Provisioning Profile** shows "Xcode Managed Profile"

2. **Configure WebDriverAgentLib Target**:
   - Select **WebDriverAgentLib** target
   - **Team**: Select your Apple Developer team  
   - **Bundle Identifier**: Change to `com.yourname.WebDriverAgentLib`
   - **Automatically manage signing**: ✅ Checked
   - Verify: **Provisioning Profile** shows "None Required" (normal for libraries)

3. **Verify Configuration**:
   - Ensure both targets show **green checkmarks** (no red errors)
   - Both should use the same development team
   - Bundle identifiers should be unique and match your Apple Developer setup

##### **Step 4: Build and Export WebDriverAgent**

1. **Select Build Target**:
   - **Scheme**: Select `WebDriverAgentRunner` (top-left dropdown)
   - **Destination**: Select `Any iOS Device (arm64)`

2. **Build the Project**:
   ```bash
   # First, build to ensure everything works
   # In Xcode: Product → Build (⌘+B)
   ```
   - Wait for **"Build Succeeded"** message
   - Enter your Mac login password when prompted for keychain access

3. **Create Archive**:
   ```bash
   # In Xcode: Product → Archive
   ```
   - Wait for archive to complete
   - Organizer window will open automatically

4. **Export the App**:
   - In **Organizer**, select your WebDriverAgent archive
   - Click **"Distribute App"**
   - Select **"Archive"** (not "Built Products")
   - Click **"Next"**
   - Choose **"Development"** distribution
   - Select your team and provisioning profile
   - Click **"Export"** and choose save location

##### **Step 5: Extract and Prepare Files**

1. **Find the Built App**:
   ```bash
   # If export created a folder, look inside for:
   # - WebDriverAgentRunner.app
   # - OR navigate to the .xcarchive and extract manually
   
   # Alternative: Use Xcode to find build products
   # Product → Show Build Folder in Finder
   # Navigate to: Build/Products/Debug-iphoneos/WebDriverAgentRunner.app
   ```

2. **Create IPA File**:
   ```bash
   # Method 1: Simple rename (works for sideloading)
   cp -R WebDriverAgentRunner.app WebDriverAgentRunner-Runner.ipa
   
   # Method 2: Proper IPA structure
   mkdir Payload
   cp -R WebDriverAgentRunner.app Payload/
   zip -r WebDriverAgentRunner-Runner.ipa Payload/
   rm -rf Payload/
   ```

##### **Step 6: Export Developer Certificate & Provisioning Profile**

1. **Export Developer Certificate**:
   - **Open Keychain Access**: Applications → Utilities → Keychain Access
   - **Select "login" keychain** and click **"My Certificates"** category
   - **Find Your Certificate**: Look for **"Apple Development: YOUR_NAME (TEAM_ID)"**
   - **Click triangle** to expand and see the private key
   - **Cmd+Click** to select both certificate and private key
   - **Right-click** → **"Export 2 items..."**
   - **File Format**: Select **"Personal Information Exchange (.p12)"**
   - **Save As**: `developer.p12`
   - **Set a password** (remember this!)
   - **Save** and enter your Mac login password when prompted

2. **Export Provisioning Profile**:
   - **Method 1: From Apple Developer Portal**:
     - Go to [Apple Developer Portal](https://developer.apple.com/account)
     - Navigate to **Certificates, Identifiers & Profiles** → **Profiles**
     - Find your **"WebDriverAgent Development"** profile
     - Click **"Download"** to get the `.mobileprovision` file
   
   - **Method 2: From Xcode**:
     ```bash
     # Find provisioning profiles in Xcode's directory
     ls ~/Library/MobileDevice/Provisioning\ Profiles/
     
     # Copy all profiles to Desktop for easy access
     cp ~/Library/MobileDevice/Provisioning\ Profiles/*.mobileprovision ~/Desktop/
     ```
   
   - **Method 3: From Xcode Preferences**:
     - **Xcode** → **Preferences** → **Accounts**
     - **Select your Apple ID** → **Manage Certificates**
     - **Right-click** your development certificate → **"Export"**
     - This may also export associated provisioning profiles
   - **File Format**: Select **"Personal Information Exchange (.p12)"**
   - **Save As**: `developer.p12`
   - **Set a password** (remember this!)
   - **Save** and enter your Mac login password when prompted

##### **Step 7: Package for Windows**

**Files to transfer to Windows**:
- ✅ `WebDriverAgentRunner-Runner.ipa` (signed app)
- ✅ `developer.p12` (certificate + private key)
- ✅ `development.mobileprovision` (provisioning profile)
- 🔐 Certificate password (from export step)
- 📝 Bundle ID: `com.yourname.WebDriverAgentRunner`
- 📋 Target device UDIDs (for verification)

**Documentation to include**:
```
WebDriverAgent Package Contents:
- WebDriverAgentRunner-Runner.ipa: Signed app for sideloading
- developer.p12: Development certificate and private key  
- development.mobileprovision: Provisioning profile
- Certificate Password: [YOUR_PASSWORD_HERE]
- Bundle ID: com.yourname.WebDriverAgentRunner
- Compatible Device UDIDs: [LIST_YOUR_REGISTERED_DEVICES]
- Installation: Use Sideloadly, 3uTools, or Apple Configurator 2
```

**Complete Package Checklist**:
- [ ] WebDriverAgentRunner-Runner.ipa (signed app binary)
- [ ] developer.p12 (certificate + private key with password)
- [ ] .mobileprovision file (development provisioning profile) 
- [ ] Bundle ID documented (com.yourname.WebDriverAgentRunner)
- [ ] Device UDIDs verified and documented
- [ ] Installation instructions provided

#### 📱 **Phase 2: Deployment on Windows (Automation User)**

> **🖥️ This phase is done on Windows machines where the iOS automation will run**

##### **Step 1: Receive WDA Package**
- Get the WebDriverAgent package from your Mac developer
- Note the exact Bundle ID used during compilation

##### **Step 2: Sideload WebDriverAgent to iPhone**

**Option 1: Using Sideloadly (Recommended)**
1. **Install Sideloadly** from [Sideloadly Official Website](https://sideloadly.io/)
2. **Connect iPhone** to Windows PC via USB (use USBA to Lightning, not USBC to Lightning)
3. **Trust the computer** on your iPhone
4. **Insert the ipa** in Sideloadly and put your Apple ID of the device.
5. **Install** will begin automatically

**Option 2: Using Apple Configurator 2 (Recommended)**
1. **Install Apple Configurator 2** from Microsoft Store
2. **Connect iPhone** to Windows PC via USB
3. **Trust the computer** on your iPhone
4. **Drag and drop** the `.ipa` file onto your device in Configurator
5. **Install** will begin automatically

**Option 3: Using 3uTools**
1. **Download 3uTools** (free iOS device manager)
2. **Connect iPhone** to Windows PC
3. **Go to Apps** > **Install Local Apps**
4. **Select the `.ipa` file** and install


##### **Step 3: Trust Developer Profile on iPhone**

1. **Open iPhone Settings**:
   - Go to **Settings** > **General** > **VPN & Device Management**
   - Or **Settings** > **General** > **Profiles & Device Management**

2. **Trust Developer Profile**:
   - Find your developer profile (Apple Development: your.email@domain.com)
   - Tap on it and select **Trust**
   - Confirm by tapping **Trust** again

3. **Verify Installation**:
   - WebDriverAgent app should appear on your home screen
   - Try launching it - should open without crashing (may show blank screen)

##### **Step 4: Configure Windows Automation Project**

1. **Update Bundle ID in start.ps1**:
   Edit `tools/start.ps1` on line 69:
   ```powershell
   # Change this line:
   $Bundle = "com.yourwdaname.WebDriverAgentRunner"
   
   # To the EXACT bundle ID from compilation:
   $Bundle = "com.yourcompany.WebDriverAgentRunner"
   ```

2. **Update Environment Variables**:
   Add to your `.env` file:
   ```env
   WDA_BUNDLE_ID=com.yourcompany.WebDriverAgentRunner
   ```

3. **Configure Device UDID**:
   ```env
   IOS_UDID=YOUR_DEVICE_UDID_HERE
   ```

#### ✅ **Phase 3: Testing the Setup**

1. **Open Appium Wizard and start server on port 4723** 
   - Open Appium Wizard
   - Go to server -> configuration
   - It will start. It uses to give errors but works anyways.

2. **Test with Control Panel**:
   - Run: `python e2eios\scripts\control_panel.py`
   - Click **"Start Services"**
   - At this point, Check if Appium Server and WebDriverAgent status shows "✅ Running", and device connected.

3. **Direct Connection Test**:
   - After starting services, if you want to be sure, open browser
   - Navigate to: `http://127.0.0.1:8200/status`
   - Should return JSON with device information

On error try to
**Launch WebDriverAgent Manually**:
   - Open the WebDriverAgent app on your iPhone
   - Keep it running (don't close it)

#### 🚨 **Common Issues in Deployment Phase**

**❌ "App won't install on Windows"**:
- Verify device UDID was registered during compilation phase
- Check that provisioning profile includes your device
- Make sure iPhone storage has space for the app

**❌ "Untrusted Developer" error**:
- Go to iPhone Settings and trust the developer profile
- Make sure you're trusting the correct profile
- Restart iPhone after trusting if needed

**❌ "WebDriverAgent crashes on launch"**:
- Check that bundle ID in start.ps1 matches exactly
- Verify device UDID is correct in .env file
- Try deleting and reinstalling the WDA app
- In any case with all working, the WDA app will "open and close" instantly, you don't need to open it usually. The script start.ps1 will do itself. 

**❌ "Connection refused" when testing**:
- Make sure WebDriverAgent app is running on iPhone
- Check Windows firewall isn't blocking port 8200
- Verify iPhone and PC are on same network (if using Wi-Fi)

#### 💡 **Pro Tips for Team Workflow**

1. **For Mac Developer**:
   - Build multiple variants if team uses different bundle IDs
   - Include detailed bundle ID documentation with each build
   - Test on at least one device before distributing

2. **For Windows Automation User**:
   - Always verify bundle ID matches exactly
   - Keep WebDriverAgent running during automation sessions
   - Document your device UDID for future re-builds

3. **Team Coordination**:
   - Maintain a shared list of device UDIDs for provisioning
   - Use consistent bundle ID naming across team
   - Set up automated build process if doing frequent updates
   - Tap on it and select **Trust**
   - Confirm by tapping **Trust** again

3. **Verify Installation**:
   - Try launching the WebDriverAgent app from your home screen
   - It should open without crashing (may show a blank/white screen - this is normal)

#### 🔧 **Step 5: Configure Bundle ID in Project**

**IMPORTANT**: After building WebDriverAgent with your custom bundle ID, you need to update the project configuration:

1. **Note Your Bundle ID**: Remember the bundle ID you used (e.g., `com.mycompany.WebDriverAgentRunner`)

2. **Update start.ps1**:
   Edit `tools/start.ps1` on line 69:
   ```powershell
   # Change this line:
   $Bundle = "com.yourwdaname.WebDriverAgentRunner"
   
   # To your actual bundle ID:
   $Bundle = "com.mycompany.WebDriverAgentRunner"
   ```

3. **Update Environment Variables** (Optional):
   You can also add this to your `.env` file:
   ```env
   WDA_BUNDLE_ID=com.johndoe.WebDriverAgentRunner
   ```

#### ✅ **Step 6: Verify WebDriverAgent Installation**

1. **Automated Test**:
   - Run the control panel: `python e2eios\scripts\control_panel.py`
   - Click **"Start Services"** 
   - Check if WebDriverAgent status shows "✅ Running"

2. **Direct URL Test**:
   - After starting services, open browser
   - Navigate to: `http://127.0.0.1:8200/status` or curl it.
   - Should return JSON response with device information

#### 🚨 **Common WebDriverAgent Issues**

**❌ Code Signing Error**:
- Ensure your Apple Developer account has active membership
- Check that your device UDID is registered in the provisioning profile
- Try cleaning project: **Product** > **Clean Build Folder**

**❌ "Could not launch WebDriverAgent"**:
- Make sure the app is trusted in device settings
- Manually launch the app once from the home screen
- Check that device is unlocked during automation

**❌ Bundle ID Conflicts**:
- Make sure your bundle ID is unique (don't use Facebook's default)
- Verify bundle ID matches exactly in start.ps1 configuration
- Check for typos in the bundle identifier

**❌ Provisioning Profile Issues**:
- Refresh provisioning profiles in Xcode: **Preferences** > **Accounts** > **Download Manual Profiles**
- Make sure you're using a Development provisioning profile, not Distribution

#### 📝 **Why Custom Bundle ID is Required**

The default WebDriverAgent uses Facebook's bundle identifier (`com.facebook.WebDriverAgentRunner`). You MUST change this because:

1. **Code Signing**: You can't sign apps with someone else's bundle ID
2. **Apple Store Policies**: Facebook's bundle ID is reserved 
3. **Provisioning**: Your provisioning profile won't work with Facebook's identifier
4. **Automation**: go-ios needs the correct bundle ID to communicate with your WDA installation
5. **Security**: Could lead to bans

**Example Bundle ID Format**:
- ✅ `com.yourcompany.WebDriverAgentRunner`
- ✅ `com.johndoe.WebDriverAgentRunner` 
- ✅ `com.myteam.WebDriverAgentRunner`
- ❌ `com.facebook.WebDriverAgentRunner` (default, NOT RECOMMENDED)

## 🎮 Using the Enhanced Control Panel

### Features Overview
- 📱 **Device Information**: Shows detected UDID and connection status
- 📊 **Advanced Service Status**: Real-time monitoring with auto-recovery indicators for:
  - Appium Server (with health status and recovery attempts)
  - WebDriverAgent (with connection monitoring and auto-restart)
  - Device Connection (with reconnection handling)
  - go-ios Process (with process monitoring and restart)
- 🎛️ **Enhanced Control Buttons**: 
  - Start/Stop services with progress indication
  - Test connections with detailed diagnostics
  - Refresh devices with auto-detection
  - Auto-recovery controls (pause/resume, force recovery)
  - Log export and console management
- 🖥️ **Professional Dark Console**: Color-coded logging with enhanced themes
- ⌨️ **Configurable Keyboard Shortcuts**: Fully customizable shortcuts for all actions

### Auto-Recovery System
The enhanced control panel includes a comprehensive auto-recovery system:

#### **Service Health Monitoring**
- **Continuous Monitoring**: Each service is monitored every 10-20 seconds
- **Health States**: Services can be Healthy, Degraded, Failed, Recovering, or Unknown
- **Visual Indicators**: Real-time status updates with color-coded indicators
- **Recovery Tracking**: Shows recovery attempts and failure counts

#### **Intelligent Recovery Actions**
- **Appium Server**: Restart Appium Wizard, kill stuck processes
- **WebDriverAgent**: Restart port forwarding, restart WDA service
- **Device Connection**: Refresh connection, restart device services
- **go-ios Process**: Restart go-ios processes, refresh device list

#### **Recovery Configuration**
- **Failure Thresholds**: Configurable failure limits before recovery triggers
- **Backoff Strategy**: Exponential backoff between recovery attempts
- **Cooldown Periods**: Prevents excessive recovery attempts
- **Global Limits**: Maximum recovery attempts per service

### Keyboard Shortcuts System
The panel supports fully configurable keyboard shortcuts:

#### **Default Shortcuts**
- `Ctrl+L` - Clear console output
- `F5` - Refresh device list
- `Ctrl+S` - Start all services
- `Ctrl+Q` - Stop all services
- `Ctrl+T` - Test connections
- `Ctrl+R` - Toggle auto-recovery on/off
- `Ctrl+Shift+R` - Force recovery for all services
- `F1` - Show keyboard shortcuts help
- `Ctrl+M` - Minimize control panel
- `Ctrl+E` - Export console logs to file

#### **Service-Specific Shortcuts**
- `Ctrl+1` - Force restart Appium service
- `Ctrl+2` - Force restart WebDriverAgent
- `Ctrl+3` - Force device reconnection
- `Ctrl+4` - Force restart go-ios processes

#### **Console Navigation**
- `Ctrl+Home` - Scroll console to top
- `Ctrl+End` - Scroll console to bottom
- `Ctrl+Plus` - Increase console font size
- `Ctrl+Minus` - Decrease console font size

#### **Script Execution**
- `Ctrl+Shift+O` - Run open settings script
- `Ctrl+Shift+T` - Run connection test script

### Console Color Coding
- 🟢 **Green**: Success messages (✅, "successful", "ok")
- 🔴 **Red**: Error messages (❌, "error", "failed")
- 🟡 **Yellow**: Warning messages (⚠️, "warning", "timeout")
- 🟣 **Purple**: Recovery messages (🔧, "recovery", "restart")
- ⚪ **White**: General information
- 🔘 **Gray**: Timestamps

### Customizing Shortcuts
Edit `e2eios/config/shortcuts.json` to customize keyboard shortcuts:

```json
{
  "shortcuts": {
    "panel_actions": {
      "your_custom_action": {
        "key": "Control-y",
        "description": "Your custom action",
        "action": "your_action_handler",
        "enabled": true
      }
    }
  }
}
```

### Auto-Recovery Configuration
The auto-recovery system can be configured by modifying the AutoRecoveryManager settings:

- **Monitoring Intervals**: How often each service is checked
- **Failure Thresholds**: Number of failures before recovery triggers
- **Recovery Cooldowns**: Time between recovery attempts
- **Global Limits**: Maximum recovery attempts per service

## 🔄 Auto-Recovery System

The iOS Automation Boilerplate includes a comprehensive auto-recovery system that monitors service health and automatically restarts failed components.

### **System Architecture**

#### **Service Monitoring**
The auto-recovery system continuously monitors four key components:

1. **Appium Server** (`http://127.0.0.1:4723`)
   - HTTP health checks every 10 seconds
   - Monitors `/status` endpoint availability
   - Tracks response times and error rates

2. **WebDriverAgent** (`http://127.0.0.1:8200`)
   - Port connectivity checks every 10 seconds  
   - Monitors WDA service availability
   - Tracks port forwarding status

3. **Device Connection**
   - Device UDID presence checks every 15 seconds
   - Uses go-ios to validate device connectivity
   - Monitors USB connection stability

4. **go-ios Process**
   - Process monitoring every 20 seconds
   - Checks for running ios.exe processes
   - Validates process health and responsiveness

#### **Health States**
Each service can be in one of five states:

- 🟢 **Healthy**: Service operating normally
- 🟡 **Degraded**: Minor issues detected, monitoring increased
- 🔴 **Failed**: Service down, recovery triggered
- 🟣 **Recovering**: Recovery actions in progress
- ⚪ **Unknown**: Unable to determine service state

#### **Recovery Actions**

**Appium Server Recovery:**
```
1. Restart Appium Wizard application
2. Kill stuck Appium processes (node.exe, appium.exe)
3. Verify service restoration
```

**WebDriverAgent Recovery:**
```
1. Restart port forwarding (8200 -> 8100)
2. Kill and restart go-ios processes
3. Re-establish WDA connection
4. Restart WDA service if needed
```

**Device Connection Recovery:**
```
1. Refresh device connection via go-ios list
2. Restart Apple Mobile Device Service
3. Re-detect device UDID
4. Validate device trust status
```

**go-ios Process Recovery:**
```
1. Kill existing ios.exe processes
2. Clean up port forwarding
3. Restart device monitoring
```

### **Configuration Options**

#### **Failure Thresholds**
```python
# Number of consecutive failures before recovery
APPIUM_MAX_FAILURES = 3      # 30 seconds of failures
WDA_MAX_FAILURES = 3         # 30 seconds of failures  
DEVICE_MAX_FAILURES = 2      # 30 seconds of failures
GO_IOS_MAX_FAILURES = 2      # 40 seconds of failures
```

#### **Recovery Limits**
```python
GLOBAL_MAX_RECOVERY_ATTEMPTS = 5    # Per service
RECOVERY_COOLDOWN_MINUTES = 5       # Between attempts
EXPONENTIAL_BACKOFF = True          # Increasing delays
```

#### **Monitoring Intervals**
```python
APPIUM_CHECK_INTERVAL = 10          # seconds
WDA_CHECK_INTERVAL = 10             # seconds
DEVICE_CHECK_INTERVAL = 15          # seconds
GO_IOS_CHECK_INTERVAL = 20          # seconds
```

### **Using Auto-Recovery**

#### **Automatic Operation**
Auto-recovery runs automatically when you start the enhanced control panel:

```bash
python e2eios\scripts\control_panel.py
```

The system will:
- Start monitoring all services immediately
- Display real-time health status
- Automatically trigger recovery when failures occur
- Log all recovery actions to the console

#### **Manual Control**
You can control auto-recovery manually:

```python
# Toggle auto-recovery on/off
Ctrl+R                    # Keyboard shortcut
# or click "Pause Recovery" button

# Force recovery for all services  
Ctrl+Shift+R             # Keyboard shortcut
# or click "Force Recovery" button

# Force recovery for specific services
Ctrl+1                   # Force Appium restart
Ctrl+2                   # Force WDA restart
Ctrl+3                   # Force device reconnection
Ctrl+4                   # Force go-ios restart
```

#### **Monitoring Dashboard**
The control panel shows detailed recovery information:

```
📊 Service Status & Auto-Recovery
┌─────────────────┬─────────────┬──────────────────┐
│ Service         │ Status      │ Recovery Info    │
├─────────────────┼─────────────┼──────────────────┤
│ Appium Server   │ ✅ Healthy  │                  │
│ WebDriverAgent  │ 🔧 Recovery │ Recovery in progress... │
│ Device Connect  │ ⚠️ Degraded │ Failures: 1      │
│ go-ios Process  │ ❌ Failed   │ Attempts: 2      │
└─────────────────┴─────────────┴──────────────────┘
```

### **Recovery Logs**
All recovery actions are logged with detailed information:

```
[10:30:45] 🔄 Auto-recovery system is active and monitoring services
[10:35:12] ⚠️ WebDriverAgent service degraded (consecutive failures: 2/3)
[10:35:42] ❌ WebDriverAgent failed - recovery will be attempted
[10:35:43] 🔧 Auto-recovery started for wda
[10:35:43] 🔧 Executing recovery action: restart_wda_forward
[10:35:58] ✅ WebDriverAgent recovered successfully
```

### **Advanced Configuration**

You can customize auto-recovery behavior by modifying the `AutoRecoveryManager`:

```python
# In your custom script
from e2eios.utils.auto_recovery import AutoRecoveryManager

# Initialize with custom settings
recovery_manager = AutoRecoveryManager(config_path, "MyScript")

# Customize service monitoring
recovery_manager.services['appium']['check_interval'] = 5  # Check every 5 seconds
recovery_manager.services['appium']['max_failures'] = 5    # Allow 5 failures

# Add custom recovery actions
def my_custom_recovery():
    # Your custom recovery logic
    return True

recovery_manager.services['appium']['recovery_actions'].append(
    RecoveryAction(
        name="my_custom_action",
        action=my_custom_recovery,
        max_attempts=3,
        description="My custom recovery action"
    )
)

# Start monitoring
recovery_manager.start_monitoring()
```

### **Troubleshooting Auto-Recovery**

#### **Common Issues**

**Recovery Not Triggering:**
- Check that auto-recovery is enabled (green indicator in panel)
- Verify service monitoring intervals aren't too long
- Ensure failure thresholds are appropriate for your setup

**Excessive Recovery Attempts:**
- Increase failure thresholds to reduce sensitivity
- Extend recovery cooldown periods
- Check for underlying infrastructure issues

**Services Not Staying Healthy:**
- Review service logs in the `logs/` directory
- Check system resources (CPU, memory)
- Verify network connectivity and firewall settings
- Ensure device USB connection is stable

#### **Debug Mode**
Enable detailed recovery logging:

```python
# Set debug mode in control panel
recovery_manager = AutoRecoveryManager(config_path, "Debug")
recovery_manager.logger.enable_debug = True
```

This will provide verbose logging of all recovery operations and health checks.

---

### 1. Verify All Services
```bash
python e2eios\scripts\test_connection.py
```

### 2. Run Sample Automation
```bash
python e2eios\scripts\open_settings.py
```

### 3. Check Logs
Monitor logs in the `logs/` directory for detailed debugging information.

## 🛡️ Troubleshooting

### Common Issues

#### ❌ "Device not connected"
- ✅ Ensure iPhone is connected via USBA
- ✅ Trust the computer on your iPhone
- ✅ Verify UDID in `.env` file matches your device
- ✅ Check that iTunes/Apple Mobile Device Service recognizes device

#### ❌ "WebDriverAgent not responding"
- ✅ Ensure WDA is installed and trusted on iPhone
- ✅ Manually launch WebDriverAgent app on device
- ✅ Check certificates haven't expired
- ✅ Verify port 8200 is not blocked by firewall

#### ❌ "Appium connection failed"
- ✅ Start Appium Server (Desktop/Wizard) on port 4723
- ✅ Check firewall settings
- ✅ Verify Appium version compatibility

#### ❌ "go-ios not found"
- ✅ Download go-ios from GitHub releases
- ✅ Extract to `C:\tools\go-ios\ios.exe`
- ✅ Update `GO_IOS_EXE` path in `.env` if using different location

### Debug Mode
Enable detailed logging by modifying scripts:
```python
logger = get_logger("YourComponent", enable_debug=True)
```

## ⚖️ Legal Disclaimer

> **📢 Important Notice**: This project is provided as-is for the developer and testing community.

### 🎯 **Intended Use**
This iOS automation framework is designed **exclusively** for:
- ✅ **Software Testing** - Automated testing of your own applications
- ✅ **Development** - Building and testing iOS apps during development
- ✅ **Quality Assurance** - Legitimate QA processes and workflows
- ✅ **Educational Purposes** - Learning iOS automation techniques
- ✅ **Personal Projects** - Automating your own devices and applications

### 🚫 **Prohibited Use**
This framework **MUST NOT** be used for:
- ❌ **Terms of Service Violations** - Breaking any app's ToS or EULA
- ❌ **Unauthorized Access** - Accessing systems without permission
- ❌ **Commercial Abuse** - Violating platform policies for commercial gain
- ❌ **Malicious Activities** - Any harmful, illegal, or unethical purposes
- ❌ **Policy Violations** - Breaking Apple App Store or platform guidelines

### 💝 **Community Spirit**
This project is shared with **love** for the community of:
- 👨‍💻 **Developers** building amazing iOS applications
- 🧪 **Testers** ensuring quality and reliability
- 🎓 **Students** learning mobile automation
- 🔧 **Engineers** solving complex testing challenges

### 🛡️ **Disclaimer of Responsibility**
- **No Liability**: The author(s) assume **NO RESPONSIBILITY** for how this framework is used
- **User Responsibility**: You are **solely responsible** for ensuring your use complies with all applicable laws, terms of service, and platform policies
- **As-Is Basis**: This software is provided "as-is" without warranties of any kind
- **Legal Compliance**: Users must ensure their automation activities are legal and authorized
- **Platform Policies**: Respect all platform terms, conditions, and usage policies

### 📜 **Your Responsibility**
By using this framework, you agree to:
1. **Use it ethically** and in compliance with all applicable laws
2. **Respect platform policies** and terms of service
3. **Only automate applications** you own or have explicit permission to test
4. **Take full responsibility** for your automation activities
5. **Not hold the author liable** for any misuse or consequences

### 💫 **Final Note**
This project exists to **empower legitimate developers and testers** to build better software. Please use it responsibly and contribute to a positive, ethical development community.

**🙏 Thank you for being part of the responsible automation community!**

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Appium](https://appium.io/) - Cross-platform automation framework
- [go-ios](https://github.com/danielpaulus/go-ios) - iOS device communication
- [WebDriverAgent](https://github.com/appium/WebDriverAgent) - iOS automation agent

## 💬 Support

- 📚 Check the [documentation](docs/)
- 🐛 Report issues in [GitHub Issues](issues/)
- 💡 Request features in [GitHub Discussions](discussions/)

---

**Happy Automating! 🚀📱**