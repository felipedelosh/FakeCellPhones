"""
This is a conection beetwen interfaceUI fake cell pones and module

Invoke all methods and objs an d others configurations
"""

from module import MovilData


class Controller:
    def __init__(self):
        self.movilData = MovilData()
        self.tempSufijos = []

    def getIndicators(self, operator):
        """
        This return a sufijos 3XX claro, movistar, tigo, others
        """
        if operator == 0:
            return self.movilData.claroSub
        elif operator == 1:
            return self.movilData.movistarSub
        elif operator == 2:
            return self.movilData.tigoSub
        elif operator == 3:
            return self.movilData.otherSub

    def generateAllNumbers(self, operator, tipeOfCreate, tipeOfOutput, numberOfCell, nameOfSQLTable, operators):
        """
        This Generate all subfijos of numbers 3XX, 3XX
        1 -> Restart list of mobile data

        operator = 0 claro, 1 movistar, 2 tigo, 3 others
        tipeOfCreate : list(secuencial) or three(random)
        tipeOfOutPut : 0 txt, 1 excel, 2 sql
        numberOfCell : is a quantity of numbers to generate
        nameOfSQLTable = insert into TABLENAME
        operator = ALL, 3XX, 3XX, 3XX [this is a user subs to need]
        """
        self.movilData.restartSaves()
        self.movilData.modeToGenerate = tipeOfCreate
        self.movilData.modeToSave = tipeOfOutput
        self.movilData.tableNameSQL = nameOfSQLTable

        # Return all subs
        if operators == ['ALL']:
            operators = self.getAllSubs(operator)

        if tipeOfCreate == 0:
            self.movilData.generateAList(operators, numberOfCell)
        else:
            self.movilData.generateARandomNumbers(operators, numberOfCell)

        self.movilData.saveToHDD()


    def getAllSubs(self, operator):
        return self.movilData.getOperator(operator)
