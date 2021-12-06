import os
from functools import reduce

import utils
from get_ips import *


def collect_and_clean(*list_of_ips: Iterable[Iterable[str]]) -> Iterable[str]:
    ip_set = reduce(lambda x, y: set(x).union(set(y)), list_of_ips)
    ip_set = map(utils.convert_to_ip_network, ip_set)
    ip_set = filter(lambda x: x is not None, ip_set)
    ip_set = list(ip_set)

    subset_indexes = set()

    for i in range(0, len(ip_set)):
        for j in range(i + 1, len(ip_set)):
            x = ip_set[i]
            y = ip_set[j]

            if x.subnet_of(y):
                subset_indexes.add(i)
                continue
            elif y.subnet_of(x):
                subset_indexes.add(j)

    for i in sorted(subset_indexes, reverse=True):
        del ip_set[i]

    return map(str, sorted(ip_set))


if __name__ == '__main__':
    if not os.path.exists("output"):
        os.mkdir("output")

    ips = collect_and_clean(ito_gov(), geo_lite2(), ip2location())

    utils.save_to_file('output/iran_ips.txt', "\n".join(ips))
