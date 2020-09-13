"""
This is a conection beetwen interfaceUI fake cell pones and module

Invoke all methods and objs an d others configurations
"""

from module import MovilData


class Controller:
    def __init__(self):
        self.movilData = MovilData()


    def getIndicatorsClaro(self):
        return self.movilData.claroSub