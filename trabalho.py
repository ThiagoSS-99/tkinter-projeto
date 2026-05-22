import re
import sqlite3
from tkinter import *
from tkinter import ttk
root = Tk()
#banco = banco.connect('Notafiscal.db')
connection = sqlite3.connect("Notafiscal.db")

cursor = connection.cursor()

#cursor.execute("CREATE TABLE Notafiscal_menor_50k (nome TEXT, data TEXT, valor FLOAT)")
#cursor.execute("CREATE TABLE Notafiscal_maior_50k (nome TEXT, data TEXT, valor FLOAT)")
#cursor.execute("CREATE TABLE Notafiscal_maior_100k (nome TEXT, data TEXT, valor FLOAT)")

cursor.execute("SELECT * FROM Notafiscal")
print(cursor.fetchall())


Val = r"(?<=[V,v]alor:)\w.+"
Em = r"(?<=[e,E]mpresa:)\w.+"
Da = r"(?<=[d,D]ata:)\w.+"


def salvar_menor_50k():
    cursor.execute("INSERT INTO Notafiscal_menor_50k VALUES('"+Em+"' ,'"+Da+"' , '"+Val+"')")
connection.commit()

def salvar_maior_50k():
    cursor.execute("INSERT INTO Notafiscal_maior_50k VALUES('"+Em+"' ,'"+Da+"' , '"+Val+"')")
connection.commit()

def salvar_maior_100k():
    cursor.execute("INSERT INTO Notafiscal_maior_100k VALUES('"+Em+"' ,'"+Da+"' , '"+Val+"')")
connection.commit()
    
    
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="Notas Fiscais").grid(column=0, row=0)
butao1 = Button(frm, text="Sair", command=root.destroy).grid(column=1, row=4)
butao2 = Button(frm, text="50k+", command=salvar_maior_50k).grid(column=1, row=1)
butao3 = Button(frm, text="-50k", command=salvar_menor_50k).grid(column=1, row=2)
butao4 = Button(frm, text="100k+", command=salvar_maior_100k).grid(column=1, row=3)






ex = open(r"C:/Users/Ruan/OneDrive/Área de Trabalho/notasficais/novanota.txt", "r", encoding = "utf=8").read()



Val = re.findall (Val,ex)[0]
Em = re.findall (Em,ex)[0]
Da = re.findall (Da,ex)[0]

cursor.execute("INSERT INTO Notafiscal VALUES('"+Em+"' ,'"+Da+"' , '"+Val+"')")
connection.commit()




#Grupo Thiago Serra, Afonso Henrique, Lucas Fonte, Ruan Caetano, João Pedro Guimarães 

root.mainloop()
