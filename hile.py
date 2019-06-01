import win32event, win32api, winerror,win32console,win32api,win32gui
import pyautogui
import time
import win32api
import time
from tkinter import *
from threading import Thread

def click_hack():
    pyautogui.click(button='left', clicks=50, interval=0.05)


class Uyg():
    def __init__(self):
        self.state = None
        self.win = Tk()
        self.win.geometry("400x300")
        self.win.configure(bg = "black")
        self.label = Label(self.win,text="  :)   ----Wellcome----   (:",bg="dark green",fg = "black",font="Italic 20")
        self.label.pack(fill=X)
        self.win.title("Çağrı Atalar Macro v0.1")
        self.disbut = Button(self.win,font="Bold 15",text="Disable",bg = "black",fg ="red",command=self.geT,height = 1,width=22)
        
        self.disbut.pack()
        self.enabut = Button(self.win,font="Bold 15",text = "Enable",bg="black",fg = "green",command=self.seT,height = 1,width=22)
        self.enabut.pack()
        

    def handle_key2(self):
        while (self.state == False):
            
            if (win32api.GetAsyncKeyState(0x5A) < 0):
                self.seT()
                break
            else:
                continue
            time.sleep(0.01)
    def handle_key(self):
        while (self.state==True):
            print("state key alt değil")
            print(win32api.GetAsyncKeyState(0x12))
            if (win32api.GetAsyncKeyState(0x12) < 0 ):
                
                self.geT()
                break
            else:
                continue
            time.sleep(0.01)
               
    def run(self):
        self.win.mainloop()
        self.state = None
    
    def seT(self): 
        self.state = True
        print("seT e gelnidi enabled")
        self.label['fg'] = "red"
        self.label['text'] = "Started!!! Enjoy :)"
        self.label['fg'] = "black"
        self.label['bg'] = "dark green"
        t2 = Thread(target=self.handle_key,args=())
        t2.start()
        t1 = Thread(target = self.handle,args=())
        t1.start()
        print("t1 handle başla")
        
    def geT(self):
        
        print("geT e gelindi")
        self.label['text'] = "Stopped!!!"
        self.label['fg'] = "yellow"
        self.label['bg'] = "red"
        self.state = False
        t3 = Thread(target=self.handle_key2)
        t3.start()
       
        
    def handle(self):
        state_left = win32api.GetKeyState(0x01)  
        state_right = win32api.GetKeyState(0x02)  

        while (self.state == True):
            a = win32api.GetKeyState(0x01)
            b = win32api.GetKeyState(0x02)
    
            if a != state_left:  
                state_left = a
                print(a)
                if a < 0:
                    print('Left Button Pressed')
                    click_hack()
 
                else:
                    print('Left Button Released')

            if b != state_right:  
                state_right = b
                print(b)
                if b < 0:
                    print('Right Button Pressed')
                else:
                    print('Right Button Released')
            time.sleep(0.001)

        

def hide():
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window,0)
    return True

hide()






star = Uyg()
star.run()
