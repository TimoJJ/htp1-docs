# Troubleshooting

## Safari Browser

Loading the Web GUI in Safari can fail. Workarounds:

- Turn off content blockers (Safari > Settings > Websites > Content Blockers > Off) and iCloud
  Private Relay (System Settings > iCloud > Private Relay > Off), then reload the Web GUI.
- Try the local hostname shown on the front panel's **Help** screen instead of the numeric IP address.
  Enter the address with `http://`, for example `http://htp-1.local`.

!!! note "Local hostname availability"
    The HTP-1 advertises its local hostname using mDNS. Your browser must support mDNS, and the network
    must allow the required local multicast traffic. Router DNS support is not required. If the
    hostname does not resolve, use the IP address shown on the front panel's Help screen.
