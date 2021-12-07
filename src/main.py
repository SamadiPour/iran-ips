import ipaddress
import os
from functools import reduce

import create_config
import utils
from get_ips import *


def collect_and_clean(*list_of_ips: Iterable[Iterable[str]]) -> Iterable[ipaddress.IPv4Network]:
    ip_set = reduce(lambda x, y: set(x).union(set(y)), list_of_ips)
    ip_set = map(utils.convert_to_ip_network, ip_set)
    ip_set = filter(lambda x: x is not None, ip_set)
    ip_set = list(ip_set)

    utils.remove_subnet_ips(ip_set)

    return sorted(ip_set)


if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")

    ips = collect_and_clean(ito_gov(), geo_lite2(), ip2location())
    ips_str = map(str, ips)

    utils.save_to_file('output/iran_ips.txt', "\n".join(ips_str))
    create_config.openvpn(ips)
