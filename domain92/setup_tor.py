#!/usr/bin/env python3
"""
Tor Setup Helper for Domain92 Discord Bot
This script helps users set up Tor for proxy support to avoid IP blocking.
"""

import os
import sys
import subprocess
import platform

def check_tor_installed():
    """Check if Tor is installed on the system"""
    try:
        result = subprocess.run(['tor', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def install_tor_windows():
    """Provide instructions for installing Tor on Windows"""
    print("🌐 Tor Installation for Windows:")
    print("1. Download Tor Browser from: https://www.torproject.org/download/")
    print("2. Install Tor Browser")
    print("3. Or install Tor standalone:")
    print("   - Download from: https://www.torproject.org/download/tor/")
    print("   - Extract to C:\\tor")
    print("   - Add C:\\tor to your PATH environment variable")
    print("4. Create torrc file in C:\\tor\\torrc with:")
    print("   SocksPort 9050")
    print("   ControlPort 9051")
    print("   HashedControlPassword your_hashed_password")

def install_tor_linux():
    """Provide instructions for installing Tor on Linux"""
    print("🌐 Tor Installation for Linux:")
    print("Ubuntu/Debian:")
    print("  sudo apt update")
    print("  sudo apt install tor")
    print("")
    print("CentOS/RHEL/Fedora:")
    print("  sudo yum install tor  # or sudo dnf install tor")
    print("")
    print("Enable and start Tor service:")
    print("  sudo systemctl enable tor")
    print("  sudo systemctl start tor")

def install_tor_macos():
    """Provide instructions for installing Tor on macOS"""
    print("🌐 Tor Installation for macOS:")
    print("Using Homebrew:")
    print("  brew install tor")
    print("  brew services start tor")
    print("")
    print("Or download Tor Browser from:")
    print("  https://www.torproject.org/download/")

def setup_tor_config():
    """Create basic Tor configuration"""
    config_content = """# Basic Tor configuration for Domain92
SocksPort 9050
ControlPort 9051
# Uncomment and set a password for control access
# HashedControlPassword your_hashed_password_here
# RunAsDaemon 1
"""
    
    config_path = "torrc"
    if os.path.exists(config_path):
        print(f"⚠️  {config_path} already exists. Backing up...")
        os.rename(config_path, f"{config_path}.backup")
    
    with open(config_path, 'w') as f:
        f.write(config_content)
    
    print(f"✅ Created {config_path} configuration file")
    return config_path

def test_tor_connection():
    """Test if Tor is working"""
    try:
        import requests
        import socks
        import socket
        
        # Configure requests to use Tor
        session = requests.Session()
        session.proxies = {
            'http': 'socks5h://127.0.0.1:9050',
            'https': 'socks5h://127.0.0.1:9050'
        }
        
        print("🔄 Testing Tor connection...")
        response = session.get('http://httpbin.org/ip', timeout=10)
        
        if response.status_code == 200:
            ip_info = response.json()
            print(f"✅ Tor is working! Your IP: {ip_info.get('origin', 'Unknown')}")
            return True
        else:
            print(f"❌ Tor test failed with status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Tor test failed: {str(e)}")
        return False

def main():
    print("🌐 Domain92 Tor Setup Helper")
    print("=" * 40)
    print("This script helps you set up Tor for proxy support")
    print("to avoid IP blocking when using the Domain92 Discord bot.")
    print("")
    
    # Check if Tor is installed
    if check_tor_installed():
        print("✅ Tor is already installed!")
    else:
        print("❌ Tor is not installed.")
        print("")
        
        system = platform.system().lower()
        if system == "windows":
            install_tor_windows()
        elif system == "linux":
            install_tor_linux()
        elif system == "darwin":
            install_tor_macos()
        else:
            print(f"❌ Unsupported operating system: {system}")
            print("Please install Tor manually from: https://www.torproject.org/")
        
        print("")
        input("Press Enter after installing Tor...")
    
    # Create configuration
    print("")
    print("📝 Setting up Tor configuration...")
    config_path = setup_tor_config()
    
    # Test connection
    print("")
    if test_tor_connection():
        print("")
        print("🎉 Tor setup completed successfully!")
        print("")
        print("Your Domain92 Discord bot is now configured to use Tor.")
        print("When you get IP blocked, the bot will automatically:")
        print("1. Detect the 'Username and password invalid' error")
        print("2. Switch to the Tor proxy (socks5://127.0.0.1:9050)")
        print("3. Retry the operation with a new IP")
        print("")
        print("Commands you can use:")
        print("  !start          - Start a new session")
        print("  !handleblock    - Manually handle IP blocking")
        print("  !testproxy      - Test if Tor proxy is working")
        print("  !listproxies    - Show all available proxies")
    else:
        print("")
        print("⚠️  Tor setup incomplete. Please:")
        print("1. Make sure Tor is running on port 9050")
        print("2. Check your firewall settings")
        print("3. Verify the torrc configuration")
        print("4. Run this script again to test")

if __name__ == "__main__":
    main() 