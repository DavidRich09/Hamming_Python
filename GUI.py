from tkinter import *
import customtkinter
from Converter import Converter
from graphic import Graphic

# need custom tkinters for this to work
# pip3 install customtkinter
# documentation: https://github.com/TomSchimansky/CustomTkinter

class Table:

    def __init__(self, root, total_rows, total_columns, lst, size):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                current_size = 4

                if (len(lst[i][j]) > 4):
                    current_size = len(lst[i][j])

                self.e = Entry(root, width=current_size, fg='black',
                               font=('Consolas', size, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.delete(0, END)
                self.e.insert(END, lst[i][j])


class Code_Hamming:

    def __init__(self):
        self.bit = '0'
        self.InPar = False
        self.p = [[3, 5, 7, 9, 11, 13, 15, 17], [3, 6, 7, 10, 11, 14, 15], [5, 6, 7, 12, 13, 14, 15],
                  [9, 10, 11, 12, 13, 14, 15], [17]]
        self.hambit = '0'

    def Obtener_dato(self, num):
        self.bit = num

    def calcRedundantBits(self, m):
        for i in range(m):
            if (2 ** i >= m + i + 1):
                return i

    def posRedundantBits(self, data, r):

        # Redundancy bits are placed at the positions
        # which correspond to the power of 2.
        j = 0
        k = 0
        m = len(data)
        res = ''

        # If position is power of 2 then insert '0'
        # Else append the data
        for i in range(1, m + r + 1):
            if (i == 2 ** j):
                res = 'N' + res
                j += 1
            else:
                res = data[k] + res
                k += 1

        # The result is reversed since positions are
        # counted backwards. (m + r+1 ... 1)
        return res[::-1]

    def checkbits(self, paritybits, bitlist):

        cant1s = 0

        for i in paritybits:
            if bitlist[i - 1] == '1':
                cant1s += 1

        return cant1s

    def calcBitParidad(self, paridad):

        self.InPar = paridad

        # Calculate the no of Redundant Bits Required
        m = len(self.bit)
        # print(m)
        r = self.calcRedundantBits(m)
        # print(r)

        # Determine the positions of Redundant Bits
        self.hambit = self.posRedundantBits(self.bit, r)
        # print(self.hambit)

        paritybit = 0

        bitlist = list(self.hambit)

        while paritybit < len(self.p):

            cant1s = self.checkbits(self.p[paritybit], bitlist)

            if self.InPar:
                if cant1s % 2 == 0:
                    bitlist[2 ** paritybit - 1] = '1'
                else:
                    bitlist[2 ** paritybit - 1] = '0'

                # print(cant1s)
            else:
                if cant1s % 2 == 0:
                    bitlist[2 ** paritybit - 1] = '0'
                else:
                    bitlist[2 ** paritybit - 1] = '1'

                # print(cant1s)

            paritybit += 1

        # print(bitlist)
        return bitlist

    def verBitParidad(self, binary, evenParity):

        verificationlist = [[], [], [], [], []]
        errorPosition = []
        bitlist = binary

        paritybit = 0

        while paritybit < 5:

            amountOf1s = self.checkbits(self.p[paritybit], bitlist)

            if evenParity:
                if amountOf1s % 2 == 0:
                    if bitlist[2 ** paritybit - 1] != '1':
                        verificationlist[paritybit] = ['     Error    ', '1']
                    else:
                        verificationlist[paritybit] = ['   Correcto   ', '0']
                else:
                    if bitlist[2 ** paritybit - 1] != '0':
                        verificationlist[paritybit] = ['     Error    ', '1']
                    else:
                        verificationlist[paritybit] = ['   Correcto   ', '0']
            else:
                if amountOf1s % 2 == 0:
                    if bitlist[2 ** paritybit - 1] != '0':
                        verificationlist[paritybit] = ['     Error    ', '1']
                    else:
                        verificationlist[paritybit] = ['   Correcto   ', '0']
                else:
                    if bitlist[2 ** paritybit - 1] != '1':
                        verificationlist[paritybit] = ['     Error    ', '1']
                    else:
                        verificationlist[paritybit] = ['   Correcto   ', '0']
            paritybit += 1

        for i in verificationlist:
            errorPosition.append(i[1])

        errorPosition.reverse()

        errornum = ''.join(errorPosition)

        errornum = int(errornum, 2)

        return (verificationlist, errornum)


class GUI(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # create a window
        self.newNumber = []
        self.geometry(f"{1105}x{600}")
        self.title("Hamming Code")
        self.resizable(False, False)

        # create a converter object
        self.converter = Converter()
        self.hamming = Code_Hamming()

        self.paridad = False
        self.bipolar = False

        # main frame
        self.frame = customtkinter.CTkFrame(master=self.master, width=1105, height=600)
        self.frame.place(x=0, y=0)

        # HammingGeneratorTable frame
        self.tableHammingGenerator = customtkinter.CTkFrame(master=self.master, width=400, height=200)
        self.tableHammingGenerator.place(x=325, y=75)

        # HammingGeneratorVerification frame
        self.tableHammingVerification = customtkinter.CTkFrame(master=self.master, width=400, height=200)
        self.tableHammingVerification.place(x=150, y=350)

        # number entry
        self.numberEntry = customtkinter.CTkEntry(master=self.frame, placeholder_text="Introducir numero")
        self.numberEntry.place(x=10, y=10)

        # entry number button
        self.numberButton = customtkinter.CTkButton(master=self.frame, text="Calcular", command=self.Calculate)
        self.numberButton.place(x=160, y=10)

        #generate Hamming code
        self.GnrHamButton = customtkinter.CTkButton(master=self.frame, text="Generar Hamming", command=self.generar)
        self.GnrHamButton.place(x=450, y=10)

        # generate converter table with labels
        self.label = customtkinter.CTkLabel(master=self.frame, text="Tabla de conversion")
        self.label.place(x=0, y=50)
        self.label = customtkinter.CTkLabel(master=self.frame,
        text="Tabla 1 Calculo de los bits de paridad en el c??digo Hamming")
        self.label.place(x=510, y=45)

        self.label = customtkinter.CTkLabel(master=self.frame,
        text="Tabla 2 Verificaci??n de los bits de paridad con el c??digo Hamming")
        self.label.place(x=510, y=320)

        self.labelErrorNumber = customtkinter.CTkLabel(master=self.frame,
        text="")
        self.labelErrorNumber.place(x=510, y=500)

        self.decimal = customtkinter.CTkLabel(master=self.frame, text="Decimal")
        self.decimal.place(x=0, y=70)

        self.decimalNumber = customtkinter.CTkLabel(master=self.frame, text="")
        self.decimalNumber.place(x=130, y=70)

        self.binary = customtkinter.CTkLabel(master=self.frame, text="Binario")
        self.binary.place(x=0, y=90)

        self.binaryNumber = customtkinter.CTkLabel(master=self.frame, text="")
        self.binaryNumber.place(x=130, y=90)

        self.hexa = customtkinter.CTkLabel(master=self.frame, text="Hexadecimal")
        self.hexa.place(x=0, y=110)

        self.hexaNumber = customtkinter.CTkLabel(master=self.frame, text="")
        self.hexaNumber.place(x=130, y=110)

        # Switch to parity

        self.switchVar = StringVar(value="on")
        self.switchVar = customtkinter.CTkSwitch(master=self.frame, text="Paridad par", command=self.switch_event,
                                                 variable=self.switchVar, onvalue="On", offvalue="Off")
        self.switchVar.place(x=310, y=15)

        # Switch to bipolar
        self.switchVar2 = StringVar(value="on")
        self.switchVar2 = customtkinter.CTkSwitch(master=self.frame, text="Bipolar", command=self.switch_event2,
                                                    variable=self.switchVar2, onvalue="On", offvalue="Off")
        self.switchVar2.place(x=310, y=50)

        # entry for each number in binary table in total is 11 numbers

        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry3 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry4 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry5 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry6 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry7 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry8 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry9 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry10 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry11 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry12 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry13 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry14 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry15 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry16 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)

        self.entry17 = customtkinter.CTkEntry(master=self.frame, placeholder_text="", width=5)


        # list of entries
        self.listEntry = [self.entry17,self.entry16,self.entry15,self.entry14,self.entry13,self.entry12, self.entry11, self.entry10, self.entry9, self.entry8, self.entry7, self.entry6,
                          self.entry5,self.entry4, self.entry3, self.entry2, self.entry1]

        # Button for change binary number

        self.changeButton = customtkinter.CTkButton(master=self.frame, text="Verificar", command=self.VerifyNewNumber)
        # self.changeButton.place(x=385, y=120)


    def switch_event(self):

        if self.switchVar.get() == "On":

            self.paridad = True

        else:

            self.paridad = False

        print(self.paridad)


    def switch_event2(self):

        if self.switchVar2.get() == "On":

            self.bipolar = True

        else:

            self.bipolar = False

        print(self.bipolar)


    def Calculate(self):

        number = self.numberEntry.get()

        if self.ValidateNumber(number):

            self.decimal = self.converter.OctalToDecimal(number)
            self.binary = self.converter.OctalToBinary(number)
            self.hexa = self.converter.OctalToHexadecimal(number)

            self.binary = str(self.binary)
            self.binary = "0" * (12 - len(self.binary)) + self.binary

            print("binary with zeros ", self.binary)

            self.decimalNumber.configure(text=str(self.decimal))
            self.binaryNumber.configure(text=str(self.binary))
            self.hexaNumber.configure(text=str(self.hexa))

            graphic = Graphic(self.binary, self.bipolar)
            graphic.Run()

        else:

            self.decimalNumber.configure(text="Error con el numero octal")
            self.binaryNumber.configure(text="Error con el numero octal")
            self.hexaNumber.configure(text="Error con el numero octal")

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

        number = number[::-1]
        index = 0
        posx = 800
        posy = 270

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

        self.changeButton.place(x=900, y=270)

    def GetNewNumber(self):

        self.newNumber= []
        tempList = self.listEntry[::-1]

        for i in tempList:
            if i.get() != "":
                self.newNumber.append(i.get()[0])

       #newNumber ser?? el nuevo n??mero binario que se modific?? por el usuario

    def ValidateChangeNumber(self):

        for i in self.listEntry:

            if i.get() != "":

                if int(i.get()) >= 1:
                    return True

        return False

    def VerifyNewNumber(self):

        self.GetNewNumber()
        self.verificarHamm(self.newNumber, self.tableHammingVerification, self.paridad)

    def generarHamm(self, binary, root, paridad):

        print("Generando codigo Hamming")
        self.hamming.Obtener_dato(binary)
        self.hammOutput = self.hamming.calcBitParidad(paridad)\

        self.SetNumberOnEntry(self.hammOutput)

        lista1 = [("                             ", "p1", "p2", "d1", "p3", "d2", "d3", "d4", "p4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "p5",
                  "d12"),
                  ("Palabra de datos sin paridad:", " ", " ", binary[0], " ", binary[1], binary[2], binary[3], " ",
                   binary[4], binary[5], binary[6],
                   binary[7], binary[8], binary[9], binary[10], " ", binary[11]),
                  ("             p1              ", self.hammOutput[0], " ", self.hammOutput[2], " ", self.hammOutput[4], "", self.hammOutput[6], " ", self.hammOutput[8],
                   " ", self.hammOutput[10],
                   " ", self.hammOutput[12], " ", self.hammOutput[14], " ", self.hammOutput[16]),
                  ("             p2              ", " ", self.hammOutput[1], self.hammOutput[2], " ", " ", self.hammOutput[5], self.hammOutput[6], " ", " ",
                   self.hammOutput[9], self.hammOutput[10],
                   " ", " ", self.hammOutput[13], self.hammOutput[14], " ", " "),
                  ("             p3              ", " ", " ", " ", self.hammOutput[3], self.hammOutput[4], self.hammOutput[5], self.hammOutput[6], " ", " ", " ", " ",
                   self.hammOutput[11],
                   self.hammOutput[12], self.hammOutput[13], self.hammOutput[14], " ", " "),
                  ("             p4              ", " ", " ", " ", " ", " ", " ", " ", self.hammOutput[7], self.hammOutput[8], self.hammOutput[9], self.hammOutput[10],
                   self.hammOutput[11],
                   self.hammOutput[12], self.hammOutput[13], self.hammOutput[14], " ", " "),
                  ("             p5              ", " ", " ", " ", " ", " ", " ", " ", "", "", "", "", "", "", "", "", self.hammOutput[15],
                   self.hammOutput[16]),
                  ("Palabra de datos con paridad:", self.hammOutput[0], self.hammOutput[1], self.hammOutput[2], self.hammOutput[3],
                   self.hammOutput[4], self.hammOutput[5],
                   self.hammOutput[6], self.hammOutput[7], self.hammOutput[8], self.hammOutput[9], self.hammOutput[10], self.hammOutput[11],
                   self.hammOutput[12], self.hammOutput[13], self.hammOutput[14], self.hammOutput[15], self.hammOutput[16])]

        tabla1 = Table(root, 8, 18, lista1, 10)
        self.GetNewNumber()

    def verificarHamm(self, binary, root, parity):

        print("Verificando codigo Hamming")

        hammingVerBits, hammingErrorPos = self.hamming.verBitParidad(binary, parity)

        lista2 = [("                          ", "p1", "p2", "d1", "p3", "d2", "d3", "d4", "p4", "d5", "d6", "d7", "d8", "d9", "d10", "d11", "p5",
                  "d12", "Prueba Paridad", "Bit de Paridad"),

                  ("Palabra de datos recibida:", binary[0], binary[1], binary[2], binary[3], binary[4], binary[5], binary[6], binary[7],
                   binary[8], binary[9], binary[10], binary[11], binary[12], binary[13],binary[14], binary[15], binary[16], "              ", "              "),

                  ("            p1            ", binary[0], " ", binary[2], " ", binary[4], "", binary[6], " ", binary[8], " ", binary[10],
                   " ", binary[12], " ", binary[14], " ", binary[16], hammingVerBits[0][0], "      " + hammingVerBits[0][1] + "       "),

                  ("            p2            ", " ", binary[1], binary[2], " ", " ", binary[5], binary[6], " ", " ", binary[9], binary[10],
                   " ", " ", binary[13], binary[14], " ", " ", hammingVerBits[1][0], "      " + hammingVerBits[1][1] + "       "),

                  ("            p3            ", " ", " ", " ", binary[3], binary[4], binary[5], binary[6], " ", " ", " ", " ", binary[11],
                   binary[12], binary[13], binary[14], " ", " ", hammingVerBits[2][0], "      " + hammingVerBits[2][1] + "       "),

                  ("            p4            ", " ", " ", " ", " ", " ", " ", " ", binary[7], binary[8], binary[9], binary[10], binary[11],
                   binary[12], binary[13], binary[14], " ", " ", hammingVerBits[3][0], "      " + hammingVerBits[3][1] + "       "),

                  ("            p5            ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", binary[15],
                   binary[16], hammingVerBits[4][0], "      " + hammingVerBits[4][1] + "       ")]

        tabla2 = Table(root, 7, 20, lista2, 10)

        if (hammingErrorPos != 0):
            print(hammingErrorPos)
            if(self.converter.BinaryToDecimal(hammingErrorPos) > 17):
                self.labelErrorNumber.configure(text="Error detectado. No es posible verificar su posici??n")
            else:
                self.labelErrorNumber.configure(text="Se ha encontrado un error el bit: " + str(hammingErrorPos))
        else:
                self.labelErrorNumber.configure(text="No se han detectado errores")


    def generar(self):
        num = "110101100101"
        self.generarHamm(self.binary, self.tableHammingGenerator, self.paridad)
        self.verificarHamm(self.newNumber, self.tableHammingVerification, self.paridad)
        print("Generado")


customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
GUI = GUI()
GUI.mainloop()