"""
@felipedelosh
This is a UI of fake data of mobiles colombia
"""

from tkinter import *
from tkinter import ttk
from controller import *

class Software:
    def __init__(self):
        # Principal Display
        self.mainScreem = Tk()
        # painter buttons text and others
        self.canvas = Canvas(self.mainScreem, height=480, width=720, bg='snow')
        # Imgages to show
        self.imgBackGround = PhotoImage(file='img/bg.gif')
        self.imgClaro = PhotoImage(file='img/claro.gif')
        self.imgMovistar = PhotoImage(file='img/movistar.gif')
        self.imgTigo = PhotoImage(file='img/tigo.gif')
        self.imgOthersOP = PhotoImage(file='img/otros.gif')
        #Buttons
        self.btnInterfaceClaro = Button(self.canvas, image= self.imgClaro, command = self.launchInterfaceClaro)
        self.btnInterfaceMovistar = Button(self.canvas, image= self.imgMovistar, command = self.launchInterfaceMovistar)
        self.btnInterfaceTigo = Button(self.canvas, image= self.imgTigo, command = self.launchInterfaceTigo)
        self.btnInterfaceOthersOP = Button(self.canvas, image= self.imgOthersOP, command = self.launchInterfaceOtherOP)
        # Launchers 
        self.titleLauncher = ""
        # This is a operator to generate 0 -> claro 1 -> movistar 2 -> tigo 3 -> others
        self.controlOperatorGenerate = 0
        self.controlGenerateSecuencial = IntVar()
        self.controlGenerateRandom = IntVar()
        self.listOfComboBoxIndicadores = []
        self.indexComboBoxSubs = 0
        self.valueComboBoxSubs = StringVar()
        self.indexComboBoxOutput = 0
        self.valueComboBoxOutput = StringVar()
        self.controlNumberOfCellNumbers = StringVar() # constains a information about numberscell to generate
        self.numberOfCellNumbers = 0
        self.sqlTableName = ""
        # COMBOBOX IS GENERATE IN LAUCHER
        #Controller ALL
        self.controller = Controller()
        #Configure, paint and show
        self.configureAndLaunchView()

    def configureAndLaunchView(self):
        self.mainScreem.title("Fake Movil data by Loko")
        self.mainScreem.geometry("720x480")


        self.canvas.place(x=0, y=0)
        self.canvas.create_image(0, 0, image=self.imgBackGround, anchor=NW)
        self.btnInterfaceClaro.place(x=50, y=160)
        self.btnInterfaceMovistar.place(x=200, y=160)
        self.btnInterfaceTigo.place(x=350, y=160)
        self.btnInterfaceOthersOP.place(x=500, y=160)


        self.mainScreem.mainloop()

    def launchInterfaceClaro(self):
        self.titleLauncher = "CLARO fake data by loko"
        self.ControlOperatorGenerate = 0
        self.numberOfCellNumbers = 0
        self.getComboBoxOptions()
        self.genericLancher()

    def launchInterfaceMovistar(self):
        print('B')

    def launchInterfaceTigo(self):
        print('C')

    def launchInterfaceOtherOP(self):
        print('D')

    def genericLancher(self):
        # Graphic configuration an resize
        top = Toplevel()
        top.title(self.titleLauncher)
        top.geometry("500x300")
        lblGenrateWay = Label(top, text="Metodo para la generacio'n de numeros:")
        lblGenrateWay.place(x=20, y=20)
        # Chechk way to save
        chckList = Checkbutton(top, text="Secuencial", variable=self.controlGenerateSecuencial,
         onvalue=1, offvalue=0, command= self.chooseListOrRandom)
        chckList.place(x=250, y=20)
        chckRandom = Checkbutton(top, text="Random", variable=self.controlGenerateRandom,
         onvalue=1, offvalue=0, command= self.chooseListOrRandom)
        chckRandom.place(x=330, y=20)
        lblNumbersOfCellNumbersToGenerate = Label(top, text="Cuantos Numeros desea generar: ")
        lblNumbersOfCellNumbersToGenerate.place(x=50, y=60)
        txtNumbersOfCellToGenrate = Entry(top, textvariable=self.controlNumberOfCellNumbers)
        txtNumbersOfCellToGenrate.place(x=250, y=60)
        lblselectSub = Label(top, text="seleccione sufijo de operador movil: ")
        lblselectSub.place(x=50, y=100)
        comboxSubs = ttk.Combobox(top, state='readonly', textvariable=self.valueComboBoxSubs)
        comboxSubs['values'] = self.listOfComboBoxIndicadores
        comboxSubs.place(x=250, y=100)
        lblSelectOutputformat = Label(top, text='seleccione formato de salida: ')
        lblSelectOutputformat.place(x=60, y=160)
        comboxOutputFormat = ttk.Combobox(top, state='readonly', textvariable=self.valueComboBoxOutput)
        comboxOutputFormat['values'] = ['texto plano', 'Excel', 'SQL script']
        comboxOutputFormat.place(x=250, y=160)

        btnGenerate = Button(top, text="GENERATE", command=self.validategenerateOutputData)
        btnGenerate.place(x=220, y=200)

    def chooseListOrRandom(self):
        """
        This control in all the launcher the way that is create.
        If you choose any you disable other

        --This need be better
        """
        if self.controlGenerateSecuencial.get() == 1:
            self.controlGenerateRandom.set(0)
        else:
            if self.controlGenerateRandom.get() == 1:
                self.controlGenerateSecuencial.set(0)

    def getComboBoxOptions(self):
        self.listOfComboBoxIndicadores = []
        if self.ControlOperatorGenerate == 0:
            # apend all options
            self.listOfComboBoxIndicadores.append("ALL")
            for i in self.controller.getIndicatorsClaro():
                self.listOfComboBoxIndicadores.append(str(i))


    def validategenerateOutputData(self):
        # Get secuencial of list
        """
        1 - Validate if configure a method to create a numbers
        2 - Valitade if input a numbers to cellnumbers be create
        3 - valitate a combo box
        4 - if you insert sqlscript launch a view with tablename
        """
        if (self.controlGenerateSecuencial.get() == 1 and self.controlGenerateRandom.get() == 0) or (self.controlGenerateSecuencial.get() == 0 and self.controlGenerateRandom.get() == 1):
            if self.validateCellNumbersInput():
                if self.validateComboBox():
                    if self.valueComboBoxOutput.get() == 'SQL script':
                        w = Toplevel()
                        w.title('Nombre de la tabla SQL')
                        w.geometry("300x150")
                        label = Label(w, text='Por favor ingrese el nombre de la tabla')
                        label.pack()
                        txt = Entry(w)
                        txt.pack()
                        btnGenerate = Button(w, text='OK', command= lambda: self.setSQLtableName(w, txt))
                        btnGenerate.pack()

                else:
                    self.alertSMS('Error', 'Verifique las opciones de sufijo y salida de datos')
            else:
                self.alertSMS('Error', 'Por favor ingrese el numero de telefonos celulares que desea generar')

        if self.controlGenerateSecuencial.get() == 0 and self.controlGenerateRandom.get() == 0:
            self.alertSMS('Error', 'Por favor seleccione el metodo de generacio.n: random o secuencial')


    def alertSMS(self, title, txt):
        """
        This is a output message for the user, only show a text in toplevel screem
        """
        w = Toplevel()
        w.title(title)
        sms = Message(w, text=txt)
        sms.pack()
        btnClocse = Button(w, text='OK', command=w.destroy)
        btnClocse.pack()


    def validateCellNumbersInput(self):
        try:
            temp = int(self.controlNumberOfCellNumbers.get())
            self.numberOfCellNumbers = temp
            return True
        except:
            return False

    def validateComboBox(self):
        print(self.valueComboBoxOutput.get(), self.valueComboBoxSubs.get())
        return self.valueComboBoxOutput.get() != "" and self.valueComboBoxSubs.get() != ""

    def setSQLtableName(self, topl, entryTxt):
        self.sqlTableName = entryTxt.get()
        if len(self.sqlTableName.strip()) > 0:
            topl.destroy()



s = Software()