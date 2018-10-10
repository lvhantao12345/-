import socket
import time
import threading


class DnsResolved:

    def __init__(self):
        self.dict_config = {}
        self.dict_resolved = {}
        self.domain_list = []
        self.ip_list_config = []
        self.ip_list_resolved = []
        self.ip_list_resolved_failed = []
        self.command = ""

    def get_domain_config(self):
        config_file = "E:\python\config.txt"
        with open(config_file) as config:
            for line in config.readlines():
                line = line.rstrip()
                self.domain_list.append(line.split(":")[0])
        config.close()
        return

    def get_address_config(self):
        config_file = "E:\python\config.txt"
        with open(config_file) as address:
            ip_list_config_temp = []
            for line in address.readlines():
                line = line.rstrip()
                ip_list_config_temp.append(line.split(":")[1])
            for line in ip_list_config_temp:
                line = line.split(",")
                line.sort()
                self.ip_list_config.append(line)
        address.close()
        return

    def write_dict_config(self):
        for index in range(len(self.domain_list)):
            self.dict_config[self.domain_list[index]] = self.ip_list_config[index]
        return

    def get_address_resolved(self):
        for domain in self.domain_list:
            try:
                ip = socket.gethostbyname_ex(domain)
                ip=ip[2]
                ip.sort()
                self.ip_list_resolved.append(ip)
            except:
                self.ip_list_resolved.append("0.0.0.0")
                print("域名:"+str(domain)+"解析失败...")
                self.ip_list_resolved_failed.append(domain)
        return

    def write_dict_resolved(self):
        for index in range(len(self.domain_list)):
            self.dict_resolved[self.domain_list[index]] = self.ip_list_resolved[index]
        return

    def check(self):
        file_log="E:\python\log.txt"
        with open(file_log,'a') as log:
            log.write((str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))) + '\n')
            for index in self.domain_list:
                print("解析前"+index+str(self.dict_config[str(index)]))
                print("解析后"+index+str(self.dict_resolved[str(index)]))
                if self.dict_config[str(index)] == self.dict_resolved[str(index)]:
                    log.write("域名"+str(index)+"检查通过...\n")
                elif str(self.dict_config[str(index)]) in str(self.dict_resolved[str(index)]):
                    log.write("域名" + str(index) + "检查通过...\n")
                else:
                    log.write("域名" + str(index) + "检查不通过，新地址为"+str(self.dict_resolved[str(index)])+"\n")
            log.write("--------------------------------------------------------------------------\n")
            log.write("如下域名无法解析：\n"+str(self.ip_list_resolved_failed)+"\n--------------------------------------------------------------------------\n\n")
        log.close()
        return

    def init(self):
        self.ip_list_resolved.clear()
        self.ip_list_resolved_failed.clear()
        return

    def main(self):
        self.get_domain_config()
        self.get_address_config()
        self.write_dict_config()
        print("程序已开始运行...")
        while instance1.command != "exit":
            self.init()
            self.get_address_resolved()
            self.write_dict_resolved()
            self.check()
            time.sleep(int(instance1.interval))
        print("程序已经结束!")


class MyThread:

    def __init__(self):
        self.command = ""
        self.interval = 5
        return

    def time_interval_input(self):
        self.interval = input("请输入检查间隔，默认为5秒...\n")

    def command_input(self):
        while self.command != "exit":
            self.command = input("请输入exit退出！\n")

    def main(self):
        t_command = threading.Thread(target=self.command_input)
        t_main = threading.Thread(target=instance0.main)
        t_time_interval = threading.Thread(target=self.time_interval_input)
        t_time_interval.start()
        t_time_interval.join()
        t_command.start()
        t_main.start()


instance0 = DnsResolved()
instance1 = MyThread()
instance1.main()
