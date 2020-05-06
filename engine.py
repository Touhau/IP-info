import tkinter as tk
from gui import iug
import re
import os
import subprocess
import winreg


class engine(iug):
    def __init__(self, window):
        super().__init__(window)
        self.ipconfig.config(command = lambda *args: self.IPFunk())
        self.registryPath.delete(0, tk.END)
        self.registryPath.insert(0, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\NetworkCards\\2')
        


    def IPFunk(self):
    # Вытаскиваем IP
        ip = subprocess.check_output('ipconfig')
        ip = ip.decode('cp866')
        b = open('temp.txt', 'w')
        b.write(ip)
        b.close()
        d = open('temp.txt', 'r')
        for line in d:
            t = re.findall('IPv4', line)
            if len(t)!=0:
                t1 = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line)
                break

        d.close()
        os.remove('temp.txt', dir_fd = None)

    # Вытаскиваем мак
        mac = subprocess.check_output('getmac /v')
        mac = mac.decode('cp866')
        b1 = open('temp.txt', 'w')
        b1.write(mac)
        b1.close()
        d1 = open('temp.txt', 'r')
        for line in d1:
            t2_1 = re.findall('Ethernet', line)
            t2_2 = re.findall('Беспроводная', line)
            if len(t2_1)!=0 or len(t2_2)!=0:
                t3 = re.findall(r'\w{2}\-\w{2}\-\w{2}\-\w{2}\-\w{2}\-\w{2}', line)  
        d1.close()
        os.remove('temp.txt', dir_fd = None)

    #  Вытаскиваем инфу из регистра, по дефотлу папка должна быть 2
        try:
            path = self.registryPath.get()
            hkey = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            result = winreg.QueryValueEx(hkey, 'Description')
            self.netcardInfo.config(text = result[0])
        except BaseException:
            self.netcardInfo.config(text = 'Неправильный путь')

        self.macInfo.config(text = t3[0])
        self.ipInfo.config(text = t1[0])





if __name__ == "__main__":
    window = tk.Tk()
    a = engine(window)
    a.mainloop()