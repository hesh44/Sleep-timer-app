import tkinter as tk
from tkinter import filedialog, Text, LEFT, BOTTOM, font
import os
import time

# represents mostly the main window of an application
root = tk.Tk(className='Sleep timer')
root.geometry("1000x200")

# ne koristim vise ovu funkciju, zelim samo program za spavanje
def ugasiZa(vreme):
    os.system("shutdown /s /t {0}".format(vreme))

def prekiniGasenje():
    os.system("shutdown /a")

def spavanje(vreme):
    time.sleep(vreme)
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# canvas = tk.Canvas(root, height=100, width=300, bg="#263D42")

# attach canvas to the root
# canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.9, relheight=0.9, relx=0.02, rely=0.02)
frame.pack()

bottomframe = tk.Frame(root)
bottomframe.pack(side=BOTTOM)

myFont = tk.font.Font(size=25)

min30 = tk.Button(frame, text="30 min", width=10, pady=5, fg="white", bg='#263D42', command=lambda : spavanje(1800))
min30.pack(side=LEFT)
min30['font'] = myFont

h1 = tk.Button(frame, text="1h", width=10, pady=5, fg="white", bg='#263D42', command=lambda : spavanje(3600))
h1.pack(side=LEFT)
h1['font'] = myFont

h1min30 = tk.Button(frame, text="1h 30 min", width=10, pady=5, fg="white", bg='#263D42', command=lambda : spavanje(5400))
h1min30.pack(side=LEFT)
h1min30['font'] = myFont

h2 = tk.Button(frame, text="2h", width=10, pady=5, fg="white", bg='#263D42', command=lambda : spavanje(7200))
h2.pack(side=LEFT)
h2['font'] = myFont

spavanjeB = tk.Button(frame, text="20 sek", width=10, pady=5, fg="white", bg='#263D42', command=lambda : spavanje(20))
spavanjeB.pack(side=LEFT)
spavanjeB['font'] = myFont

terminate = tk.Button(bottomframe, text="terminate (vrv nece raditi)", width=10, pady=5, fg="white", bg='#263D42', command=prekiniGasenje)
terminate.pack(side=BOTTOM)
terminate['font'] = myFont

# ovo pokrece program valjda
root.mainloop()
#aaaaaaaaaaaaa