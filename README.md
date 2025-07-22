# Hidden-IP
Program for auto-swap ip address.
This script uses the Tor SOCKS5 proxy (`127.0.0.1:9050`) to hide your IP address and automatically change it every 10 seconds.
----------------------------

## ⚙️ Tor Setup
* Download the Tor Expert Bundle for Windows:

* https://www.torproject.org/download/tor/

* 👉 Use the tor-expert-bundle-windows-x86_64-XX.X.X version.

* Extract the archive and go to the `tor` folder (where tor.exe is located).

* If it doesn’t exist, create a file named `torrc` in the same folder.

* Example `torrc` contents:
```
SocksPort 9050
ControlPort 9051
CookieAuthentication 1
```
-------------
## ▶️ How to Run
* First, start tor.exe:
```
tor.exe -f torrc
```
Wait until you see:
```
Bootstrapped 100% (done)
```
* Then run your Python script:
```
python hide IP.py
```
---
## 🌐 Use Tor in Firefox (optional)
To route all browser traffic through Tor:
* Open Firefox → Settings → Network Settings → Manual proxy configuration
* Set the following:
  * SOCKS Host: 127.0.0.1
  * Port: 9050
  * Type: SOCKS5
* Enable “Proxy DNS through SOCKS5” in Firefox:
* Open a new tab in Firefox.
  * Go to the following address:
  * ```
    about:config
    ```
  * Accept the risk and continue when prompted.
  * In the search bar, type:
  * ```
    network.proxy.socks_remote_dns
    ```
  * Make sure the value is set to true.
    * If it's false, double-click the entry to change it to true.
## ✅ Test Your IP
Go to:
```
https://dnsleaktest.com
```
→ You should see a Tor IP, not your real one.
## ⚠️ Notes
* Make sure Tor is running before starting the Python script.
* If the script fails to connect, check:
  * Is Tor running?
  * Is port 9050 open?
  * Is your firewall blocking it?
