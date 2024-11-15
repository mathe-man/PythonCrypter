"""

Logiciel programmé par Mathieu Mousset indépendament

Version:                    24.04.22    -mise en place du fichier "ressource" contenant les autres fichiers nécessaire, pour faciliter l'installation du programme
Informaation de version
historique de des verssions 24.04.21    -Ajout del'interface numérique utilisateur(UI) et f() codage/décodage des mots et phrase
                                        -Bouton de copie dans l'interface et changement de mode

License: CC-BY-SA license
Attribution-ShareAlike 4.0 International


"""

import tkinter as tk
from tkinter import *
import pyperclip
import keyboard
import zipfile
import os
import shutil


def bin_by_file(f="binaire.txt"):
    with open(f, "r") as fa:
        for ligne in fa:
            bin_list.append(ligne[0: 6])
        print(bin_list)


# maj_list = ["²", "A", "Z", "R", "T", "U", "I", "O", "P", "Q", "S", "D", "F", "G", "H", "J", "K", "L", "M", "W", "X", "C", "V", "B", "N"]
alphabet_list = [" ", "a", "z", "e", "r", "t", "y", "u", "i", "o", "p", "q", "s",
                 "d","c",
                 "f", "g", "h", "j", "k", "l", "m", "w",
                 "x", "c", "v", "b", "n", "?", ".", "!", ";", ":", "-", "<",
                 ">", "(", ")", "[", "]", "é", "è", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "à", "{", "}",
                 "+", "-", "*", "/", "=", ","]
bin_list = ['000000', '000001', '000010', '000011', '000100', '000101', '000110', '000111', '001000', '001001', '001010', '001011', '001100', '001101', '001110', '001111', '010000', '010001', '010010', '010011', '010100', '010101',
            '010110', '010111', '011000', '011001', '011010', '011011', '011100', '011101', '011110', '011111', '100000', '100001', '100010', '100011', '100100', '100101', '100110', '100111', '101000', '101001', '101010', '101011',
            '101100', '101101', '101110', '101111', '110000', '110001', '110010', '110011', '110100', '110101', '110110', '110111', '111000', '111001', '111010', '111011', '111100', '111101', '111110', '111111']
input_chiffrement = ""
output_chiffrement = ""


def code_list_print():
    dy = 1
    while dy < len(bin_list) and dy < len(alphabet_list):
        print(f"{bin_list[dy]}      {alphabet_list[dy]}     {dy}")
        dy = dy + 1


def base50_to_binaire(base50_text):
    global input_chiffrement
    input_chiffrement = str(base50_text)
    global output_chiffrement
    output_chiffrement = ""
    while not input_chiffrement == "":
        """if input_chiffrement[0] in maj_list:
            input_chiffrement = alphabet_list[maj_list.index(input_chiffrement[0])] + input_chiffrement[1:len(input_chiffrement)]
            print(input_chiffrement)"""
        output_chiffrement = output_chiffrement + " " + bin_list[alphabet_list.index(input_chiffrement[0])]
        rdm_use = 0
        rdm_use2 = ""
        while not rdm_use == len(input_chiffrement)-1:
            rdm_use += 1
            rdm_use2 = rdm_use2 + input_chiffrement[rdm_use]
        input_chiffrement = rdm_use2


def binaire_to_base50(binary_text):
    global input_chiffrement
    input_chiffrement = binary_text
    global output_chiffrement
    output_chiffrement = ""
    while not input_chiffrement == "":
        letter = input_chiffrement.split(" ")[1]
        output_chiffrement = output_chiffrement + alphabet_list[bin_list.index(letter)]
        rdm_use = 7
        rdm_use2 = ""
        while not rdm_use == len(input_chiffrement):
            rdm_use += 1
            rdm_use2 = rdm_use2 + input_chiffrement[rdm_use]
        input_chiffrement = rdm_use2


InLetterCryp = ""
OutLetterCryp = ""


def lettre_a_lettre_code(normal_txt, prt=False):
    global InLetterCryp
    InLetterCryp = normal_txt
    global OutLetterCryp
    OutLetterCryp = ""
    base50_to_binaire(InLetterCryp)
    a = output_chiffrement[1:4]
    b = output_chiffrement[4:7]
    a = " " + a + "010"
    b = " 001" + b
    binaire_to_base50(a)
    a = output_chiffrement
    binaire_to_base50(b)
    b = output_chiffrement
    OutLetterCryp = a + b
    if prt:
        print(OutLetterCryp)
    return OutLetterCryp


def lettre_code_a_lettre(code_txt, prt=False):
    global InLetterCryp
    InLetterCryp = code_txt
    global OutLetterCryp
    OutLetterCryp = ""
    a = InLetterCryp[0]
    b = InLetterCryp[1]
    base50_to_binaire(a)
    a = output_chiffrement[0:4]
    base50_to_binaire(b)
    b = output_chiffrement[4:7]
    OutLetterCryp = a + b
    binaire_to_base50(OutLetterCryp)
    OutLetterCryp = output_chiffrement
    if prt:
        print(OutLetterCryp)
    return OutLetterCryp


InMotCryp = ""
OutMotCryp = ""


def code_mot(mot_normale):
    global InMotCryp
    global OutMotCryp
    InMotCryp = mot_normale
    OutMotCryp = ""
    while not InMotCryp == "":
        lettre_a_lettre_code(InMotCryp[0])
        OutMotCryp = OutMotCryp + OutLetterCryp
        InMotCryp = InMotCryp[1:len(InMotCryp)]
    print(OutMotCryp)
    return OutMotCryp


def decode_mot(mot_code):
    global InMotCryp
    global OutMotCryp
    InMotCryp = mot_code
    OutMotCryp = ""
    while not InMotCryp == "":
        lettre_code_a_lettre(str(InMotCryp[0] + InMotCryp[1]))
        OutMotCryp = OutMotCryp + OutLetterCryp
        InMotCryp = InMotCryp[2:len(InMotCryp)]
    print(OutMotCryp)
    return OutMotCryp


image = {}


def load_ressource(archive_file):
    global image
    extrac_folder = "temp"
    os.rename(archive_file, archive_file + ".zip")
    with zipfile.ZipFile(archive_file + ".zip", 'r') as zipf:
        zipf.extractall(extrac_folder)
        image["icon"] = PhotoImage(file="temp/logo.png")
        image["copy_button"] = PhotoImage(file="temp/copy_button.png").zoom(1).subsample(3)
        image["fleche"] = PhotoImage(file="temp/Translate_button.png")
    shutil.rmtree("temp")
    os.rename(archive_file + ".zip", archive_file)


traduct_mod = "code"
mod_text = "(mot >> mot codé)"
# Création de l'interface pour l'utilisateur

UI = tk.Tk()
UI.geometry("600x300")
UI.minsize(400, 240)
UI.maxsize(500, 300)
UI.title("Chiffrement de données textuels")
load_ressource("ressources")
# icon = PhotoImage(file="logo.png")
UI.iconphoto(False, image["icon"])
UI.config(relief="sunken", bg="#5A90AD")


# Box entrer de valeur

entry_Input = Entry(UI, width=40, bg="#B6CAEB", borderwidth=0.5, relief="solid")
entry_Input.place(x=50, y=50)


title_Input = Label(UI, text="Entrer un texte à transformé", font=("COURRIER", 13), bg="#5A90AD", borderwidth=2)
title_Input.place(x=50, y=25)


title_Output = Label(UI, text="Le résultat sera ici", font=("COURRIER", 13), bg="#5A90AD", borderwidth=2)
title_Output.place(x=50, y=100)

entry_Output = Entry(UI, width=40, bg="#B6CAEB", borderwidth=0.5, relief="solid")
entry_Output.place(x=50, y=125)


def translate():
    world = entry_Input.get()
    print(f"Traduction effectué de << {world} >>")
    if traduct_mod == "code":
        entry_Output.delete(0, tk.END)
        result = str(code_mot(world))
        entry_Output.insert(0, result)

    elif traduct_mod == "decode":
        entry_Output.delete(0, tk.END)
        result = str(decode_mot(world))
        entry_Output.insert(0, result)
    else:
        entry_Output.delete(0, tk.END)
        entry_Output.insert(0, "Une erreur c'est produite, le redémarrage du programme devrait remédier au problème.ErN.219")


def change_mod():
    global traduct_mod
    if traduct_mod == "code":
        traduct_mod = "decode"
        print("Traduct mod set to decode")
        mod_indicator.configure(text="(mot codé à mot)")

    elif traduct_mod == "decode":
        traduct_mod = "code"
        print("Traduct mod set to code")
        mod_indicator.configure(text="(mot à mot codé)")

    else:
        entry_Output.delete(0, tk.END)
        entry_Output.insert(0, "Une erreur c'est produite, le redémarrage du programme devrait remédier au problème.ErN.200")


def copy_result():
    if entry_Output.get() == "":
        print("there nothing to copy!")
    else:
        pyperclip.copy(entry_Output.get())


def on_key(event):
    if keyboard.is_pressed("Return"):
        translate()


entry_Input.bind("<KeyPress>", on_key)

# fleche = PhotoImage(file="Translate_button.png")
translate_button = Button(UI, image=image["fleche"], command=translate, borderwidth=1)
translate_button.place(x=340, y=70)

translate_mod = Button(UI, text=f"Changer de mode", command=change_mod)
translate_mod.place(x=100, y=200)

mod_indicator = Label(text="(mot à mot codé)", font=("COURRIER", 10), bg="#5A90AD", fg="#000000")
mod_indicator.place(x=130, y=100)


# copy_button = PhotoImage(file="copy_button.png").zoom(1).subsample(3)
copy_zone = Button(UI, width=30, height=30, highlightthickness=7, image=image["copy_button"], overrelief="flat", fg="#000000", command=copy_result)
copy_zone.place(x=240, y=150)


UI.mainloop()
