import tkinter as tk
from tkinter import ttk 

class iug(tk.Frame):
    def __init__(self, window):
        super().__init__(window)
        window.title('Lab 2')
        window.geometry('600x690')
        # window.resizable(False, False)
        s = ttk.Style()
        s.configure('TNotebook.Tab', font = ('Arial', '11', 'italic'))

        self.nb = ttk.Notebook(window)
        self.layer1 = tk.Frame(self.nb)
        self.layer2 = tk.Frame(self.nb)
        self.layer3 = tk.Frame(self.nb)
        
        self.nb.add(self.layer1, text = 'Info')
        self.nb.add(self.layer2, text = 'Ping/Tracert')
        self.nb.add(self.layer3, text = 'Info about IP')
        self.nb.enable_traversal()

        self.nb.grid()

        # Первая вкладка: инфа про ip, сетевую карту, mac адрес, кнопка для смены ip

        self.ipconfig = tk.Button(self.layer1, text = 'Получить IPv4', font = 'Arial 13', width = 18)
        self.newipconfig = tk.Button(self.layer1, text = 'Изменить IP адрес', font = 'Arial 13', width = 18)
        self.ip = tk.Label(self.layer1, text = 'IP адрес:', font = 'Arial 13')
        self.ipInfo = tk.Label(self.layer1, text = '', font = 'Arial 13')
        self.mac = tk.Label(self.layer1, text = 'MAC адрес:', font = 'Arial 13')
        self.macInfo = tk.Label(self.layer1, text = '', font = 'Arial 13')
        self.netcard = tk.Label(self.layer1, text = 'Информация о сетевой плате:', font = 'Arial 13')
        self.netcardInfo = tk.Label(self.layer1, text = '', font = 'Arial 13')

        self.ipconfig.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.ipInfo.grid(row = 1, column = 1, padx = 5, pady = 5)
        self.newipconfig.grid(row = 0, column = 1, sticky = 'nsew', padx = 10, pady = 5)
        self.ip.grid(row = 1, column = 0, sticky = 'nsew', padx = 10, pady = 5)
        self.mac.grid(row = 2, column = 0, sticky = 'nsew', padx = 10, pady = 5)
        self.macInfo.grid(row = 2, column = 1, sticky = 'nsew', padx = 10, pady = 5)
        self.netcard.grid(row = 3, column = 0, sticky = 'nsew', padx = 10, pady = 5)
        self.netcardInfo.grid(row = 3, column = 1, sticky = 'nsew', padx = 10, pady = 5)

        # Вторая вкладка, поля для ввода сайта\ip, поля для трассировки и пинга

        self.l1 = tk.Frame(self.layer2)
        self.l2 = tk.Frame(self.layer2)
        self.l3 = tk.Frame(self.layer2)

        self.pt = tk.Label(self.l1, text = 'Введите ip или название сайта', font = 'Arial 14')
        self.ptEntry = tk.Entry(self.l1, font = 'Arial 14', width = 15)
        self.ping = tk.Button(self.l2, text = 'Ping', font = 'Arial 13')
        self.tracert = tk.Button(self.l2, text = 'Tracert', font = 'Arial 13')
        self.pingInfo = tk.Text(self.l3, width = 25, height = 35)
        self.tracertInfo = tk.Text(self.l3, width = 25, height = 35)
        self.scPing = tk.Scrollbar(self.l3, command = self.pingInfo.yview)
        self.scTracert = tk.Scrollbar(self.l3, command = self.tracertInfo.yview)
        self.emptylbl = tk.Label(self.l3, text = ' ', font = 'Arial 16')
        self.emptylb2 = tk.Label(self.l3, text = ' ', font = 'Arial 16')

        self.l1.pack()
        self.l2.pack()
        self.l3.pack()

        self.pt.pack(side = tk.LEFT)
        self.ptEntry.pack(side = tk.LEFT)
        self.ping.pack(side = tk.LEFT, padx = 100)
        self.tracert.pack(side = tk.LEFT, padx = 100)
        self.emptylb2.pack(side = tk.LEFT, fill = 'y')
        self.pingInfo.pack(side = tk.LEFT)
        self.scPing.pack(side = tk.LEFT, fill = 'y')
        self.emptylbl.pack(side = tk.LEFT, fill = 'y', padx = 35)
        self.tracertInfo.pack(side = tk.LEFT)
        self.scTracert.pack(side = tk.LEFT, fill = 'y')

        # третья вкладка для проверки сайта

        self.website = tk.Label(self.layer3, font = 'Arial 14', text = 'Введите ip адрес сайта')
        self.websiteEnt = tk.Entry(self.layer3, font = 'Arial 14', width = 18)
        self.getInfo = tk.Button(self.layer3, font = 'Arial 14', text = 'Получить информацию')
        self.siteInfo = tk.Text(self.layer3, width = 60, height = 35)

        self.website.grid(row = 0, column = 0, pady = 5)
        self.websiteEnt.grid(row = 0, column = 1, pady = 5)
        self.getInfo.grid(row = 1, column = 0, columnspan = 2, pady = 5)
        self.siteInfo.grid(row = 2, column = 0, columnspan = 2, pady = 5, padx = 10)

        self.nb.select(self.layer1)




if __name__ == "__main__":
    window = tk.Tk()
    g = iug(window)
    g.mainloop()

