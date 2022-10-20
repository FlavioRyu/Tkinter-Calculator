from tkinter import *
from tkinter import ttk


class Calculator(ttk.Frame):
    
    narray = []
    temp = []
        
    def __init__(self, master, title, matrix):
        ttk.Frame.__init__(self, master)
        self.master = master
        self.master.title(title)
        self.matrix = matrix
        self.textbox()
        self.buttons()
        
    def buttons(self):
        self.virtual = PhotoImage(width=1, height=1)
        i = 1; j = 0
        for row in self.matrix:
            for element in row: # create all buttons at once
                b = ttk.Button(self.master, text=element, width=100, height=100, 
                              image=self.virtual, compound='c', command = 
                              lambda a=element : self.function(a))
                b = b.grid(row=i, column=j)
                j += 1
            i += 1
            j = 0
        
    def textbox(self):
        self.text = Text(self.master, width=40, height=3, font=('Arial', 12))
        self.text.grid(row=0, columnspan=5)

    def insert_operator(self, operator):
        self.text.insert(ttk.END, ' ')
        self.text.insert(ttk.END, operator)
        self.text.insert(ttk.END, ' ')

    def function(self, symbol):
        # distinguish buttons between numbers and operators
        try:
            int(symbol)
            is_number = True
        except:
            is_number = False
        if is_number or symbol == '.' or symbol == '(-)':
            if symbol == '(-)': # for negative numbers
                self.temp.append('-')
                self.negative = True
            else:
                temp2 = []
                self.temp.append(symbol) # append value in the temp array
                self.number = ''.join(self.temp)
                self.text.delete(1.0, ttk.END)
                temp2 = self.narray[:]
                temp2.append(self.number)
                self.text.insert(ttk.END, temp2)
        elif not is_number:
            if symbol == 'C':
                self.text.delete(1.0, ttk.END)
                self.narray = []
                self.temp = []
                return
            # if symbol == 'DEL':
            #     self.narray = self.narray[0:len(self.narray)]
            self.narray.append(float(self.number))
            self.narray.append(symbol)
            self.temp = [] # reset temp array for next number
            if symbol == '=':
                self.test()

    def test(self):
        value = 0
        for i in range(0, len(self.narray)-2, 2):
            a = self.narray[i:i+3]
            if i != 0:
                a[0] = value
            value = self.calculate(a)
        self.result = value
        self.insert_operator('=')
        self.text.insert(ttk.END, self.result)
        
    def calculate(self, array):
        if array[1] == '+':
            result = array[0] + array[2]
        if array[1] == '-':
            result = array[0] - array[2]
        if array[1] == '*':
            result = array[0] * array[2]
        if array[1] == '/':
            result = array[0] / array[2]
        return result
