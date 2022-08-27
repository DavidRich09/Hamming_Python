class Converter:

    def __init__(self):

        pass

    def BaseToDecimal(self, number, base): #recive a number and a base of the number and return the decimal value of the number
        newNumber = 0

        number = str(number)
        number = number[::-1]

        for i in range(0, len(number),1):

            if ord(number[i]) >= 65: #
                newNumber += (ord(number[i]) - 55) * pow(base, i)
            else:
                newNumber += (ord(number[i]) - 48) * pow(base, i)

        return newNumber

    def DecimalToBase(self, number, base):

        newNumber = ""

        number = int(number)

        while True:

            residue = number % base

            number -= residue

            if residue >= 10:
                residue += 55
                newNumber += str(chr(int(residue)))
            else:
                newNumber += str(int(residue))

            number = number / base

            if number == 0:

                break

        newNumber = newNumber[::-1]

        return newNumber

    def OctalToDecimal(self, number):

        return self.BaseToDecimal(number, 8)

    def OctalToBinary(self, number):

        return self.DecimalToBase(self.OctalToDecimal(number), 2)

    def OctalToHexadecimal(self, number):

        return self.DecimalToBase(self.OctalToDecimal(number), 16)

