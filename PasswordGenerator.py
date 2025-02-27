import tkinter as tk
from tkinter import messagebox

#Tee usu frame nimega frame2. Taust kollane. Paisuta esimese frame alla sarnaselt. Paiguta lbl_previous frame2-le.


#Funktsioon hiire kordinaatide jaoks
def mouse_motion(event=None):
    x, y = event.x, event.y
    lbl_mouse.config(text=f'x = {x}, y = {y}') #Kirjutab hiire kordinaadid

#Tervitustekst
def welcome(event=None):
    name = txt_name.get().strip().title() #Eemaldab tühikud ja kirjutab suure tähega
    #print(name) #test konsooli
    if name:
        messagebox.showinfo('Tervitus', f'Tere, {name}!') #Tervitusteks: esimene on kasti nimi ja teine on sõnumi sisu.
        lbl_previous.config(text=name) #Kirjutab labelisse selle viimase sisestatud nime.
    else:
        messagebox.showerror('Hoiatus', f'Nime pole sisestatud!')
        lbl_previous.config(text='VIGA')

    txt_name.delete(0, 'end') #Kustutab eelneva sisestuse Sobib ka tk.END

window = tk.Tk() #Esimene on tk lühend ja teine on funktsioon
window.title('Lihtne kasutajaliides') #Põhiakna loomine (Tiitelriba teksti määramine)
window.geometry('450x250') #Pikslites akna suurus laiusxkõrgus
window.resizable(False, False) #Akna suurust muuta ei saa (Vaikimisi muidu saab muuta)


#Põhiaknale frame loomine
frame = tk.Frame(window, background='lightblue') #loome frame
frame.pack(fill='both') #Paiguta põhiaknale (vabasse kohta) fill='both' teeb põhiakna ääre värviliseks. #Pack teeb nähtavaks Sobib ka tk.BOTH

#Ülesanne frame2 panemine
frame2 =tk.Frame(window, background='yellow')
frame2.pack(fill=tk.BOTH) #Kasuta expand=True koos .place()

# Label nimi
tk.Label(frame, text='Nimi', background='lightblue').pack(side=tk.LEFT, padx=3, pady=3) #Label luuakse, pannakse ja sinna jääb #padx ja pady kui palju ruumi jätta

#Sisestuskast (Entry)
txt_name = tk.Entry(frame) #Loome sisestuskasti
txt_name.focus() #Sisestuskast aktiivseks ehk kursor on seal kohe plinkimas
txt_name.pack(side=tk.LEFT, padx=3, pady=3) #Teeme nähtavaks

#Nupp (Button)
btn_submit = tk.Button(frame, text='Näita', command=lambda: welcome()) #command rida juurde lisada, et ta kutsuks välja selle welcom def-i
btn_submit.pack(side=tk.LEFT, padx=3, pady=3)

# Hiire koordinaadid (Label)
lbl_mouse = tk.Label(frame, text='x = 0, y = 0', background='lightblue')
lbl_mouse.pack(side=tk.LEFT, padx=3, pady=3)

# Eelnev tekst (Label)
lbl_previous = tk.Label(frame2, text='POLE', background='yellow') #frame2 muutsin ülesande pärast
#lbl_previous.pack(side=tk.LEFT, padx=3, pady=3)
#lbl_previous.place(x=5, y=5) #Kui kasutad place siis peab panema frame2 juures expand=True. Lükkab kogu vaba akna seda frame täis
lbl_previous.grid(row=0, column=0) #grid ilma expandita teeb ka ühe rea

window.bind('<Motion>', mouse_motion) #Paneb hiireliikumise funktsiooni tööle

window.bind('<Return>', welcome) #Paneb enter klahvi ka töötama lisaks buttonile

window.mainloop() #Se on koodi viimane rida