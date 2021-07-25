from tkinter import *
import time
import pyautogui
def screen_shot():
    name=int(round(time.time()*1000))
    name="Image"+"{}.png".format(name)
    #time.sleep(2)
    img=pyautogui.screenshot(name)
    img.show()
    win.deiconify()
def delay():
    win.withdraw()
    win.after(1000,screen_shot)
win=Tk()
win["bg"]="black"
win.title("SCREENSHOT GUI")
win.geometry("300x300")
win.resizable()
btn=Button(win,text="Take Screenshot",font=("Arial",10,"bold"),height=2,width=14,bg="yellow",command=delay).place(x=95,y=70)
btn=Button(win,text="Exit",font=("Arial",10,"bold"),height=2,width=10,bg="green",command=quit).place(x=110,y=135)
win.mainloop()
