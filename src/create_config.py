import ipaddress
from collections import Iterable

import utils


def openvpn(ips: Iterable[ipaddress.IPv4Network]):
    config = "".join(f"route {ip.network_address} {ip.netmask} net_gateway\n" for ip in ips)
    utils.save_to_file('output/openvpn.ovpn', config)
