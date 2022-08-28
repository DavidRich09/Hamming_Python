from tkinter import *
import customtkinter
from Converter import Converter

#need custom tkinters for this to work
#pip3 install customtkinter
#documentation: https://github.com/TomSchimansky/CustomTkinter

class GUI(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        #create a window
        self.geometry(f"{605}x{500}")
        self.title("Hamming Code")
        self.resizable(False, False)

        #create a converter object
        self.converter = Converter()

        #main frame
        self.frame = customtkinter.CTkFrame(master=self.master, width=605, height=500)
        self.frame.place(x=0, y=0)

        #numbre entry
        self.numberEntry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Enter a number ")
        self.numberEntry.place(x=10, y=10)

        #entry number button
        self.numberButton = customtkinter.CTkButton(master=self.frame, text="Calculate", command=self.Calculate)
        self.numberButton.place(x=160, y=10)

        #generate converter table with labels
        self.label = customtkinter.CTkLabel(master=self.frame, text="Converter Table")
        self.label.place(x=0, y=50)

        self.decimal = customtkinter.CTkLabel(master=self.frame, text="Decimal")
        self.decimal.place(x=0, y=70)

        self.decimalNumber = customtkinter.CTkLabel(master=self.frame, text="")
        self.decimalNumber.place(x=130, y=70)

        self.binary = customtkinter.CTkLabel(master=self.frame, text="Binary")
        self.binary.place(x=0, y=90)

        self.binaryNumber = customtkinter.CTkLabel(master=self.frame, text="")
        self.binaryNumber.place(x=130, y=90)

        self.hexa = customtkinter.CTkLabel(master=self.frame, text="Hexadecimal")
        self.hexa.place(x=0, y=110)

        self.hexaNumber = customtkinter.CTkLabel(master=self.frame, text="")
        self.hexaNumber.place(x=130, y=110)

        #Switch to parity

        self.switchVar= StringVar(value="on")
        self.switchVar = customtkinter.CTkSwitch(master=self.frame, text="Even parity", command=self.switch_event, variable=self.switchVar, onvalue="on", offvalue="off")
        self.switchVar.place(x=310, y=15)

        #entry for each number in binary table in total is 11 numbers

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry1.place(x=330, y=70)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry2.place(x=355, y=70)

        self.entry3 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry3.place(x=380, y=70)

        self.entry4 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry4.place(x=405, y=70)

        self.entry5 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry5.place(x=430, y=70)

        self.entry6 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry6.place(x=455, y=70)

        self.entry7 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry7.place(x=480, y=70)

        self.entry8 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry8.place(x=505, y=70)

        self.entry9 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry9.place(x=530, y=70)

        self.entry10 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry10.place(x=555, y=70)

        self.entry11 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry11.place(x=580, y=70)

        self.entry12 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)
        #self.entry12.place(x=605, y=70)

        #list of entries
        self.listEntry = [self.entry12,self.entry11, self.entry10, self.entry9, self.entry8, self.entry7, self.entry6, self.entry5,
                          self.entry4, self.entry3, self.entry2, self.entry1]

        #Button for change binary number

        self.changeButton = customtkinter.CTkButton(master=self.frame, text="Change", command=self.GetNewNumber)
        #self.changeButton.place(x=385, y=120)


    def switch_event(self):

        print(self.switchVar.get())

    def Calculate(self):

        number = self.numberEntry.get()

        if self.ValidateNumber(number):

            self.decimal = self.converter.OctalToDecimal(number)
            self.binary = self.converter.OctalToBinary(number)
            self.hexa = self.converter.OctalToHexadecimal(number)

            self.SetNumberOnEntry(self.binary)

            self.decimalNumber.configure(text=str(self.decimal))
            self.binaryNumber.configure(text=str(self.binary))
            self.hexaNumber.configure(text=str(self.hexa))

        else:

            self.decimalNumber.configure(text="Mistake with the octal number")
            self.binaryNumber.configure(text="Mistake with the octal number")
            self.hexaNumber.configure(text="Mistake with the octal number")

            for i in self.listEntry:
                i.configure(placeholder_text="")



    def ValidateNumber(self, number):

        if len(number) <= 4:
            for i in number:
                if int(i) >= 8:
                    return False
            return True
        else:
            return False

    def SetNumberOnEntry(self, number):

        number = str(number)
        number = number[::-1]
        index = 0
        posx = 580
        posy = 70

        for i in self.listEntry:

            i.delete(0, END)

        for i in range(len(number)):

            self.listEntry[i].insert(0, number[i])
            self.listEntry[i].place(x=posx, y=posy)
            posx -= 25
            index += 1

        for i in range(index, len(self.listEntry)):

            self.listEntry[i].insert(0, "")
            self.listEntry[i].place(x=posx, y=posy)
            posx -= 25

        self.changeButton.place(x=385, y=120)

    def GetNewNumber(self):

        newNumber = ""
        tempList = self.listEntry[::-1]

        for i in tempList:

            newNumber += i.get()[0]

        self.octal = self.converter.BinaryToOctal(newNumber)
        self.numberEntry.delete(0, END)
        self.numberEntry.insert(0, self.octal)
        self.Calculate()




customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
GUI = GUI()
GUI.mainloop()