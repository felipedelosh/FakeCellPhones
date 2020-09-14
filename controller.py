"""
This is a conection beetwen interfaceUI fake cell pones and module

Invoke all methods and objs an d others configurations
"""

from module import MovilData


class Controller:
    def __init__(self):
        self.movilData = MovilData()
        self.tempSufijos = []


    def getIndicatorsClaro(self):
        return self.movilData.claroSub

    def generateAllNumbers(self, operator, tipeOfCreate, tipeOfOutput, numberOfCell, nameOfSQLTable, operators):
        """
        This Generate all subfijos of numbers 3XX, 3XX
        operator = 0 claro, 1 movistar, 2 tigo, 3 others
        tipeOfCreate : list(secuencial) or three(random)
        tipeOfOutPut : 0 txt, 1 excel, 2 sql
        numberOfCell : is a quantity of numbers to generate
        nameOfSQLTable = insert into TABLENAME
        operator = ALL, 3XX, 3XX, 3XX [this is a user subs to need]
        """
        print('Entra')
        self.movilData.modeToGenerate = tipeOfCreate
        self.movilData.modeToSave = tipeOfOutput
        self.movilData.tableNameSQL = nameOfSQLTable

        print(tipeOfOutput)
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
