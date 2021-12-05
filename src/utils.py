import ipaddress


def save_to_file(path: str, content: str):
    with open(path, "w") as fp:
        fp.write(content)


def convert_to_ip_network(ip: str):
    try:
        return ipaddress.ip_network(ip)
    except:
        return None
