import customtkinter
from tkinter import *

class Graphic():

    def __init__(self,signal, bipolar):

        self.win = customtkinter.CTk()
        self.signal = signal

        self.win.geometry(f"{500}x{300}")
        self.win.title("NRZI Graphic")
        self.win.resizable(False, False)

        self.frame = customtkinter.CTkFrame(master=self.win, width=605, height=500)
        self.frame.place(x=0, y=0)


        if bipolar == True:
            self.DrawBipolar()
        else:
            self.Draw()

    def SetSignal(self,signal):
        self.signal = signal


    def Run(self):
        G_GUI = self.win
        G_GUI.mainloop()

    def Draw(self):
        canvas = Canvas(self.win,scrollregion=(0,0,900,0))
        x = 5
        y = 150
        moved = True
        canvas.create_line(5, 185, x + len(self.signal)*60 + 10, 185, fill="black", width=5)
        canvas.create_line(5, 50, 5, 300, fill="black", width=5)
        for i in range(0,len(self.signal)):
            print(self.signal[i])
            if (self.signal[i] == "1"):
                if moved==False:
                    moved = True

                    canvas.create_line(x,y,x,y - 70,fill="red",width=5)
                    y -= 70
                else:
                    moved = False

                    canvas.create_line(x, y, x, y + 70, fill="red", width=5)
                    y += 70

                canvas.create_line(x,y,x+60,y,fill="red",width=5)

            else:
                #canvas.create_line(x, y, x, y + 50, fill="red",width=5)
                canvas.create_line(x, y, x + 60, y,fill="red",width=5)

            x += 60
        hbar = Scrollbar(self.win, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas.xview)
        canvas.pack(fill=BOTH, expand=True, side=LEFT)

    def DrawBipolar(self):

        canvas = Canvas(self.win,scrollregion=(0,0,900,0))
        x = 5
        y = 150
        up = True
        canvas.create_line(5, 185, x + len(self.signal)*60 + 10, 185, fill="black", width=5)
        canvas.create_line(5, 50, 5, 300, fill="black", width=5)

        for i in range(0,len(self.signal)):

            if (self.signal[i] == "1"):

                if up == True:

                    canvas.create_line(x, y, x + 60, y , fill="blue", width=5)

                else:
                    canvas.create_line(x, y, x, y - 70, fill="blue", width=5)
                    canvas.create_line(x, y - 70, x + 60, y - 70 , fill="blue", width=5)
                    y -= 70
                    up = True

            else:

                if up == True:
                    canvas.create_line(x, y, x, y + 70, fill="blue", width=5)
                    canvas.create_line(x, y + 70, x + 60, y + 70 , fill="blue", width=5)
                    y += 70
                    up = False
                else:
                    canvas.create_line(x, y, x + 60, y , fill="blue", width=5)


            x += 60

        hbar = Scrollbar(self.win, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas.xview)
        canvas.pack(fill=BOTH, expand=True, side=LEFT)






