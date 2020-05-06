import tkinter as tk
from gui import iug
import re
import os
import subprocess
import winreg
from tkinter import messagebox as mb


class engine(iug):
    def __init__(self, window):
        super().__init__(window)
        self.ipconfig.config(command = lambda *args: self.IPFunk())
        self.registryPath.delete(0, tk.END)
        self.registryPath.insert(0, 'Software\\Microsoft\\Windows NT\\CurrentVersion\\NetworkCards\\2')
        self.newipconfig.config(command = lambda *args: self.changeIP())
        


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

    def changeIP(self):
        connectType = self.CoT()
        if self.newipconfig['text'] == 'Изменить IP адрес':
            if len(self.newIp.get())>=7:
                if connectType == 'eth':
                    changeCommand = 'netsh interface ip set address name = "Ethernet" static {} 255.255.255.0 192.168.1.1'.format(self.newIp.get())
                    b = open('change.txt', 'w') 
                    b.write(changeCommand)
                    b.close()
                    os.rename('change.txt', 'change.bat')
                    os.startfile('change.bat', 'runas')
                    mb.showinfo(title = 'Успешно', message = 'IP изменён')                     
                    self.newipconfig.config(text = 'Вернуть прежний IP') 
                    os.remove('change.bat', dir_fd = None)     
                elif connectType == 'wir':
                    changeCommand = 'netsh interface ip set address name = "Беспроводная сеть" static {} 255.255.255.0 192.168.1.1'.format(self.newIp.get())
                    b = open('change.txt', 'w') 
                    b.write(changeCommand)
                    b.close()
                    os.rename('change.txt', 'change.bat')
                    os.startfile('change.bat', 'runas')
                    mb.showinfo(title = 'Успешно', message = 'IP изменён')
                    self.newipconfig.config(text = 'Вернуть прежний IP') 
                    os.remove('change.bat', dir_fd = None)
        else:
            if connectType == 'eth':
                changeCommand = 'netsh interface ip set address "Ethernet" dhcp'
                b = open('ret.txt', 'w') 
                b.write(changeCommand)
                b.close()
                os.rename('ret.txt', 'ret.bat')
                os.startfile('ret.bat', 'runas')
                self.newipconfig.config(text = 'Изменить IP адрес')    
                os.remove('ret.bat', dir_fd = None)
            elif connectType == 'wir':
                changeCommand = 'netsh interface ip set address "Беспроводная сеть" dhcp'
                b = open('ret.txt', 'w') 
                b.write(changeCommand)
                b.close()
                os.rename('ret.txt', 'ret.bat')
                os.startfile('ret.bat', 'runas')
                self.newipconfig.config(text = 'Изменить IP адрес')
                os.remove('ret.bat', dir_fd = None) 
        
    def CoT(self):
        connect = subprocess.check_output('netsh interface ip show interface')
        connect = connect.decode('cp866')
        b = open('temp.txt', 'w')
        b.write(connect)
        b.close()
        d = open('temp.txt', 'r')
        for line in d:
            t1 = re.findall('Ethernet', line)
            t2 = re.findall('Беспроводная', line)
            if len(t1) != 0:
                return 'eth'
            elif len(t2) != 0:
                return 'wir'
        d.close()
        os.remove('temp.txt', dir_fd = None)

if __name__ == "__main__":
    window = tk.Tk()
    a = engine(window)
    a.mainloop()