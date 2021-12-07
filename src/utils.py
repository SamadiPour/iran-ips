import ipaddress


def save_to_file(path: str, content: str):
    with open(path, "w") as fp:
        fp.write(content)


def convert_to_ip_network(ip: str):
    try:
        return ipaddress.ip_network(ip)
    except:
        return None


# -- Old method to remove subnets --
# -- I will remove it when I'm sure from the new method --
# def remove_subnet_ips(ip_list: list[ipaddress.IPv4Network]):
#     subset_indexes = set()
#
#     for i in range(0, len(ip_list)):
#         for j in range(i + 1, len(ip_list)):
#             x = ip_list[i]
#             y = ip_list[j]
#
#             if x.subnet_of(y):
#                 subset_indexes.add(i)
#                 continue
#             elif y.subnet_of(x):
#                 subset_indexes.add(j)
#
#     for i in sorted(subset_indexes, reverse=True):
#         del ip_list[i]


def remove_subnet_ips(ip_list: list[ipaddress.IPv4Network]):
    i = -1
    while True:
        # iterate over the list to compare ip[i] with others
        # then and one to i and iterate over till the end
        list_len = len(ip_list)
        i += 1

        # if i is out of range, then break
        if i >= list_len:
            break

        # make an empty list of subset_indexes and iterate over the list
        subset_indexes = set()
        for j in range(i + 1, list_len):
            x = ip_list[i]
            y = ip_list[j]

            # compare x and y to find subnet and add it to subset_indexes
            if x.subnet_of(y):
                subset_indexes.add(i)
                continue
            elif y.subnet_of(x):
                subset_indexes.add(j)

        # go back for one if [i] is going to be deleted
        if i in subset_indexes:
            i -= 1

        # remove the subset_indexes from the list
        for x in sorted(subset_indexes, reverse=True):
            del ip_list[x]


def get_private_ip_networks():
    return [
        ipaddress.ip_network("0.0.0.0/8"),
        ipaddress.ip_network("10.0.0.0/8"),
        ipaddress.ip_network("100.64.0.0/10"),
        ipaddress.ip_network("127.0.0.0/8"),
        ipaddress.ip_network("169.254.0.0/16"),
        ipaddress.ip_network("172.16.0.0/12"),
        ipaddress.ip_network("192.0.0.0/24"),
        ipaddress.ip_network("192.0.2.0/24"),
        ipaddress.ip_network("192.88.99.0/24"),
        ipaddress.ip_network("192.168.0.0/16"),
        ipaddress.ip_network("198.18.0.0/15"),
        ipaddress.ip_network("198.51.100.0/24"),
        ipaddress.ip_network("203.0.113.0/24"),
        ipaddress.ip_network("224.0.0.0/3"),
    ]


def get_private_ip_networks_str():
    return map(str, get_private_ip_networks())
