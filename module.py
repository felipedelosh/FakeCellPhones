"""
@felipedelosh
9/12/2020

This is a module of Fake data movil by loko

* Save a numbers.txt, numbers.xlxs, numbers.sql

"""

"""
This program work with random data
Not accept duplicate numbers then i need save a numbers
in a three to be fast and unique
"""
import random
import os

class Node(object):
    def __init__(self, left, data, rigth):
        self.left = None
        self.data = None
        self.rigth = None

class BinaryThree():
    def __init__(self):
        self.root = Node(None, None, None)
        self.numberOfNodes = 0
        self.dataToList = []

    def addNode(self, data):
        if self.root.data == None:
            self.root.data = data
            self.numberOfNodes = 1
        else:
            self._addNode(self.root ,data)

    def _addNode(self, root, data):
        # No Acept duplicate values
        if root.data == data:
            pass
        else:
            if root.data > data:
                if root.left is None:
                    root.left = Node(None, None, None)
                    root.left.data = data
                    self.numberOfNodes = self.numberOfNodes + 1
                else:
                    self._addNode(root.left, data)
            else:
                if root.rigth is None:
                    root.rigth = Node(None, None, None)
                    root.rigth.data = data
                    self.numberOfNodes = self.numberOfNodes + 1
                else:
                    self._addNode(root.rigth, data)

    def show(self):
        self._show(self.root)

    def _show(self, root):
        if(root is not None):
            self._show(root.left)
            self.dataToList.append(root.data)
            self._show(root.rigth)


class MovilData:
    def __init__(self):
        # To save a ramdom numbers is temp bcos then insert into self.listOfNumbers
        self.listToRamdon = BinaryThree()
        # To save a secuencial numbers
        self.listOfNumbers = []
        # Controle a mode to generate a information 
        # 0 -> secuential, 1 -> ramdom
        self.modeToGenerate = 0
        self.claroSub = [310, 311, 312, 313, 314, 320, 321, 322, 323]
        self.movistarSub = [315, 316, 317, 318]
        self.tigoSub = [300, 301, 302, 304, 305]
        self.virginSub = [319]
        self.otherSub = [303, 304, 305, 350, 351]
        #To save mode: 0 -> txt 1 -> .xlsx 2-> .sql
        self.modeToSave = 0 
        # To save a file
        self.pathProject = str(os.path.dirname(os.path.abspath(__file__)))
        # To save SQL
        self.tableNameSQL = ""

    def getOperator(self, operator):
        if operator == 0:
            return self.claroSub
        elif operator == 1:
            return self.movistarSub
        elif operator == 2:
            return self.tigoSub
        else:
            return self.otherSub

    def generateAList(self, operatorSubs, total):
        """
        This methos saved a secuentual numbers in self.listOfNumbers trougth self.saveBumberInList
        """
        self.modeToGenerate = 0
        for i in range(0, total):
            operator = operatorSubs[random.randint(0, len(operatorSubs)-1)]
            self.saveNumberInList(operator, i)


    def saveNumberInList(self, opetator, number):
        """
        apeend a number in self.listOfNumbers

        AAA + 7 numbers
        sometimes i need to fill with zero
        for example 99 -> AAA 000 0099
        """
        self.listOfNumbers.append(self.formatToNumber(str(opetator) + self.fillWithZero(number) + str(number)))

    def generateARandomNumbers(self, operatorSubs, total):
        self.modeToGenerate = 1
        while(self.listToRamdon.numberOfNodes < total):
            operator = operatorSubs[random.randint(0, len(operatorSubs)-1)]
            number = random.randint(0, 9999999)
            cellNumber = self.formatToNumber(str(operator) + self.fillWithZero(number) + str(number))
            self.listToRamdon.addNode(cellNumber)


    def formatToNumber(self, strData):
        """
        In a String with AAA + 7 numbers 
        this return a int value
        """
        return int(strData)

    def saveToHDD(self):
        """
        this save a output(txt, excel, sql) in hard drive
        1 - verify if data is in list or three, if this in three need to cast a list
        controller a mode of create
        2 - try to save, 
        """
        if self.modeToGenerate == 0:
            pass
        else:
            self.listToRamdon.show()
            self.listOfNumbers = self.listToRamdon.dataToList
        
        try:

            txt = ""
            
            if self.modeToSave == 0:
                for i in self.listOfNumbers:
                    txt = txt + str(i) + "\n"
                file = open(self.pathProject + "\\numbers.txt", "w")
                file.write(txt)
                file.close()

            if self.modeToSave == 1:
                for i in self.listOfNumbers:
                    txt = txt + str(i) + ";\n"

                file = open(self.pathProject + "\\numbers.xlsx", "w")
                file.write(txt)
                file.close()

            if self.modeToSave == 2:
                con = 0
                for i in self.listOfNumbers:
                    txt = txt + "insert into " + self.tableNameSQL + " values(" +str(con)+ "," + str(i) + ");\n"
                    con = con + 1

                file = open(self.pathProject + "\\numbers.sql", "w")
                file.write(txt)
                file.close()


        except:
            pass


    def fillWithZero(self, number):
        """
        1 -> AAA0000001
        2 -> AAA0000002
        9 -> AAA0000009
        10-> AAA0000010
        99-> AAA0000099 
        """
        numberOFZeros = 7 - len(str(number))
        zeros = ""
        for i in range(0, numberOFZeros):
            zeros = zeros + "0"
        
        return zeros


    def restartSaves(self):
        """
        Delete all values in list and three
        """
        self.listOfNumbers = []
        self.listToRamdon = BinaryThree()