# Desenvolvido por Adriel Freud!
# Contato: businessc0rp2k17@gmail.com 
# FB: http://www.facebook.com/xrn401
#   =>DebutySecTeamSecurity<=
#conding: utf-8

#!/bin/usr/python
import requests, base64, tempfile, sys, json, os, random, string, webbrowser, subprocess, getpass, hashlib, tkMessageBox
from bs4 import BeautifulSoup
from tkFileDialog import askopenfilename
from Tkinter import *
from time import sleep
from ctypes import *

#os.system('color a')
os.system('title Central - Adriel Freud')

menu = """\n\n
-----------------------------------------
  #  Desenvolvido por Adriel Freud!
  #  Contato: businessc0rp2k17@gmail.com 
  #  FB: http://www.facebook.com/xrn401
  #   =>DebutySecTeamSecurity<=
-----------------------------------------
\n"""

delimiter = "|"
print(menu)
temporario = tempfile.gettempdir()
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
(LEN_NBI, LEN_NIF, LEN_NISS, LEN_NIB, LEN_ISBN) = (9, 9, 11, 21, 10)
(MINLEN_CC, MAXLEN_CC) = (7, 19)

def callback(event):
    	webbrowser.open_new(r"https://www.facebook.com/xrn401")

def callback1(event):
    	webbrowser.open_new(r"https://github.com/AdrielFreud")

def callback2(event):
    	webbrowser.open_new(r"https://www.youtube.com/AdrielFreud")

def _toIntList(numstr, acceptX=0):
    res = []
    for i in numstr:
        if i in string.digits:
            res.append(int(i))
    if acceptX and (numstr[-1] in 'Xx'):
        res.append(10)
    return res

def luhn(ncc):
    ncc = _toIntList(ncc)
    ncc.reverse()
    if MINLEN_CC > len(ncc) or len(ncc) > MAXLEN_CC:
        return False
    sum = 0
    alt = False
    for i in ncc:
        if alt:
            i *= 2
            if i > 9:
                i -= 9
        sum += i
        alt = not alt
    return not (sum % 10)

def gerarccv(num):
  return random.randrange(num)

def gerar_ano(num):
  return random.randrange(1, num)

def gerar_cvc(num):
	return random.randrange(1,10)

def callmenu():
	try:
		gerador_de_cc.destroy()
	except:
		pass
	try:
		binnn.destroy()
	except:
		pass
	try:
		window.destroy()
	except:
		pass
	main() 

def gerando_cc():
	entry_info = Label(gerador_de_cc, text="Gerado Arquivo com CC'S!", fg="black", bg="white")
	entry_info.place(x=83, y=120)
	LUHN = 0
	NOT_LUHN = 0
	a = open("CCvs.txt", 'w')
	bin_ = entry_bincc.get()
	for i in range(int(len_credits.get())):
		ccv_sem_bin = "%s%s%s%s%s%s%s%s%s%s"%(gerarccv(10),gerarccv(10),gerarccv(10),gerarccv(10),gerarccv(10),gerarccv(10),gerarccv(10),gerarccv(10), gerar_cvc(10), gerar_cvc(10))
		mes = "%s%s" %(0, gerar_ano(10))
		ano = "%s%s%s%s"%(2, 0, gerar_ano(4), gerar_ano(10))
		cvc = "%s%s%s" %(gerar_cvc(2), gerar_cvc(10), gerar_cvc(10))
		ccv_inteira = "%s%s%s%s%s%s%s%s"% (bin_, ccv_sem_bin, delimiter,mes,delimiter,ano,delimiter,cvc)
		if luhn(ccv_sem_bin) == True:
		    #a.write(ccv_inteira+'\n')
		    LUHN += 1
		else:
		  	a.write(ccv_inteira+'\n')
			NOT_LUHN += 1
	tkMessageBox.showinfo("Info", "[WARNING] - Total [TRUE] Luhn Algoritm: %i | Total Failed: %i"%(NOT_LUHN, LUHN))
	a.close()

def Gerador_CC():
	menu.destroy()
	global gerador_de_cc
	gerador_de_cc = Tk()
	gerador_de_cc.title('Gerador de CC')
	gerador_de_cc['bg'] = 'black'
	gerador_de_cc.geometry("300x200+200+200")
	#########################
	info = Label(gerador_de_cc, text=" - obs; Insira sua BIN abaixo!", font="Arial 10").pack(side=TOP)
	bincc = Label(gerador_de_cc, text="BIN:", fg="white", bg="black").place(x=34, y=90) 
	#########################
	global entry_bincc
	entry_bincc = Entry(gerador_de_cc)
	entry_bincc.place(x=90, y=90)
	#########################
	funcMenu = Button(gerador_de_cc, text="MENU", command=callmenu, bg='#4F4F4F', fg='white').place(x=30, y=150)
	button_cc = Button(gerador_de_cc, text="Gerar!", bg='#4F4F4F', fg='white', width=20, command=gerando_cc).place(x=80, y=150)
	#########################
	global len_credits
	len_credits = Entry(gerador_de_cc, width=5)
	len_credits.place(x=240, y=90)

	gerador_de_cc.mainloop()

def binchecker():
	def openccs():
		hizi = Tk()
		hizi.withdraw()
		filename = askopenfilename(parent=hizi)
		f = open(filename, 'r')
		for lines in f.readlines():
			url = 'https://www.ke1.nl/en/checker/api.php'
			r = requests.post(url, headers=header, data={'data':lines})
			bs = BeautifulSoup(r.content, 'lxml')
			data = ""
			if 'Live' in r.content:
				for a in bs.find_all('div'):
					data += a.get_text()

			a = open('APROVADAAAS!!.txt', 'a')
			a.write(data)
			a.close()
		f.close()

def check():
		os.system('cls')
		biin = entrybin.get()

		if len(biin) >= 16:
			url = 'https://www.ke1.nl/en/checker/api.php'
			r = requests.post(url, headers=header, data={'data':entrybin.get()})
			bs = BeautifulSoup(r.content, 'lxml')
			for a in bs.find_all('div'):
				tkMessageBox.showinfo("Info", a.get_text())

		else:
			url = "https://lookup.binlist.net/{0}".format(biin)
			req = requests.get(url, headers=header)
			code = req.status_code
			html = req.text
			data = ""
			if code == 200:
				jsbin = json.loads(html)
				try:
					data += "\nNumber: \n"
					data += "Lenght: %s"%jsbin['number']['length']
					data += "Prefix: %s"%jsbin['number']['prefix']
					data += "Type: %s"%jsbin['type']
					data += "Brand: %s"%jsbin['brand']
					data += "Prepaid: %s"%jsbin['prepaid']
					data += "Bank Name: %s"%jsbin['bank']['name']
					data += "Bank Logo: %s"%jsbin['bank']['logo']
					data += "Bank City: %s"%jsbin['bank']['city']
					data += "Bank Phone: %s"%jsbin['bank']['phone']
					data += "Contry alpha: %s"%jsbin['country']['alpha2']
					data += "Contry Name: %s"%jsbin['country']['name']
					data += "Contry Numeric: %s"%jsbin['country']['numeric']
					tkMessageBox.showinfo("Info", data)
				except:
					pass
			else:
				tkMessageBox.showwarning("Warn", "[!] Error ao requisitar!")

	menu.destroy()
	global binnn
	binnn = Tk()
	binnn.title('Bin Checker')
	tkMessageBox.showinfo("Info", " - obs; Pode Inserir CCV inteira junto a CVC e MES/DATA@ - Delimiter: | ")
	binnn['bg'] = 'black'
	#################################
	Abrircc = Button(binnn, text="Abrir txt com Varias CC'S!", bg='#4F4F4F', fg='white', command=openccs).place(x=30, y=60)
	#################################
	labelbin = Label(binnn, text="Insira a Bin ou um Cartao Valido!", bg='black', fg='white').place(x=30, y=100)
	#################################
	entrybin = Entry(binnn, width=20)
	entrybin.place(x=75, y=130)
	#################################
	checkbt = Button(binnn, width=20, text="Checkar!", command=check, bg='#4F4F4F', fg='white').place(x=75, y=160)
	#################################
	exitbin = Button(binnn, width=20, text="Sair!", command=sair, bg='#4F4F4F', fg='white').place(x=75, y=190)
	#################################
	funcMenu = Button(binnn, text="MENU", command=callmenu, bg='#4F4F4F', fg='white').place(x=75, y=220)
	#################################
	binnn.geometry("300x300+200+200")
	binnn.mainloop()

def CleanTemp():
	root = Tk()
	root.title("-:[ Limpador by Adriel ]:-")

	root['bg'] = 'black'
	root.geometry("300x500+200+200")

	menubar = Menu(root)
	root.config(menu=menubar)
	filemenu = Menu(menubar)
	menubar.add_cascade(label='Menu', menu=filemenu)
	if windll.shell32.IsUserAnAdmin() == 0:
		tkMessageBox.showwarning("Warning", "Execute como administrador para uma limpeza Profunda!")
	else:
		pass

	def Creditos():
		tkMessageBox.showinfo("Creditos", cred)

	filemenu.add_command(label='Creditos', command=Creditos)

	def Open_channel():
		webbrowser.open('https://www.youtube.com/AdrielFreud')

	filemenu.add_command(label='Canal', command=Open_channel)

	def Github():
		webbrowser.open('https://github.com/AdrielFreud')

	filemenu.add_command(label='Github', command=Github)

	def Exit():
		sys.exit()
		exit()

	filemenu.add_command(label='Exit', command=Exit)

	def call_all_functions():
		list_thread = [clear_temp(), clear_prefetch(), clear_SoftwareDistribution(), clean_system(), cleanmgr()]
		for threads in list_thread:
			threading.Thread(target=threads, args=()).start()
		tkMessageBox.showinfo("Information", "Todos os arquivos inuteis foram retirados do seu computador, Obrigado por utilizar nosso programa! Att. AdrielFreud :)")

	def clear_temp():
		try:
			os.chdir('C:\\Windows\\Temp')
			for temp1 in os.listdir('.'):
				if os.path.isdir(temp1) == True:
					os.system('rmdir %s /S /Q'%temp1)
				else:
					os.system('del %s /S /Q /F'%temp1)
			os.chdir('C:\\Temp')
			for temp2 in os.listdir('.'):
				if os.path.isdir(temp2) == True:
					os.system('rmdir %s /S /Q'%temp2)
				else:
					os.system('del %s /S /Q /F'%temp2)
			os.chdir(temporario)
			for temp3 in os.listdir('.'):
				if os.path.isdir(temp3) == True:
					os.system('rmdir %s /S /Q'%temp3)
				else:
					os.system('del %s /S /Q /F'%temp3)
		except:
			pass

	def clear_prefetch():
		try:
			os.chdir('C:\\Windows\\Prefetch')
			for prefetch in os.listdir('.'):
				if os.path.isdir(prefetch) == True:
					os.system('rmdir %s /S /Q'%prefetch)
				else:
					os.system('del %s /S /Q /F'%prefetch)
		except:
			pass

	def clear_SoftwareDistribution():
		try:
			os.chdir('C:\\Windows\\installer')
			for installer in os.listdir('.'):
				if os.path.isdir(installer) == True:
					os.system('rmdir %s /S /Q'%installer)
				else:
					os.system('del %s /S /Q /F'%installer)

			os.chdir('C:\\Windows\\SoftwareDistribution\\Download')
			for Software in os.listdir('.'):
				if os.path.isdir(Software) == True:
					os.system('rmdir %s /S /Q'%Software)
				else:
					os.system('del %s /S /Q /F'%Software)

			os.chdir('C:\\Windows\\Downloaded Program Files')
			for ProgramFiles in os.listdir('.'):
				if os.path.isdir(ProgramFiles) == True:
					os.system('rmdir %s /S /Q'%ProgramFiles)
				else:
					os.system('del %s /S /Q /F'%ProgramFiles)
					
		except:
			pass

	info_sistema = Label(root, text='Limpador de Arquivos Temporarios do Sistema', bg='black', fg='white', font="Arial 10").place(x=12,y=10)
	temp = Button(root, text='Clean TEMP', bg='#4F4F4F', fg='white', width=30, command=clear_temp).place(x=40, y=60)
	prefetch = Button(root, text='Clean PREFETCH', bg='#4F4F4F', fg='white', width=30, command=clear_prefetch).place(x=40, y=100)
	Distribution = Button(root, text='Clean SoftwareDistribution', bg='#4F4F4F', fg='white', width=30, command=clear_SoftwareDistribution).place(x=40, y=140)
	####
	info_clean_all = Label(root, text='> Limpador em Massa de Arquivos <', bg='black', fg='white', font="Arial 10").place(x=40, y=195)
	clean_all = Button(root, text='Clean ALL FILES', bg='#4F4F4F', fg='white', width=30, command=call_all_functions).place(x=40, y=250)

	# - Startup - #

	def Add_Startup():
		tkMessageBox.showinfo('Information', '[!!] Adicionado ao Startup!')
		os.chdir('C:\\ProgramData')
		os.system('mkdir Startup-Cleandir')
		os.chdir('Startup-Cleandir/')
		with open('start.vbs', 'w') as w:
			w.write('Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "start.bat" & Chr(34), 0\nSet WshShell = Nothing')
			w.close()
			with open('clean.bat', 'w') as clean:
				clean.write('''
	@echo off
	cd "C:\\Windows\\SoftwareDistribution\\Download"
	del * /S /Q /F
	rmdir * /S /Q
	cd "C:\\Windows\\Prefetch"
	del * /S /Q /F
	rmdir * /S /Q
	cd "C:\\Windows\\Temp"
	del * /S /Q /F
	rmdir * /S /Q
	cd "C:\\Temp"
	del * /S /Q /F
	rmdir * /S /Q
	cd %temp%
	del * /S /Q /F
	rmdir * /S /Q''')
				clean.close()
				subprocess.Popen('reg add "HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run" /v "CleanDIRS" /d "%ProgramData%\\Startup-Cleandir\\start.vbs" /f', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

	def Remove_Startup():
		tkMessageBox.showinfo('Information', '[!] Removendo Startup!')
		os.chdir('C:\\ProgramData')
		os.system('rmdir Startup-Cleandir /S /Q')
		tkMessageBox.showinfo('[!] Startup Removido!')

	def cleanmgr():
		tkMessageBox.showinfo('Information', "[@@@] Selecione todas as TextBox e Inicie uma Limpeza Profunda!")
		subprocess.Popen('RunDll32.exe inetcpl.cpl, ClearMyTracksByProcess 255', shell=True)
		subprocess.Popen('cleanmgr', shell=True).wait()

	def clean_system():
		subprocess.Popen('ipconfig /flushdns', shell=True)
		os.chdir('%s\\AppData\\Local\\Microsoft\\Windows\\INetCache\\IE'%usr)

		for INetCache in os.listdir('.'):
			if os.path.isdir(INetCache) == True:
				os.system('rmdir %s /S /Q'%INetCache)
			else:
				os.system('del %s /S /Q /F'%INetCache)

		os.chdir('C:\\WINDOWS\\Offline Web Pages')	
		for Offline in os.listdir('.'):
			if os.path.isdir(Offline) == True:
				os.system('rmdir %s /S /Q'%Offline)
			else:
				os.system('del %s /S /Q /F'%Offline)

		os.chdir('C:\\Windows')
		try:
			os.system("del *.log /a /s /q /f")
		except:
			pass


	Startup = Button(root, text='ADD Startup', bg='#4F4F4F', fg='white', width=30, command=Add_Startup).place(x=40, y=290)
	remove_Startup = Button(root, text='REMOVE Startup', bg='#4F4F4F', fg='white', width=30, command=Remove_Startup).place(x=40, y=330)
	Button(root, text='Limpeza de Disco', bg='#4F4F4F', fg='white', width=30, command=cleanmgr).place(x=40, y=370)
	Button(root, text='Limpeza de Cache do Systema', bg='#4F4F4F', fg='white', width=30, command=clean_system).place(x=40, y=410)
	Label(root, text='[ Agradeca ao Adriel Freud <3 ]', fg='white', bg='black', font="Arial 11").place(x=46, y=460)

	root.mainloop()

def main():
	global menu
	menu = Tk()
	menu.title("Menu")
	info = Label(menu, text="- Central feita por Adriel Freud - ", font="Arial 10").pack(side=TOP)
	#################################
	con = Button(menu, text="Consultor", command=Consultar, bg='#4F4F4F', fg='white', width=20).place(x=75, y=60)
	#################################
	bincheck = Button(menu, text="Check Bin && CC", command=binchecker, bg='#4F4F4F', fg='white', width=20).place(x=75, y=100)
	#################################
	clean = Button(menu, text="Limpar Arquivos Temp.", command=CleanTemp, bg='#4F4F4F', fg='white', width=20).place(x=75, y=140)
	#################################
	cc = Button(menu, text="Gerador de CC", command=Gerador_CC, bg='#4F4F4F', fg='white', width=20).place(x=75, y=180)
	#################################
	exitt = Button(menu, text="Sair!", command=sair, bg='#4F4F4F', fg='white', width=20).place(x=75, y=220)
	#################################
	base = Label(menu, text=" ========== Base64 Encode ==========", bg='black', fg='white').place(x=20, y=250)
	#################################
	baseLabel = Label(menu, text="String > ", bg='black', fg='white').place(x=5, y=290)
	#################################
	baseEntry = Entry(menu, width=24)
	baseEntry.place(x=75, y=290)

	def encodarbase64():
		string = baseEntry.get()
		encriptado = base64.b64encode(string)
		gerararq = Label(menu, text="Gerado arquivo: encoded.txt", bg='black', fg='white').place(x=75, y=400)
		with open('encoded.txt', 'w') as w:
			w.write(encriptado+'\n')
			w.close()

	def function():
		baseEntry = Entry(menu, width=24)
		baseEntry.place(x=75, y=250)

	Buttonbase64 = Button(menu, text="Encodar", command=encodarbase64, bg='#4F4F4F', fg='white', width=20).place(x=75, y=330)
	#################################
	Buttonbase64 = Button(menu, text="CleanString", command=function, bg='#4F4F4F', fg='white', width=20).place(x=75, y=365)
	#################################
	menu['bg'] = 'black'
	menu.geometry("300x450+200+200")
	menu.mainloop()

def Consultar():
	def requisitar():
		cpf = edi2.get()
		cnpj = edi1.get()
		nome = edi3.get()

		if nome:
			os.system('cls')
			tkMessageBox.showinfo("Info", "[!] Aguarde cerca de 3 Minutos por Consultas!")
			'''
			count = 181
			for i in range(1, count):
			    sys.stdout.write("\r{} Segundos".format(i))
			    sys.stdout.flush()
			    sleep(1)
			'''
			forms = {'enviarnome':nome.replace(' ','+'),'pesquisar':'Consultar'}
			r = requests.post('', data=forms, headers=header)
			if r.status_code == 200:
				html = r.text
				tkMessageBox.showinfo("Info", html)
			else:
				tkMessageBox.showwarning("Warn", "Error ao Puxar! :(")			

		elif cpf:
			os.system('cls')
			tkMessageBox.showinfo("Info", "[!] Aguarde cerca de 3 Minutos por Consultas!")
			
			count = 181
			for i in range(1, count):
			    sys.stdout.write("\r{} Segundos".format(i))
			    sys.stdout.flush()
			    sleep(1)

			r = requests.post('', data=forms, headers=header)
			if r.status_code == 200:
				html = r.text
				bs = BeautifulSoup(html, 'lxml')
				div = bs.find_all('div')
				for divs in div:
					tkMessageBox.showinfo("Info", divs.get_text()).strip('\n')
			else:
				tkMessageBox.showwarning("Warn","Error ao Puxar! :(")

		elif cnpj:

			os.system('cls')
			url = 'aHR0cHM6Ly93d3cucmVjZWl0YXdzLmNvbS5ici92MS9jbnBqL3swfQ=='
			enc = base64.b64decode(url)
			req = requests.get(enc.format(cnpj), headers=header)
			code = req.status_code
			html = req.text
			data = ""
			if code == 200:
				receita = json.loads(html)
				print(menu)
				try:
					data += "Atividade Principal: %s"%receita['atividade_principal'][0]['text']
					data += "Nome: %s"%receita['nome']
					data += "Complemento: %s"%receita['complemento']
					data += "UF: %s"%receita['uf']
					data += "Telefone: %s"%receita['telefone']
					data += "Email: %s"%receita['email']
					data += "(QSA) Nome: %s"%receita['qsa'][0]['nome']
					data += "(QSA): %s"%receita['qsa']
					data += "Situacao: %s"%receita['situacao']
					data += "Abertura: %s"%receita['abertura']
					data += "Bairro: %s"%receita['bairro']
					data += "Ultima atualizacao: %s"%receita['ultima_atualizacao']
					data += "Numero: %s"%receita['numero']
					data += "CEP: %s"%receita['cep']
					data += "Municipio: %s"%receita['municipio']
					data += "CNPJ: %s"%receita['cnpj']
					data += "Status: %s"%receita['status']
					tkMessageBox.showinfo("Info", data)
				except:
					tkMessageBox.showwarning("Warn", "Error ao Puxar! :(")

		else:
			adriellb = Label(window, text="Insira um CPF ou CNPJ valido!", fg="green", bg="black").pack(side=TOP)

	menu.destroy()
	global window
	window = Tk()

	window.title('= Central by AdrielFreud =')
	#################################
	lb = Label(window, text="Consultor CPF", bg='black', fg='white').place(x=75, y=90)
	#################################
	lb3 = Label(window, text="Consultor Nome", bg='black', fg='white').place(x=75, y=35)
	#################################
	l2 = Label(window, text="Consultor CNPJ", bg='black', fg='white').place(x=75, y=150)
	#################################
	bt1 = Button(window, width=20, text="Consultar", command=requisitar, bg='#4F4F4F', fg='white').place(x=75, y=220)

	#cnpj
	edi1 = Entry(window, width=24)
	edi1.place(x=75, y=180)

	#cpf
	edi2 = Entry(window, width=24)
	edi2.place(x=75, y=120)

	#Nome

	edi3 = Entry(window, width=24)
	edi3.place(x=75, y=65)

	bot2 = Button(window, width=20, text="Sair!", command=sair, bg='#4F4F4F', fg='white').place(x=75, y=250)

	def functionCLEAR():
		os.system('cls')
		edi1 = Entry(window, width=24)
		edi1.place(x=75, y=180)
		edi2 = Entry(window, width=24)
		edi2.place(x=75, y=120)

	adriellb = Label(window, text="==== Creditos Adriel Freud ====", bg='black', fg='white').pack(side=TOP)
	#################################
	funcMenu = Button(window, text="MENU", command=callmenu, bg='#4F4F4F', fg='white').place(x=10, y=150)
	#################################
	funCLEAR = Button(window, text="CLEAR", command=functionCLEAR, bg='#4F4F4F', fg='white').place(x=240, y=150)
	#################################
	window['bg'] = 'black'
	window.geometry("300x300+200+200")
	#################################
	window.mainloop()

def logar():
	global login
	login = Tk()
	login.title('Login Central - Freud')
	login['bg'] = "black"
	#################################
	label1 = Label(login, text="Login: ", bg='black', fg='white').place(x=5, y=30)
	#################################
	label2 = Label(login, text="Senha: ", bg='black', fg='white').place(x=5, y=60)
	#################################
	global ed1, ed2
	ed1 = Entry(login)
	ed1.place(x=60, y=30)
	ed2 = Entry(login, show='*')
	ed2.place(x=60, y=60)
	#################################
	bt1 = Button(login, text="Confirmar", bg="black", fg="green", command=testar, width=20).place(x=60, y=100)
	bt2 = Button(login, text="Sair", bg="black", fg="green", command=sair, width=20).place(x=60, y=130)
	#################################

	cred = Label(login, text="Facebook", bg='black', fg='white', cursor="hand2")
	cred.place(x=10, y=170)

	cred1 = Label(login, text="Github", bg='black', fg='white', cursor="hand2")
	cred1.place(x=110, y=170)

	cred2 = Label(login, text="Youtube", bg='black', fg='white', cursor="hand2")
	cred2.place(x=210, y=170)

	cred.bind("<Button-1>", callback)
	cred1.bind("<Button-1>", callback1)
	cred2.bind("<Button-1>", callback2)
	#################################
	login.geometry("270x200+100+100")
	login.mainloop()

def testar():
	loginn = ed1.get()
	password = ed2.get()
	ison = requests.get('http://test.fcen.co.in/logins/vendido0.txt')
	if ison.status_code == 200:
		if 'on' in ison.text:
			r = requests.get('http://test.fcen.co.in/logins/login.txt')
			b = requests.get('http://test.fcen.co.in/logins/pass.txt')
			if r.status_code and b.status_code == 200:
				if hashlib.sha512(loginn).hexdigest().strip('\n') in r.text:
					if hashlib.sha512(password).hexdigest().strip('\n') in b.text:
						tkMessageBox.showinfo("Info", "[Logado com Sucesso!]")
						arq = open('conf.deb', 'w')
						arq.write(hashlib.sha512(password).hexdigest().strip('\n'))
						arq.close()
						login.destroy()
						main()
					else:
						tkMessageBox.showinfo("Info", "[!] Usuario ou Senha Invalidos, Tente Novamente! 2")
			else:
					tkMessageBox.showinfo("Info", "[!] Usuario ou Senha Invalidos, Tente Novamente! 1")
			else:
				tkMessageBox.showwarning("Warn", "[!] Problema de Conexao, Tente Novamente!")

		elif 'atualizar' in ison.text:
			tkMessageBox.showwarning("Warn", "[+] Voce deve atualizar Seu Programa, procure o Desenvolvedor e Contateo!\n%s"%menu)
		else:
			tkMessageBox.showwarning("Warn", "[!] A Aplicacao foi Desativada, Por algum motivo, contateo o Desenvolvedor!\n%s"%menu)


def sair():
	sys.exit()
	exit()

##################################################################

'''
if (os.path.exists('conf.deb') == True):
	with open('conf.deb', 'r') as login_file:
		b = requests.get('http://test.fcen.co.in/logins/pass.txt')
		if b.status_code == 200:
			if login_file.read() in b.text:
				main()
			else:
				print("[!] Exclua o arquivo conf.deb e tente novamente!")
		else:
			print("[!] Problema de Conexao, Tente Novamente!\n")
else:
	logar()
'''
main()
