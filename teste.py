import socket
from tkinter import *
class application():
	def __init__(self, master=None):
		self.master= master
		self.master.geometry('360x220')
		self.botao1 = Button(master, text='Batatã',command=self.socket)
		self.botao1.grid(row = 1, column = 1)
	def socket(self, master = None):
		self.ip = Entry(master)
		self.ip.grid(row=2,column=2)
		self.botaoadd = Button(master, text='Get',command =self.ipget)
		self.botaoadd.grid(row=1,column=2)
		self.meu_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	def ipget(self, master=None):
		self.ipf = (self.ip.get())
		for x in range(3):
			self.nigga = Label(master, text = x)
			self.nigga.grid(row =  x, column = 3)
			if self.meu_socket.connect_ex((self.ipf,x)):
				label=Label(master,text="\nPorta fechada")
				label.grid(row = x, column = 3)
			else:
				label1=Label(master,text="\nPorta aberta")
				label1.grid(row = x, column = 3)

root = Tk()
application(root)
root.mainloop()
