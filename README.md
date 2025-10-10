# 📱 iOS Automation Boilerplate

> A comprehensive Windows-based iOS automation framework using Appium, WebDriverAgent, and go-ios for seamless iOS app testing and automation. This is a FULLY CUSTOMIZABLE base boilerplate and guide to set-up Appium on Windows. Something may seem hard for someone made so easy. From this, get your UI testing to another level and save time, only updating the scripts and panel.

[![Platform](https://img.shields.io/badge/platform-iOS-blue.svg)](https://developer.apple.com/ios/)
[![Framework](https://img.shields.io/badge/framework-Appium-green.svg)](https://appium.io/)
[![Language](https://img.shields.io/badge/language-Python-yellow.svg)](https://python.org/)
[![OS](https://img.shields.io/badge/os-Windows-lightgrey.svg)](https://microsoft.com/windows/)

## 🚀 Features

- ✅ **Complete iOS Device Management** - Automated device setup and WebDriverAgent deployment
- 🎮 **GUI Control Panel** - User-friendly interface with dark mode console
- 🔧 **PowerShell Automation** - Streamlined service management scripts
- 📊 **Real-time Monitoring** - Live status checking for all services
- 🧪 **Connection Testing** - Built-in validation tools
- 📝 **Comprehensive Logging** - Detailed logging with timestamps and color coding
- 🔄 **Auto-recovery** - Robust error handling and service restart capabilities

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
│   │   └── 📄 app_config.json       # Optional app-specific config
│   ├── 📂 scripts/
│   │   ├── 🎮 control_panel.py      # GUI Control Panel
│   │   ├── 🔍 test_connection.py    # Connection validator
│   │   └── ⚙️ open_settings.py      # Sample automation script
│   └── 📂 utils/
│       ├── 📝 logger.py             # Logging utilities
│       └── 🔧 env.py                # Environment loader
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

#### 📦 **Phase 1: Compilation on macOS (Developer/Team Member)**

> **👨‍💻 This phase requires a Mac with Xcode and should be done by someone with macOS access**

##### **Step 1: Download and Setup WebDriverAgent**

1. **Clone WebDriverAgent Repository**:
   ```bash
   git clone https://github.com/appium/WebDriverAgent.git
   cd WebDriverAgent
   ```

2. **Install Dependencies**:
   ```bash
   npm install
   ./Scripts/bootstrap.sh
   ```

##### **Step 2: Configure Xcode Project**

1. **Open Project in Xcode**:
   - Open `WebDriverAgent.xcodeproj` in Xcode
   - You'll see multiple targets in the project

2. **Select Development Team**:
   - Select `WebDriverAgentLib` target
   - Go to **Signing & Capabilities** tab
   - Select your **Apple Developer Team**
   - Repeat for `WebDriverAgentRunner` and `WebDriverAgent` targets

3. **Configure Bundle Identifiers**:
   
   **For WebDriverAgentRunner target**:
   - Change Bundle Identifier from `com.facebook.WebDriverAgentRunner` 
   - To: `com.yourcompany.WebDriverAgentRunner` (use your own domain)
   
   **For WebDriverAgent target**:
   - Change Bundle Identifier from `com.facebook.WebDriverAgent`
   - To: `com.yourcompany.WebDriverAgent`
   - You can put whatever you want to be honest, an alias too.
4. **Register Target Device UDIDs**:
   - Collect UDIDs from Windows machines that will use the automation. You can connect the iPhone to the Windows and get UDID by go-ios on console or iTunes (DO NOT download from Microsoft Store, download official .exe instead)
   - Go to [Apple Developer Portal](https://developer.apple.com/account)
   - Navigate to **Certificates, Identifiers & Profiles** > **Devices**
   - Add all target device UDIDs to your provisioning profile

##### **Step 3: Build WebDriverAgent (Archive Method)**

> **📝 Note**: You DON'T need to connect the target iPhone to the Mac. You're just building the app.

1. **Select Generic iOS Device**:
   - In Xcode, select **"Any iOS Device (arm64)"** as target
   - This builds a universal app that can be deployed to any registered device

2. **Build for Archive**:
   - Select `WebDriverAgentRunner` scheme
   - Click **Product** > **Archive**
   - This creates a distributable `.ipa` file

3. **Export IPA**:
   - In the Organizer window, select your archive
   - Click **"Distribute App"**
   - Choose **"Development"** distribution
   - Select your team and provisioning profile
   - Export the `.ipa` file

4. **Package for Distribution**:
   Create a package containing:
   - 📄 `WebDriverAgentRunner.ipa` (the built app)
   - 📄 Bundle ID information (e.g., `com.yourcompany.WebDriverAgentRunner`)
   - 📄 Installation instructions for Windows users

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

## 🎮 Using the Control Panel

### Features Overview
- 📱 **Device Information**: Shows detected UDID and connection status
- 📊 **Service Status**: Real-time monitoring of Appium Server, WebDriverAgent, and Device Connection
- 🎛️ **Control Buttons**: Start/Stop services, Test connections, Refresh devices
- 🖥️ **Dark Console**: Color-coded logging with professional dark slate theme

### Console Color Coding
- 🟢 **Green**: Success messages (✅, "successful", "ok")
- 🔴 **Red**: Error messages (❌, "error", "failed")
- 🟡 **Yellow**: Warning messages (⚠️, "warning", "timeout")
- ⚪ **White**: General information
- 🔘 **Gray**: Timestamps

### Keyboard Shortcuts
- `Ctrl+L`: Clear console
- `F5`: Refresh device list

## 🧪 Testing Your Setup

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