import re
import sqlite3
from tkinter import *
from tkinter import ttk
root = Tk()


connection = sqlite3.connect("Notafiscal.db")

cursor = connection.cursor()

#cursor.execute("CREATE TABLE Empresa (nome TEXT, data TEXT, valor FLOAT)")

Val = r"(?<=[V,v]alor:)\w.+"
Em = r"(?<=[e,E]mpresa:)\w.+"
Da = r"(?<=[d,D]ata:)\w.+"

#cursor.execute("INSERT INTO Empresa VALUES()")
#connection.commit()



 



frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Notas Fiscais").grid(column=0, row=0)
ttk.Button(frm, text="Sair", command=root.destroy).grid(column=1, row=4)
ttk.Button(frm, text="Mais", command=root.mainloop).grid(column=1, row=1)
ttk.Button(frm, text="Menos", command=root.mainloop).grid(column=1, row=2)
ttk.Button(frm, text="Inserir", command=root.mainloop).grid(column=1, row=3)


ex = open(r"C:/Users/alunoti/Desktop/notafiscalA.txt", "r", encoding = "utf=8").read()

(cursor.execute("SELECT * FROM Empresa").fetchall())

Val = re.findall(Val,ex)[0] 
Em = re.findall (Em,ex) [0]
Da = re.findall (Da,ex) [0]



#Grupo Thiago Serra, Afonso Henrique, Lucas Fonte, Ruan Caetano, João Pedro Guimarães 

root.mainloop()
