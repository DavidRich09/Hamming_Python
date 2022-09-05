import customtkinter
from tkinter import *

class Graphic():

    def __init__(self,signal):

        self.win = customtkinter.CTk()
        self.signal = signal

        self.win.geometry(f"{500}x{300}")
        self.win.title("NRZI Graphic")
        self.win.resizable(False, False)

        self.frame = customtkinter.CTkFrame(master=self.win, width=605, height=500)
        self.frame.place(x=0, y=0)

        self.Draw()

    def SetSignal(self,signal):
        self.signal = signal

    def RemoveLeft0(self):
        pos = 0
        for i in self.signal:
            if i == "1":
                break
            else:
                pos += 1
        self.signal = self.signal[pos:]

    def Run(self):
        G_GUI = self.win
        G_GUI.mainloop()

    def Draw(self):
        canvas = Canvas(self.win,scrollregion=(0,0,800,0))
        x = 5
        y = 200
        moved = False
        self.RemoveLeft0()
        canvas.create_line(5, 200, x + len(self.signal)*60 + 10, 200, fill="black", width=5)
        canvas.create_line(5, 50, 5, 300, fill="black", width=5)
        for i in range(0,len(self.signal)):
            print(self.signal[i])
            if (self.signal[i] == "1"):
                if moved==False:
                    moved = True
                    if x != 5:
                        canvas.create_line(x,y,x,y - 50,fill="red",width=5)
                    y -= 50

                canvas.create_line(x,y,x+60,y,fill="red",width=5)

            else:
                if moved:
                    moved = False
                    canvas.create_line(x, y, x, y + 50, fill="red",width=5)
                    y += 50
                canvas.create_line(x, y, x + 60, y,fill="red",width=5)

            x += 60
        hbar = Scrollbar(self.win, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas.xview)
        canvas.pack(fill=BOTH, expand=True, side=LEFT)






