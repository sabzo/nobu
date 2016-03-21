## Raspberry Pi as an AccessPoint (AP) and Server
**Nobu** is a minimum library to use the Raspberry Pi as an AccessPoint and a Web Server. It's important to note that depending on the Wireless Network card you maybe using (Realtek for example) the appropriate `hostapd` will need to be downloaded. For example the Raspbian hostapd doesn't work
on some Realtek chips (Realtek-RTL8188 for ex), as a result I've used the driver from Realtek.

# EXAMPLE
```python
  import nobu
  n = nobu.Nobu("ssid", "passwd_must_>_8_chars")
```

There are three components to create a Linux Accesspoint: hostapd (host access point daemon), interfaces configuration, dhcpd (dynamic host configuration protocol)

# HOSTAPD
The hostapd mainly broadcasts the RPi as an Access Point. in its configuration file is where you set up the connection details (SSID/Password etc.,)
Bear in mind that this process and guide uses a Realtek WiFi chip, which REQUIRES its own Driver. So the hostapd that comes default with Raspbian WILL NOT WORK!
I've included the correct default hostapd but it can be found online as well.
Reference: https://jenssegers.com/43/Realtek-RTL8188-based-access-point-on-Raspberry-Pi
`sudo service hostapd start`
`sudo hostapd /etc/hostapd/hostapd.conf `

# Interfaces (/etc/network/interfaces)
This is where all the networking interfaces configuration go: ethernet (eth01), wireless (wlan0 for ex)
This is where you set up the static IP Address for the RPi which other devices will use when the send data to the Pi using sockets
`sudo ifconfig wlan0 192.168.42.1`
`sudo ifdown wlan0`
`sudo ifup wlan0`

# dhcpd
Since the Pi is acting as a server it needs to communicate with the clients connected. To do so it needs to assign each client an IP address. Dynamic Host Configuration Protocol allows `hosts` that connect to be dynanimically configured for communication with the server (by receiving IP addresses).
Neeed to also edit `/etc/default/isc-dhcp-server` and set INTERFACES="wlan0" letting know the dhcp server will assign IP addresses to clients connecting on to the access point.
`sudo dhcpd -cf /etc/dhcp/dhcpd.conf`
`sudo service isc-dhcp-server status`

# References
For more advanced setup like having the Pi connect with ethernet for an AP that can forward requests check out Adafruit
Monitor the logs as the AP connection/handshake takes place: `tail -f /var/log/syslog`

## License

    Copyright [2016] [Sabelo Mhlambi]

    Licensed under the MIT License.
    You may obtain a copy of the License at

        https://opensource.org/licenses/MIT

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
