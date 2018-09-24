import socket
import time


def __init__():
    global dict_config
    dict_config = {}
    global dict_resolved
    dict_resolved = {}
    global domain_list
    domain_list = []
    global ip_list_config
    ip_list_config = []
    global ip_list_resolved
    ip_list_resolved = []


def get_domain_config():
    config_file = "E:\python\config.txt"
    with open(config_file) as config:
        for line in config.readlines():
            line = line.rstrip()
            domain_list.append(line.split(":")[0])
    return
    config.close()


def get_address_config():
    config_file = "E:\python\config.txt"
    with open(config_file) as address:
        ip_list_config_temp = []
        for line in address.readlines():
            line = line.rstrip()
            ip_list_config_temp.append(line.split(":")[1])
        print(ip_list_config_temp)
        for line in ip_list_config_temp:
            ip_list_config.append(line.split(","))
        print(ip_list_config)
    return
    address.close()


def write_dict_config():
    for index in range(len(domain_list)):
        dict_config[domain_list[index]] = ip_list_config[index]
    print(dict_config)
    return


def get_address_resolved():
    for domain in domain_list:
        ip = socket.gethostbyname_ex(domain)
        ip_list_resolved.append(ip[2])
    return


def write_dict_resolved():
    for index in range(len(domain_list)):
        dict_resolved[domain_list[index]] = ip_list_resolved[index]
    print(dict_resolved)
    return


def check():
    for index in domain_list:
        if dict_config[str(index)] == dict_resolved[str(index)]:
            print(1)
        else:
            print(0)
    return


def main():
    __init__()
    get_domain_config()
    get_address_config()
    write_dict_config()
    get_address_resolved()
    write_dict_resolved()
    while True:
        check()
        time.sleep(5)


main()
