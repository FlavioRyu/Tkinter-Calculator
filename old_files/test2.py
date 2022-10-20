import numpy as np
import tkinter as tk


a = ['-', '1', '.', '2']
a = ''.join(a)
a = float(a)
print(a)
print(type(a))


    def equal_f(self):
        self.insert_operator('=')
        if self.mode == 'addition':
            for i in range(len(self.narray)-2):
                if self.narray[i] == '+':
                    continue
                self.result = self.narray[0] + self.narray[i+2]
                self.narray[0] = self.result
        if self.mode == 'subtraction':
            for i in range(len(self.narray)-2):
                if self.narray[i] == '-':
                    continue
                self.result = self.narray[0] - self.narray[i+2]
                self.narray[0] = self.result
        if self.mode == 'multiplication':
            for i in range(len(self.narray)-2):
                if self.narray[i] == '*':
                    continue
                self.result = self.narray[0] * self.narray[i+2]
                self.narray[0] = self.result
        if self.mode == 'division':
            try:
                for i in range(len(self.narray)-2):
                    if self.narray[i] == '/':
                        continue
                    self.result = self.narray[0] / self.narray[i+2]
                    self.narray[0] = self.result
            except:
                if self.negative:
                    self.result = '-'+u'\u221E'
                if not self.negative:
                    self.result = u'\u221E'
        self.text.insert(tk.END, self.result)
        # self.text.insert(tk.END, '{:.6f}'.format(self.result))

