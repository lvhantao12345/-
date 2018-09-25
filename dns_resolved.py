import socket
import time


def __init__():
    print("程序已开始运行...")
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
    global ip_list_resolved_failed
    ip_list_resolved_failed = []


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
        for line in ip_list_config_temp:
            line = line.split(",")
            line.sort()
            ip_list_config.append(line)
    return
    address.close()


def write_dict_config():
    for index in range(len(domain_list)):
        dict_config[domain_list[index]] = ip_list_config[index]
    return


def get_address_resolved():
    for domain in domain_list:
        try:
            ip = socket.gethostbyname_ex(domain)
            ip=ip[2]
            ip.sort()
            ip_list_resolved.append(ip)
        except:
            ip_list_resolved.append("0.0.0.0")
            print("域名:"+str(domain)+"解析失败...")
            ip_list_resolved_failed.append(domain)
    return


def write_dict_resolved():
    for index in range(len(domain_list)):
        dict_resolved[domain_list[index]] = ip_list_resolved[index]
    return


def check():
    file_log="E:\python\log.txt"
    with open(file_log,'a') as log:
        log.write((str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))) + '\n')
        for index in domain_list:
            if dict_config[str(index)] == dict_resolved[str(index)]:
                log.write("域名"+str(index)+"检查通过...\n")
            else:
                log.write("域名" + str(index) + "检查不通过，新地址为"+str(dict_resolved[str(index)])+"\n")
        log.write("------------------------------------------------------------------------------------------\n")
        log.write("如下域名无法解析：\n"+str(ip_list_resolved_failed)+"\n------------------------------------------------------------------------------------------\n\n")

    return


def init():
    ip_list_resolved.clear()
    ip_list_resolved_failed.clear()
    return


def main():
    __init__()
    get_domain_config()
    get_address_config()
    write_dict_config()
    while True:
        init()
        get_address_resolved()
        write_dict_resolved()
        check()
        time.sleep(5)


main()
