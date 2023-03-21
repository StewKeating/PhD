import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

class PopUp():
    
    def __init__(self, parent):
        super().__init__()
        root.columnconfigure(0, weight=1, minsize=55)
        root.rowconfigure(0, weight=1, minsize=55)
        self.num = 0
        self.Label1 = tk.Text(parent, width=50, height=3)
        self.Label1.insert(0.0,f'{MainDF.iloc[self.num,24]}')
        self.Label1.grid(row=0, column=0,rowspan=2)
        #self.Label1.place(height=50, width=350)

        self.Label2 = tk.Text(parent, width=50, height=3)
        self.Label2.insert(0.0,f'{MainDF.iloc[self.num,25]}')
        self.Label2.grid(row=2, column=0, rowspan=2)
        #self.Label2.place(height=200, width=350)

        self.Label3 = tk.Text(parent, width=50, height=3)
        self.Label3.insert(0.0,f'{MainDF.iloc[self.num,26]}')
        self.Label3.grid(row=4, column=0, rowspan=2)
        #self.Label3.place(height=50, width=300)

        self.Label4 = tk.Text(parent, width=50, height=3)
        self.Label4.insert(0.0,f'{MainDF.iloc[self.num,27]}')
        self.Label4.grid(row=6, column=0, rowspan=2)
        #self.Label4.place(height=50, width=300)


        self.LabelNum = tk.Label(parent, text=f'{self.num}')
        self.LabelNum.grid(row=12, column=2)
       
        self.Label5 = tk.Label(parent, text='Mystery Trait 1')
        self.Label5.grid(row=0, column=1)
        self.Label5 = tk.Label(parent, text='Mystery Trait 2')
        self.Label5.grid(row=2, column=1)
        self.Label5 = tk.Label(parent, text='Mystery Trait 3')
        self.Label5.grid(row=4, column=1)
        self.Label5 = tk.Label(parent, text='Mystery Trait 4')
        self.Label5.grid(row=6, column=1)
        self.Label5 = tk.Label(parent, text='Mystery Trait 5')
        self.Label5.grid(row=8, column=1)
        self.Label5 = tk.Label(parent, text='Mystery Trait 1 No.')
        self.Label5.grid(row=0, column=2)
        self.Label5 = tk.Label(parent, text='Mystery Trait 2 No.')
        self.Label5.grid(row=2, column=2)
        self.Label5 = tk.Label(parent, text='Mystery Trait 3 No.')
        self.Label5.grid(row=4, column=2)
        self.Label5 = tk.Label(parent, text='Mystery Trait 4 No.')
        self.Label5.grid(row=6, column=2)
        self.Label5 = tk.Label(parent, text='Mystery Trait 5 No.')
        self.Label5.grid(row=8, column=2)
        #self.Label2 = tk.Label(parent, text='Attractiveness')
        #self.Label2.grid(row=11, column=1)

        self.RowSkip = tk.Entry(parent)
        self.RowSkip.grid(row=13, column=1)
        SkpBtn = tk.Button(parent,text='RowSkip',command=self.SkpPress).grid(row=13, column=2)

        self.MT1 = tk.Entry(parent)
        self.MT1.grid(row=1,column=1)
        self.MT2 = tk.Entry(parent)
        self.MT2.grid(row=3,column=1)
        self.MT3 = tk.Entry(parent)
        self.MT3.grid(row=5,column=1)
        self.MT4 = tk.Entry(parent)
        self.MT4.grid(row=7,column=1)
        self.MT5 = tk.Entry(parent)
        self.MT5.grid(row=9,column=1)

        self.MT1n = tk.Entry(parent)
        self.MT1n.grid(row=1,column=2)
        self.MT2n = tk.Entry(parent)
        self.MT2n.grid(row=3,column=2)
        self.MT3n = tk.Entry(parent)
        self.MT3n.grid(row=5,column=2)
        self.MT4n = tk.Entry(parent)
        self.MT4n.grid(row=7,column=2)
        self.MT5n = tk.Entry(parent)
        self.MT5n.grid(row=9,column=2)

        self.MT1.insert(0,f'{MainDF.iloc[self.num,45]}')
        self.MT1n.insert(0,f'{MainDF.iloc[self.num,46]}')
        self.MT2.insert(0,f'{MainDF.iloc[self.num,47]}')
        self.MT2n.insert(0,f'{MainDF.iloc[self.num,48]}')
        self.MT3.insert(0,f'{MainDF.iloc[self.num,49]}')
        self.MT3n.insert(0,f'{MainDF.iloc[self.num,50]}')
        self.MT4.insert(0,f'{MainDF.iloc[self.num,51]}')
        self.MT4n.insert(0,f'{MainDF.iloc[self.num,52]}')
        self.MT5.insert(0,f'{MainDF.iloc[self.num,53]}')
        self.MT5n.insert(0,f'{MainDF.iloc[self.num,54]}')

               
        PshBtn = tk.Button(parent,text='Save+Next',command=self.BtnPress).grid(row=12, column=1)

    def SkpPress(self):
        print(f'{self.num}')
        x=self.RowSkip.get()
        print(x)
        print(type(x))
        self.num = int(self.RowSkip.get())
        print(f'{self.num}')
        #self.num = int(self.RowSkip.get())
        self.LabelNum["text"] = f'Row number = {self.num}'


        self.Label1.delete(0.0,'end')
        self.Label2.delete(0.0,'end')
        self.Label3.delete(0.0,'end')
        self.Label4.delete(0.0,'end')

        self.MT1.delete(0,'end')
        self.MT1n.delete(0,'end')
        self.MT2.delete(0,'end')
        self.MT2n.delete(0,'end')
        self.MT3.delete(0,'end')
        self.MT3n.delete(0,'end')
        self.MT4.delete(0,'end')
        self.MT4n.delete(0,'end')
        self.MT5.delete(0,'end')
        self.MT5n.delete(0,'end')
        
        self.Label1.insert(0.0,f'{MainDF.iloc[self.num,24]}')
        self.Label2.insert(0.0,f'{MainDF.iloc[self.num,25]}')
        self.Label3.insert(0.0,f'{MainDF.iloc[self.num,26]}')
        self.Label4.insert(0.0,f'{MainDF.iloc[self.num,27]}')

        self.MT1.insert(0,f'{MainDF.iloc[self.num,45]}')
        self.MT1n.insert(0,f'{MainDF.iloc[self.num,46]}')
        self.MT2.insert(0,f'{MainDF.iloc[self.num,47]}')
        self.MT2n.insert(0,f'{MainDF.iloc[self.num,48]}')
        self.MT3.insert(0,f'{MainDF.iloc[self.num,49]}')
        self.MT3n.insert(0,f'{MainDF.iloc[self.num,50]}')
        self.MT4.insert(0,f'{MainDF.iloc[self.num,51]}')
        self.MT4n.insert(0,f'{MainDF.iloc[self.num,52]}')
        self.MT5.insert(0,f'{MainDF.iloc[self.num,53]}')
        self.MT5n.insert(0,f'{MainDF.iloc[self.num,54]}')
        
    def BtnPress(self):
        MainDF.iloc[self.num,24] = self.Label1.get(0.0,'end')
        MainDF.iloc[self.num,25] = self.Label2.get(0.0,'end')
        MainDF.iloc[self.num,26] = self.Label3.get(0.0,'end')
        MainDF.iloc[self.num,27] = self.Label4.get(0.0,'end')

        MainDF.iloc[self.num,45] = self.MT1.get()
        MainDF.iloc[self.num,46] = self.MT1n.get()
        MainDF.iloc[self.num,47] = self.MT2.get()
        MainDF.iloc[self.num,48] = self.MT2n.get()
        MainDF.iloc[self.num,49] = self.MT3.get()
        MainDF.iloc[self.num,50] = self.MT3n.get()
        MainDF.iloc[self.num,51] = self.MT4.get()
        MainDF.iloc[self.num,52] = self.MT4n.get()
        MainDF.iloc[self.num,53] = self.MT5.get()
        MainDF.iloc[self.num,54] = self.MT5n.get()
        #MainDF.iloc[self.num,56] = self.Attractiveness.get()
        MainDF.to_excel("PhD_Study1_V7.xlsx",sheet_name="sheet1",index=False)
        self.num+=1

        self.Label1.delete(0.0,'end')
        self.Label2.delete(0.0,'end')
        self.Label3.delete(0.0,'end')
        self.Label4.delete(0.0,'end')

        self.MT1.delete(0,'end')
        self.MT1n.delete(0,'end')
        self.MT2.delete(0,'end')
        self.MT2n.delete(0,'end')
        self.MT3.delete(0,'end')
        self.MT3n.delete(0,'end')
        self.MT4.delete(0,'end')
        self.MT4n.delete(0,'end')
        self.MT5.delete(0,'end')
        self.MT5n.delete(0,'end')
        
        self.Label1.insert(0.0,f'{MainDF.iloc[self.num,24]}')
        self.Label2.insert(0.0,f'{MainDF.iloc[self.num,25]}')
        self.Label3.insert(0.0,f'{MainDF.iloc[self.num,26]}')
        self.Label4.insert(0.0,f'{MainDF.iloc[self.num,27]}')

        self.MT1.insert(0,f'{MainDF.iloc[self.num,45]}')
        self.MT1n.insert(0,f'{MainDF.iloc[self.num,46]}')
        self.MT2.insert(0,f'{MainDF.iloc[self.num,47]}')
        self.MT2n.insert(0,f'{MainDF.iloc[self.num,48]}')
        self.MT3.insert(0,f'{MainDF.iloc[self.num,49]}')
        self.MT3n.insert(0,f'{MainDF.iloc[self.num,50]}')
        self.MT4.insert(0,f'{MainDF.iloc[self.num,51]}')
        self.MT4n.insert(0,f'{MainDF.iloc[self.num,52]}')
        self.MT5.insert(0,f'{MainDF.iloc[self.num,53]}')
        self.MT5n.insert(0,f'{MainDF.iloc[self.num,54]}')

pd.set_option("display.max_rows", None)
#pd.set_option("display.max_columns", None)
MainDF = pd.read_excel('PhD_Study1_V7.xlsx')

root = tk.Tk()
PopUp(root)
root.mainloop()

#MainDF.to_excel("PhD_Study1_V7.xlsx",sheet_name="sheet1",index=False)


