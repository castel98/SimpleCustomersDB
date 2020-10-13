from pymongo import MongoClient




client = MongoClient()
col = client.mydb.clienti


def modify_(nome, cognome, campo, modifica):

    print(col.find_one({"nome": nome , "cognome": cognome}))
    var = col.find_one({"nome": nome , "cognome": cognome})
    v = var.get('_id')
    print(v)

    col.find_one_and_update({"_id" : v}, {"$set" : { campo : modifica}})

#######################################################################################################

def trova(nome_r, cognome_r):

    obj1= (col.find_one({ "nome" : nome_r, "cognome" : cognome_r}))
    str = 'nome: ' + obj1['nome'] + ' '+ obj1['cognome'] + ', \n' + 'comune di: ' \
          +  obj1['comune'] + ', \n'  + 'indirizzo: ' + obj1['indirizzo'] + ', \n' + \
          'pratica: ' + obj1['pratica']  + ', \n' + 'nota: ' + obj1['nota']

    return str

#######################################################################################################
def lista():
   lista_R = []
   for obj1 in list(col.find({})):
       str = 'nome: ' + obj1['nome'] + ' '+ obj1['cognome'] + ', \n' + 'comune di: ' \
          +  obj1['comune'] + ', \n'  + 'indirizzo: ' + obj1['indirizzo'] + ', \n' + \
          'pratica: ' + obj1['pratica']  + ', \n' + 'nota: ' + obj1['nota']
       lista_R.append(str)

   return  lista_R

##########################################################################################################
def elimina():
    print("inserisci il nome della persona da eliminare")
    nome_el = input()
    print("inserisci il cognome della persona da eliminare")
    cognome_el = input()
    col.delete_one({"nome" : nome_el, "cognome" : cognome_el})

#trova()
#modifica()
#lista()
#elimina()

#######################################################################################################

def insert(nome, cognome, comune, indirizzo, pratica, nota):
    col.insert_one({"nome" : nome,
                    "cognome" : cognome,
                    "comune": comune,
                    "indirizzo" : indirizzo,
                    "pratica": pratica,
                    "nota" : nota})

#####################################################################################################

#####################################################################################################
import tkinter as tk
from tkinter import *
from functools import partial




########################################################################################

def createNewWindow():
    nome=tk.StringVar()
    cognome= tk.StringVar()
    comune = tk.StringVar()
    indirizzo = tk.StringVar()
    pratica = tk.StringVar()
    nota = tk.StringVar()


    newWindow = tk.Toplevel(app)
    newWindow.geometry("600x600")

    label = tk.Label(newWindow, text = "inserisci il nome")
    label.pack()
    casella = tk.Entry(newWindow, textvariable = nome)
    casella.pack()
    label2 = tk.Label(newWindow, text="inserisci il cognome")
    label2.pack()
    casellacognome = tk.Entry(newWindow, textvariable=cognome)
    casellacognome.pack()
    label3 = tk.Label(newWindow, text="inserisci il comune di residenza")
    label3.pack()
    casellacomune= tk.Entry(newWindow, textvariable=comune)
    casellacomune.pack()
    label4 = tk.Label(newWindow, text="inserisci l'indirizzo di residenza")
    label4.pack()
    casellaind = tk.Entry(newWindow, textvariable=indirizzo)
    casellaind.pack()
    label5 = tk.Label(newWindow, text="inserisci il numero di pratica")
    label5.pack()
    caspratica= tk.Entry(newWindow, textvariable=pratica)
    caspratica.pack()
    label6 = tk.Label(newWindow, text="inserisci la nota")
    label6.pack()
    nota = tk.Entry(newWindow, textvariable = nota, width = 50)
    nota.pack()


    labelResult = tk.Label(newWindow)

    labelResult.pack()

    def inserimento(name, cognome, comune, indirizzo, pratica, nota, label_result):
        nome_c = (name.get())
        cognome_c=(cognome.get())
        comune_c=(comune.get())
        indirizzo_c=(indirizzo.get())
        pratica_c=(pratica.get())
        nota_c=(nota.get())
        print(nome_c)
        insert(nome_c, cognome_c, comune_c, indirizzo_c, pratica_c, nota_c)
        label_result.config(text="okay inviato! chiudi la finestra")
        return

    inserimento = partial(inserimento, nome, cognome, comune, indirizzo, pratica, nota, labelResult)
    buttonExample = tk.Button(newWindow, text="invia", command = inserimento)
    buttonExample.pack()

    newWindow.mainloop()
#############################################################################################

def bottonemodifica():
    campo_modifica = tk.StringVar()
    nome_modifica =  tk.StringVar()
    cognome_modifica=  tk.StringVar()
    modifi = tk.StringVar()

    newWindow = tk.Toplevel(app)
    newWindow.geometry("600x600")
    label_nome = tk.Label(newWindow, text="inserisci il nome della persona da modificare")
    label_nome.pack()
    casella_nome = tk.Entry(newWindow, textvariable=nome_modifica)
    casella_nome.pack()
    label_cognome = tk.Label(newWindow, text="inserisci il cognome della persona da modificare")
    label_cognome.pack()
    casella_cognome = tk.Entry(newWindow, textvariable=cognome_modifica)
    casella_cognome.pack()
    label = tk.Label(newWindow, text="inserisci il campo che vuoi modificare tra nome, cognome, indirizzo, comune, nota, numero pratica")
    label.pack()
    casella = tk.Entry(newWindow, textvariable=campo_modifica)
    casella.pack()
    label_modifica = tk.Label(newWindow, text="inserisci la modifica")
    label_modifica.pack()
    casella_modifica = tk.Entry(newWindow, textvariable=modifi)
    casella_modifica.pack()
    labelResult = tk.Label(newWindow)

    labelResult.pack()

    def modifica(nome, cognome, campo, modi, label_result):
        nome_c= (nome.get())
        cognome_c = (cognome.get())
        campo_c = (campo.get())
        modi_c = (modi.get())
        modify_(nome_c, cognome_c, campo_c, modi_c)
        label_result.config(text="okay inviato! chiudi la finestra")

    mof = partial(modifica, nome_modifica, cognome_modifica, campo_modifica, modifi, labelResult)
    buttonExample = tk.Button(newWindow, text="invia", command=mof)
    buttonExample.pack()

    newWindow.mainloop()
##############################################################################################################
def trovaevisual():
    nome_t = tk.StringVar()
    cognome_t = tk.StringVar()

    newWindow = tk.Toplevel(app)
    newWindow.geometry("600x600")
    label_nome = tk.Label(newWindow, text="inserisci il nome della persona da ricercare")
    label_nome.pack()
    casella_nome = tk.Entry(newWindow, textvariable=nome_t)
    casella_nome.pack()
    label_cognome = tk.Label(newWindow, text="inserisci il cognome della persona da ricercare")
    label_cognome.pack()
    casella_cognome = tk.Entry(newWindow, textvariable=cognome_t)
    casella_cognome.pack()

    def tt (nome, cognome):
        nome_tt = (nome.get())
        cognome_tt = (cognome.get())
        str = trova(nome_tt, cognome_tt)
        label= tk.Label(newWindow, text= str)
        label.pack()


    mof = partial(tt, nome_t, cognome_t)
    buttonExample = tk.Button(newWindow, text="invia", command=mof)
    buttonExample.pack()

#############################################################################################################
def visualizza_tutti():
    newWindow = tk.Toplevel(app)
    newWindow.geometry("600x600")
    label_nome = tk.Label(newWindow, text="visualizza tutti")
    label_nome.pack()
    LL = lista()
    label = tk.Label(newWindow, text=LL)
    label.pack()






app = tk.Tk()
app.geometry("600x600")
app.title("clienti")

buttonExample = tk.Button(app,
              text="inserisci",
              command=createNewWindow)
buttonExample.pack()

buttonmod = tk.Button(app,
              text="modifica",
              command=bottonemodifica)
buttonmod.pack()

buttonmod = tk.Button(app,
              text="trova e visualizza",
              command=trovaevisual)
buttonmod.pack()

buttonmodi = tk.Button(app,
              text="visualizza tutti",
              command=visualizza_tutti)
buttonmodi.pack()
app.mainloop()
