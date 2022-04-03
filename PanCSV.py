from tkinter import *
from tkinter import filedialog
import csv
import numpy as np
import random

listD = 'a'
listZ = 'b'

#function to get the .json file, configure it following the README.md
def lblank():
    f = open('PanAIOblank.json', "r")

    return(f.read())

blank = lblank()

#function to get Zalando accounts from csv PanAioZalando.csv
def PanFind(Discord):
    l = []

    with open(listZ, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            ekip = row[0].split(',')
            l.append(ekip)


        tot = []
        for j in l:

            if j[0] == Discord:
                tot.append((j[1],j[2]))

    return(set(tot))


#formatting function for PAN .json
def CreatePan(PanFinding):

    n = len(PanFinding)
    text = ''

    for t in PanFinding:
        osef = ''
        for j in range(9):
            wow = chr(random.randint(ord('a'), ord('z')))
            osef = osef+wow

        ll = '['
        zalDiscord = PanFind(t)
        for k in zalDiscord:
            ll = ll + '{"email":"' + k[0] + '","password":"' + k[1] + '"},'

        ll = ll[:-1]
        ll = ll + ']'

        text = text +'"' + osef + '":{"accounts":' + ll + ',"site":"Zalando","name":"' + t + '"},'


    text = text[:-1]
    print(text)
    return(text)

#function to get discord accounts from listDiscord.csv
def splitDiscord(listDiscord):
  l = []
  with open(listDiscord, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in spamreader:
            #ekip = row[0].split(',')
            l.append(row[0])

  return(l)


#function exec
def execPan():
    #listDiscord = listD
    with open(saisie.get() + 'Ekip.json', 'w') as f:
        f.write(blank.replace('EKIP',CreatePan(splitDiscord(listD))))






def listDfile(a):
    global listD
    listD = a

def listZfile(a):
    global listZ
    listZ = a


#function GUI
def browseFilesDiscord():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.csv*"),
                                                       ("all files",
                                                        "*.*")))


    label_file_explorer_Discord.configure(text="File Opened: "+filename)
    listDfile(filename)

def browseFilesZalando():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.csv*"),
                                                       ("all files",
                                                        "*.*")))


    label_file_explorer_Zalando.configure(text="File Opened: "+filename)
    listZfile(filename)


#GUI
window = Tk()

window.title('PanCSV')

window.geometry("350x200")

window.config(background = "white")

label_file_explorer_Discord = Label(window,
                            text = "File Explorer Discord",
                            width = 50, height = 2,
                            fg = "blue")


button_explore_Discord = Button(window,
                        text = "Browse Discord Files",
                        command = browseFilesDiscord)

label_file_explorer_Zalando = Label(window,
                            text = "File Explorer Zalando",
                            width = 50, height = 2,
                            fg = "blue")


button_explore_Zalando = Button(window,
                        text = "Browse Zalando Files",
                        command = browseFilesZalando,

                        )


spacer1 = Label(window, text="",width = 0)

saisie = Entry(window,width = 40)
saisie.insert(5,'.json directory')

button_gen = Button(window,
                     text = "Generate .json",
                     command = execPan,
                     fg = "red")



label_file_explorer_Discord.grid(column = 1, row = 1)

button_explore_Discord.grid(column = 1, row = 2)

label_file_explorer_Zalando.grid(column = 1, row = 3)

button_explore_Zalando.grid(column = 1, row = 4)

spacer1.grid(row=5, column=1)

saisie.grid(column = 1, row = 6)

button_gen.grid(column = 1,row = 7)



window.mainloop()