# Domain92 Discord Bot - IP Blocking & Proxy Guide

## Overview

This guide explains how to handle IP blocking issues when using the Domain92 Discord bot. When you get IP blocked, you'll see errors like "Username and password invalid" immediately after activating an account while trying to log in.

## Quick Solutions

### 1. Use Tor (Recommended)
```bash
# Run the Tor setup helper
python setup_tor.py
```

### 2. Use SOCKS5 Proxy
```bash
# Set a SOCKS5 proxy
!setproxy socks5://your-proxy-server:1080
```

### 3. Use HTTP Proxy
```bash
# Set an HTTP proxy
!setproxy http://username:password@proxy-server:8080
```

## Bot Commands for IP Blocking

### Basic Proxy Management
- `!setproxy <url>` - Set a custom proxy URL
- `!rotateproxy` - Switch to the next proxy in the pool
- `!listproxies` - Show all available proxies
- `!testproxy [url]` - Test if a proxy is working

### IP Block Protection
- `!handleblock` - Manually handle IP blocking by switching proxy
- `!setmaxretries <number>` - Set max retries before auto-switching (1-10)

### Advanced Proxy Management
- `!addproxy <url>` - Add custom proxy to rotation pool
- `!removeproxy <index>` - Remove proxy from pool by index

## Automatic IP Block Detection

The bot automatically detects IP blocking by monitoring for these error messages:
- "Username and password invalid"
- "ip blocked" (case insensitive)

When detected, the bot will:
1. Increment the blocked attempts counter
2. After reaching max retries (default: 3), automatically switch to the next proxy
3. Reset the counter and notify you of the new proxy

## Proxy Types Supported

### 1. Tor (SOCKS5)
```
socks5://127.0.0.1:9050
```
**Advantages:**
- Most reliable for avoiding IP blocks
- Free and anonymous
- Automatic IP rotation

**Setup:**
```bash
# Install Tor
# Windows: Download from torproject.org
# Linux: sudo apt install tor
# macOS: brew install tor

# Start Tor service
# Linux: sudo systemctl start tor
# macOS: brew services start tor
```

### 2. SOCKS5 Proxy
```
socks5://proxy-server:1080
socks5://username:password@proxy-server:1080
```

### 3. HTTP/HTTPS Proxy
```
http://proxy-server:8080
http://username:password@proxy-server:8080
https://proxy-server:8443
```

## Default Proxy Pool

The bot comes with a pre-configured proxy pool:
1. `none` - No proxy (direct connection)
2. `socks5://127.0.0.1:9050` - Local Tor proxy
3. `http://185.199.229.156:7492` - HTTP proxy
4. `http://185.199.228.220:7492` - HTTP proxy
5. `http://185.199.231.45:7492` - HTTP proxy
6. `http://185.199.230.102:7492` - HTTP proxy
7. `socks5://127.0.0.1:1080` - Alternative SOCKS5 port

## Step-by-Step Setup

### 1. Start a Session
```
!start
```

### 2. Configure Proxy (Optional)
```
!setproxy socks5://127.0.0.1:9050
```

### 3. Test Proxy
```
!testproxy
```

### 4. Run Domain Generation
```
!run
```

### 5. Handle IP Blocking (if needed)
```
!handleblock
```

## Troubleshooting

### Proxy Not Working
1. Check if proxy server is online
2. Verify credentials (if required)
3. Test with `!testproxy`
4. Try a different proxy with `!rotateproxy`

### Tor Not Working
1. Ensure Tor is installed and running
2. Check if port 9050 is open
3. Run `python setup_tor.py` for setup help
4. Verify firewall settings

### Still Getting IP Blocked
1. Increase max retries: `!setmaxretries 5`
2. Add more proxies to pool: `!addproxy <url>`
3. Use a different proxy type
4. Wait before retrying (some blocks are temporary)

## Best Practices

1. **Use Tor First**: Tor is the most reliable for avoiding IP blocks
2. **Test Proxies**: Always test proxies before using them
3. **Rotate Proxies**: Don't rely on a single proxy
4. **Monitor Attempts**: Keep track of blocked attempts
5. **Use Quality Proxies**: Free proxies are often unreliable

## Error Messages

### Common Errors and Solutions

**"Username and password invalid"**
- Solution: Use `!handleblock` to switch proxy

**"Proxy connection failed"**
- Solution: Test proxy with `!testproxy` and try another

**"Tor not running"**
- Solution: Start Tor service or use `python setup_tor.py`

**"Too many blocked attempts"**
- Solution: Increase max retries or add more proxies

## Advanced Configuration

### Custom Proxy Pool
You can customize the proxy pool by editing the bot code or using commands:
```python
# In Domain92Session.__init__()
self.proxy_pool = [
    "socks5://your-tor:9050",
    "http://your-http-proxy:8080",
    "socks5://your-socks5-proxy:1080"
]
```

### Automatic Proxy Rotation
The bot automatically rotates proxies when:
- IP blocking is detected
- Max retries are reached
- Manual rotation is requested

## Security Notes

1. **Proxy Credentials**: Never share proxy credentials in public channels
2. **Tor Usage**: Be aware of Tor's legal status in your jurisdiction
3. **Rate Limiting**: Don't abuse proxy services
4. **Privacy**: Some proxies may log your traffic

## Support

If you encounter issues:
1. Check this guide first
2. Use `!domainhelp` for command reference
3. Test your setup with `!testproxy`
4. Try the Tor setup helper: `python setup_tor.py` 