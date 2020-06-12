import tkinter as tk
from tkinter import messagebox
import psutil
from time import sleep
import wmi
import threading
import pythoncom

win = tk.Tk()
win.title("GTA 5 Private Public Lobby")
win.wm_iconbitmap("icon2.ico")


#Window size/Window Center
win.resizable(False, False)
window_height = 200
window_width = 500

screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

win.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))
#Window size/Window Center

win.configure(background = 'black')
TL = tk.Label(win, text = 'GTA 5 Private Public Lobby', fg = 'green', bg = 'black', font = (None, 30), height = 2)
TL.pack(anchor = 'n')

def th_freeze():
    pythoncom.CoInitialize() #pylint: disable=no-member
    PROCNAME = 'GTA5.exe'
    f = wmi.WMI()
    found = False
    for proc in f.Win32_Process():
        if PROCNAME in proc.Name:
            # print(f"{proc.ProcessId:<10} {proc.Name}")
            found = True
            print('Process found.. kicking players...')
            p = psutil.Process(proc.ProcessID)
            p.suspend()
            sleep(10)
            p.resume()
            print("Done. Players kicked.")
            messagebox.showinfo("GTA 5 Private Public Lobby", "You May Now Close The Program You're Now In A Public Lobby With No Other Players, Enjoy!")
    if found is False:
        print('You are not running GTA!')
        messagebox.showinfo("Ooops!", "You Are Not Running GTA 5!")

def GTACommand():
    x = threading.Thread(target=th_freeze)
    x.start()
    
def About():
    messagebox.showinfo("Made By BaseGodFelix", "Allows You To Have Your Own Public Lobby To Get Away From Greifers/Hackers")
    
    
button1 = tk.Button(win, text="Start", width=25, command=GTACommand)
button2 = tk.Button(win, text="About", width=25, command=About)
button1.pack(anchor='center')
button2.pack(anchor='center')
win.mainloop()