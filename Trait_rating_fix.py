#load each row column AA <- this is the order of all characteristics

#then AC, AD, AE, AF, AG, AH, AI, AJ, AK, AL, AM <- researcher traits ratings
#then AN, AO,AP,AQ,AR,AS,AT,AU,AV,AW,AX,AY,AZ,BA,BB,BC,BD,BE,BF,BG,BH,BI,BJ,BK,BL,BM <- self defined traits and the rating (most will be NULL)


#GUI LHS is AA in a text box that I can reorder myself
#GUI RHS is non-edit text of research traits and the self defined ones, to the right of that is the rating which is editable


#saves to a new excel file with AA being reordered

import pandas as pd
import tkinter as tk

g = pd.read_excel('PhD_Study1_V8.xlsx','sheet1')
d = g.columns.tolist()
print(d[28])
'''
print(g.iloc[0,26])# all characteristics from row
print(g.iloc[0,28])#Competence
print(g.iloc[0,29])#Integrity
print(g.iloc[0,30])#Trustworthiness
print(g.iloc[0,31])#Charisma
print(g.iloc[0,32])#Empathy
print(g.iloc[0,33])#Warmth
print(g.iloc[0,34])#Expertise
print(g.iloc[0,35])#Similarity
print(g.iloc[0,36])#Familiarity
print(g.iloc[0,37])#Likeability
print(g.iloc[0,38])#Attractiveness

print(g.iloc[0,39])#self character 1
print(g.iloc[0,40])#self rating 1
print(g.iloc[0,41])#self character 2
print(g.iloc[0,42])#self rating 2
print(g.iloc[0,43])#self character 3
print(g.iloc[0,44])#self rating 3
print(g.iloc[0,45])#self character 4
print(g.iloc[0,46])#self rating 4
print(g.iloc[0,47])#self character 5
print(g.iloc[0,48])#self rating 5
print(g.iloc[0,49])#self character 6
print(g.iloc[0,50])#self rating 6
print(g.iloc[0,51])#self character 7
print(g.iloc[0,52])#self rating 7
print(g.iloc[0,53])#self character 8
print(g.iloc[0,54])#self rating 8
print(g.iloc[0,55])#self character 9
print(g.iloc[0,56])#self rating 9
print(g.iloc[0,57])#self character 10
print(g.iloc[0,58])#self rating 10
print(g.iloc[0,59])#self character 11
print(g.iloc[0,60])#self rating 11
print(g.iloc[0,61])#self character 12
print(g.iloc[0,62])#self rating 12
print(g.iloc[0,63])#self character 13
print(g.iloc[0,64])#self rating 13
'''



class PopUp():
    def __init__(self, parent):
        super().__init__()
        self.num = 0
        self.label0 = tk.Label(parent, text=str(g.iloc[self.num,26]),width=100,height=20).grid(row=0,column=0,rowspan=24)# list of all characteristics
#researcher defined labels     
        self.label1a = tk.Label(parent, text=str(d[28]),width=15,height=2).grid(row=0,column=2,rowspan=1)#comp
        self.label1a = tk.Label(parent, text=str(d[29]),width=15,height=2).grid(row=1,column=2,rowspan=1)#int
        self.label1a = tk.Label(parent, text=str(d[30]),width=15,height=2).grid(row=2,column=2,rowspan=1) #trust
        self.label1a = tk.Label(parent, text=str(d[31]),width=15,height=2).grid(row=3,column=2,rowspan=1)#charisma
        self.label1a = tk.Label(parent, text=str(d[32]),width=15,height=2).grid(row=4,column=2,rowspan=1)#empathy
        self.label1a = tk.Label(parent, text=str(d[33]),width=15,height=2).grid(row=5,column=2,rowspan=1)#warmth
        self.label1a = tk.Label(parent, text=str(d[34]),width=15,height=2).grid(row=6,column=2,rowspan=1)#expertise
        self.label1a = tk.Label(parent, text=str(d[35]),width=15,height=2).grid(row=7,column=2,rowspan=1)#similarity
        self.label1a = tk.Label(parent, text=str(d[36]),width=15,height=2).grid(row=8,column=2,rowspan=1)#familiarity
        self.label1a = tk.Label(parent, text=str(d[37]),width=15,height=2).grid(row=9,column=2,rowspan=1)#likeability
        self.label1a = tk.Label(parent, text=str(d[38]),width=15,height=2).grid(row=10,column=2,rowspan=1)#attractiveness
        
        #Competence rating
        self.label1 = self.rating_box(parent,self.num,28,0,3) # excel row, excel column, gui row, gui column
        #Integrity rating
        self.label2 = self.rating_box(parent,self.num,29,1,3)
        #Trust rating
        self.label3 = self.rating_box(parent,self.num,30,2,3)
        #Charisma rating
        self.label4 = self.rating_box(parent,self.num,31,3,3)
        #Empathy rating
        self.label5 = self.rating_box(parent,self.num,32,4,3)
        #Warmth rating
        self.label6 = self.rating_box(parent,self.num,33,5,3)
        #Expertise rating
        self.label7 = self.rating_box(parent,self.num,34,6,3)
        #Similarity rating
        self.label8 = self.rating_box(parent,self.num,35,7,3)
        #Familiarity rating
        self.label9 = self.rating_box(parent,self.num,36,8,3)
        #Likeability rating
        self.label10 = self.rating_box(parent,self.num,37,9,3)
        #Attractiveness rating
        self.label11 = self.rating_box(parent,self.num,38,10,3)

        #mt1
        self.label13 = self.rating_box(parent,self.num,39,0,4,12)
        #mtn1
        self.label14 = self.rating_box(parent,self.num,40,0,5)

        #mt2
        self.label15 = self.rating_box(parent,self.num,41,1,4,12)
        #mtn2
        self.label16 = self.rating_box(parent,self.num,42,1,5)

        #mt3
        self.label17 = self.rating_box(parent,self.num,43,2,4,12)
        #mtn3
        self.label18 = self.rating_box(parent,self.num,44,2,5)

        #mt4
        self.label19 = self.rating_box(parent,self.num,45,3,4,12)
        #mtn4
        self.label20 = self.rating_box(parent,self.num,46,3,5)

        #mt5
        self.label21 = self.rating_box(parent,self.num,47,4,4,12)
        #mtn5
        self.label22 = self.rating_box(parent,self.num,48,4,5)

        #mt6
        self.label23 = self.rating_box(parent,self.num,49,5,4,12)
        #mtn6
        self.label24 = self.rating_box(parent,self.num,50,5,5)

        #mt7
        self.label25 = self.rating_box(parent,self.num,51,6,4,12)
        #mtn7
        self.label26 = self.rating_box(parent,self.num,52,6,5)

        #mt8
        self.label27 = self.rating_box(parent,self.num,53,7,4,12)
        #mtn8
        self.label28 = self.rating_box(parent,self.num,54,7,5)

        #mt9
        self.label29 = self.rating_box(parent,self.num,55,8,4,12)
        #mtn9
        self.label30 = self.rating_box(parent,self.num,56,8,5)

        #mt10
        self.label31 = self.rating_box(parent,self.num,57,9,4,12)
        #mtn10
        self.label32 = self.rating_box(parent,self.num,58,9,5)

        #mt11
        self.label33 = self.rating_box(parent,self.num,59,10,4,12)
        #mtn11
        self.label34 = self.rating_box(parent,self.num,60,10,5)

        #mt12
        self.label35 = self.rating_box(parent,self.num,61,11,4,12)
        #mtn12
        self.label36 = self.rating_box(parent,self.num,62,11,5)

        #mt13
        self.label37 = self.rating_box(parent,self.num,63,12,4,12)
        #mtn13
        self.label38 = self.rating_box(parent,self.num,64,12,5)

        PshBtn = tk.Button(parent,text='Save+Next',command=self.BtnPress).grid(row=13, column=4)
        self.RowSkip = tk.Entry(parent)
        self.RowSkip.grid(row=14, column=3)
        SkpBtn = tk.Button(parent,text='RowSkip',command=self.SkpPress).grid(row=14, column=4)

    def rating_box(self,parent, excel_row_no,excel_column_no, gui_row_no, gui_col_no, this_width=5):
        self.label1 = tk.Text(parent, width=this_width, height=1)
        self.label1.insert(0.0,str(g.iloc[excel_row_no,excel_column_no]))
        self.label1.grid(row=gui_row_no,column=gui_col_no,rowspan=1)
        return (self.label1)


    #function to skip to a certain row
    def SkpPress(self):
        print('beans')
            
        #print(f'{self.num}')
        Skip_to_this_row = self.RowSkip.get()
        print(Skip_to_this_row)
        #print(type(x))
        self.num = int(self.RowSkip.get())
        #print(f'{self.num}')
        ##self.num = int(self.RowSkip.get())
        #self.LabelNum["text"] = f'Row number = {self.num}'


        #self.label0.delete(0.0,'end')
        #self.Label2.delete(0.0,'end')
        #self.Label3.delete(0.0,'end')
        #self.Label4.delete(0.0,'end')

        #self.MT1.delete(0,'end')
        #self.MT1n.delete(0,'end')
        #self.MT2.delete(0,'end')
        #self.MT2n.delete(0,'end')
        #self.MT3.delete(0,'end')
        #self.MT3n.delete(0,'end')
        #self.MT4.delete(0,'end')
        #self.MT4n.delete(0,'end')
        #self.MT5.delete(0,'end')
        #self.MT5n.delete(0,'end')

        self.label0["text"] = f'{g.iloc[self.num,26]}'
        #self.label0.insert(0.0,f'{g.iloc[self.num,26]}')
        #self.Label2.insert(0.0,f'{MainDF.iloc[self.num,25]}')
        #self.Label3.insert(0.0,f'{MainDF.iloc[self.num,26]}')
        #self.Label4.insert(0.0,f'{MainDF.iloc[self.num,27]}')

        #self.MT1.insert(0,f'{MainDF.iloc[self.num,45]}')
        #self.MT1n.insert(0,f'{MainDF.iloc[self.num,46]}')
        #self.MT2.insert(0,f'{MainDF.iloc[self.num,47]}')
        #self.MT2n.insert(0,f'{MainDF.iloc[self.num,48]}')
        #self.MT3.insert(0,f'{MainDF.iloc[self.num,49]}')
        #self.MT3n.insert(0,f'{MainDF.iloc[self.num,50]}')
        #self.MT4.insert(0,f'{MainDF.iloc[self.num,51]}')
        #self.MT4n.insert(0,f'{MainDF.iloc[self.num,52]}')
        #self.MT5.insert(0,f'{MainDF.iloc[self.num,53]}')
        #self.MT5n.insert(0,f'{MainDF.iloc[self.num,54]}'
        
    #function to save the box content/ move ahead 1 row
    #def save_and_move(self,parent):
    def BtnPress(self):
        print('eggs')
        #MainDF.iloc[self.num,24] = self.Label1.get(0.0,'end')
        #MainDF.iloc[self.num,25] = self.Label2.get(0.0,'end')
        #MainDF.iloc[self.num,26] = self.Label3.get(0.0,'end')
        #MainDF.iloc[self.num,27] = self.Label4.get(0.0,'end')

        #MainDF.iloc[self.num,45] = self.MT1.get()
        #MainDF.iloc[self.num,46] = self.MT1n.get()
        #MainDF.iloc[self.num,47] = self.MT2.get()
        #MainDF.iloc[self.num,48] = self.MT2n.get()
        #MainDF.iloc[self.num,49] = self.MT3.get()
        #MainDF.iloc[self.num,50] = self.MT3n.get()
        #MainDF.iloc[self.num,51] = self.MT4.get()
        #MainDF.iloc[self.num,52] = self.MT4n.get()
        #MainDF.iloc[self.num,53] = self.MT5.get()
        #MainDF.iloc[self.num,54] = self.MT5n.get()
        ##MainDF.iloc[self.num,56] = self.Attractiveness.get()
        #MainDF.to_excel("PhD_Study1_V7.xlsx",sheet_name="sheet1",index=False)
        #self.num+=1

        #self.Label1.delete(0.0,'end')
        #self.Label2.delete(0.0,'end')
        #self.Label3.delete(0.0,'end')
        #self.Label4.delete(0.0,'end')

        #self.MT1.delete(0,'end')
        #self.MT1n.delete(0,'end')
        #self.MT2.delete(0,'end')
        #self.MT2n.delete(0,'end')
        #self.MT3.delete(0,'end')
        #self.MT3n.delete(0,'end')
        #self.MT4.delete(0,'end')
        #self.MT4n.delete(0,'end')
        #self.MT5.delete(0,'end')
        #self.MT5n.delete(0,'end')
        
        #self.Label1.insert(0.0,f'{MainDF.iloc[self.num,24]}')
        #self.Label2.insert(0.0,f'{MainDF.iloc[self.num,25]}')
        #self.Label3.insert(0.0,f'{MainDF.iloc[self.num,26]}')
        #self.Label4.insert(0.0,f'{MainDF.iloc[self.num,27]}')

        #self.MT1.insert(0,f'{MainDF.iloc[self.num,45]}')
        #self.MT1n.insert(0,f'{MainDF.iloc[self.num,46]}')
        #self.MT2.insert(0,f'{MainDF.iloc[self.num,47]}')
        #self.MT2n.insert(0,f'{MainDF.iloc[self.num,48]}')
        #self.MT3.insert(0,f'{MainDF.iloc[self.num,49]}')
        #self.MT3n.insert(0,f'{MainDF.iloc[self.num,50]}')
        #self.MT4.insert(0,f'{MainDF.iloc[self.num,51]}')
        #self.MT4n.insert(0,f'{MainDF.iloc[self.num,52]}')
        #self.MT5.insert(0,f'{MainDF.iloc[self.num,53]}')
        #self.MT5n.insert(0,f'{MainDF.iloc[self.num,54]}')



root = tk.Tk()
PopUp(root)
root.mainloop()

        
        
