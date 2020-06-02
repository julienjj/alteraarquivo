import os, re
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
root = Tk()
root.withdraw()
folder_selected = filedialog.askdirectory(initialdir='l://',title="SELECIONE A OF - duvidas: Julien")

    
directory = os.listdir(folder_selected+'/nc')
os.chdir(folder_selected+'/nc')

comparador = []
texto=[]
i=0

for file in directory:
  
    open_file = open(file,'r')
    texto= open_file.readlines()
    aux=texto[8]
    comparador.append([aux])
    print(str(comparador[i]).replace('\\n','').replace('/',''))
    i+=1    

directory2 = os.listdir(folder_selected+'/croqui/')
os.chdir(folder_selected+'/croqui/')
i=0
for nome in directory2:
    novo_nome= str(comparador[i]).replace('\\n','').replace('/','')+str(nome)
    os.rename(folder_selected+"/croqui/"+nome,folder_selected+"/croqui/"+(novo_nome))
    i+=1
messagebox.showinfo("Alterado", "Alterado com sucesso")
