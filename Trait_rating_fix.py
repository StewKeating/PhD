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

class PopUp():
    def __init__(self, parent):
        super().__init__()
        self.num = 0
        self.label0 = self.rating_box(parent,self.num,26,0,0, 100, 20,24)# list of all characteristics
#researcher defined labels     
        self.label1a = tk.Label(parent, text=str(d[28]),width=15,height=2).grid(row=0,column=2,rowspan=1)#comp
        self.label1a = tk.Label(parent, text=str(d[29]),width=15,height=2).grid(row=1,column=2,rowspan=1)#int
        self.label1a = tk.Label(parent, text=str(d[30]),width=15,height=2).grid(row=2,column=2,rowspan=1)#trust
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

    def rating_box(self,parent, excel_row_no,excel_column_no, gui_row_no, gui_col_no, this_width=5, this_height=1, this_rowspan=1):
        self.label = tk.Text(parent, width=this_width, height=this_height)
        self.label.insert(0.0,str(g.iloc[excel_row_no,excel_column_no]))
        self.label.grid(row=gui_row_no,column=gui_col_no,rowspan=this_rowspan)
        return (self.label)

    def clear_and_replace(self, row_num):
        self.label0.delete(0.0,'end')
        self.label1.delete(0.0,'end')
        self.label2.delete(0.0,'end')
        self.label3.delete(0.0,'end')
        self.label4.delete(0.0,'end')
        self.label5.delete(0.0,'end')
        self.label6.delete(0.0,'end')
        self.label7.delete(0.0,'end')
        self.label8.delete(0.0,'end')
        self.label9.delete(0.0,'end')
        self.label10.delete(0.0,'end')

        self.label11.delete(0.0,'end')
        self.label13.delete(0.0,'end')
        self.label14.delete(0.0,'end')
        self.label15.delete(0.0,'end')
        self.label16.delete(0.0,'end')
        self.label17.delete(0.0,'end')
        self.label18.delete(0.0,'end')
        self.label19.delete(0.0,'end')
        self.label20.delete(0.0,'end')

        self.label21.delete(0.0,'end')
        self.label22.delete(0.0,'end')
        self.label23.delete(0.0,'end')
        self.label24.delete(0.0,'end')
        self.label25.delete(0.0,'end')
        self.label26.delete(0.0,'end')
        self.label27.delete(0.0,'end')
        self.label28.delete(0.0,'end')
        self.label29.delete(0.0,'end')
        self.label30.delete(0.0,'end')

        self.label31.delete(0.0,'end')
        self.label32.delete(0.0,'end')
        self.label33.delete(0.0,'end')
        self.label34.delete(0.0,'end')
        self.label35.delete(0.0,'end')
        self.label36.delete(0.0,'end')
        self.label37.delete(0.0,'end')
        self.label38.delete(0.0,'end')

        self.label0.insert(0.0,f'{g.iloc[self.num,26]}')
        self.label1.insert(0.0,f'{g.iloc[self.num,28]}')
        self.label2.insert(0.0,f'{g.iloc[self.num,29]}')
        self.label3.insert(0.0,f'{g.iloc[self.num,30]}')
        self.label4.insert(0.0,f'{g.iloc[self.num,31]}')
        self.label5.insert(0.0,f'{g.iloc[self.num,32]}')
        self.label6.insert(0.0,f'{g.iloc[self.num,33]}')
        self.label7.insert(0.0,f'{g.iloc[self.num,34]}')
        self.label8.insert(0.0,f'{g.iloc[self.num,35]}')
        self.label9.insert(0.0,f'{g.iloc[self.num,36]}')
        self.label10.insert(0.0,f'{g.iloc[self.num,37]}')
        self.label11.insert(0.0,f'{g.iloc[self.num,38]}')

        self.label13.insert(0.0,f'{g.iloc[self.num,39]}')
        self.label14.insert(0.0,f'{g.iloc[self.num,40]}')
        self.label15.insert(0.0,f'{g.iloc[self.num,41]}')
        self.label16.insert(0.0,f'{g.iloc[self.num,42]}')
        self.label17.insert(0.0,f'{g.iloc[self.num,43]}')
        self.label18.insert(0.0,f'{g.iloc[self.num,44]}')
        self.label19.insert(0.0,f'{g.iloc[self.num,45]}')
        self.label20.insert(0.0,f'{g.iloc[self.num,46]}')
        self.label21.insert(0.0,f'{g.iloc[self.num,47]}')
        self.label22.insert(0.0,f'{g.iloc[self.num,48]}')
        self.label23.insert(0.0,f'{g.iloc[self.num,49]}')
        self.label24.insert(0.0,f'{g.iloc[self.num,50]}')

        self.label25.insert(0.0,f'{g.iloc[self.num,51]}')
        self.label26.insert(0.0,f'{g.iloc[self.num,52]}')
        self.label27.insert(0.0,f'{g.iloc[self.num,53]}')
        self.label28.insert(0.0,f'{g.iloc[self.num,54]}')
        self.label29.insert(0.0,f'{g.iloc[self.num,55]}')
        self.label30.insert(0.0,f'{g.iloc[self.num,56]}')
        self.label31.insert(0.0,f'{g.iloc[self.num,57]}')
        self.label32.insert(0.0,f'{g.iloc[self.num,58]}')
        self.label33.insert(0.0,f'{g.iloc[self.num,59]}')
        self.label34.insert(0.0,f'{g.iloc[self.num,60]}')
        self.label35.insert(0.0,f'{g.iloc[self.num,61]}')
        self.label36.insert(0.0,f'{g.iloc[self.num,62]}')
        self.label37.insert(0.0,f'{g.iloc[self.num,63]}')
        self.label38.insert(0.0,f'{g.iloc[self.num,64]}')
    
    #function to skip to a certain row
    def SkpPress(self):
        Skip_to_this_row = self.RowSkip.get()
        print(Skip_to_this_row)
        self.num = int(self.RowSkip.get())
        self.clear_and_replace(self.num)
        
    #save the boxes and move to the next row
    def BtnPress(self):
        g.iloc[self.num,26] = self.label0.get(0.0,'end')
        g.iloc[self.num,28] = self.label1.get(0.0,'end')
        g.iloc[self.num,29] = self.label2.get(0.0,'end')
        g.iloc[self.num,30] = self.label3.get(0.0,'end')
        g.iloc[self.num,31] = self.label4.get(0.0,'end')
        g.iloc[self.num,32] = self.label5.get(0.0,'end')
        g.iloc[self.num,33] = self.label6.get(0.0,'end')
        g.iloc[self.num,34] = self.label7.get(0.0,'end')
        g.iloc[self.num,35] = self.label8.get(0.0,'end')
        g.iloc[self.num,36] = self.label9.get(0.0,'end')
        g.iloc[self.num,37] = self.label10.get(0.0,'end')
        g.iloc[self.num,38] = self.label11.get(0.0,'end')

        g.iloc[self.num,39] = self.label13.get(0.0,'end')
        g.iloc[self.num,40] = self.label14.get(0.0,'end')
        g.iloc[self.num,41] = self.label15.get(0.0,'end')
        g.iloc[self.num,42] = self.label16.get(0.0,'end')
        g.iloc[self.num,43] = self.label17.get(0.0,'end')
        g.iloc[self.num,44] = self.label18.get(0.0,'end')
        g.iloc[self.num,45] = self.label19.get(0.0,'end')
        g.iloc[self.num,46] = self.label20.get(0.0,'end')
        g.iloc[self.num,47] = self.label21.get(0.0,'end')
        g.iloc[self.num,48] = self.label22.get(0.0,'end')
        g.iloc[self.num,49] = self.label23.get(0.0,'end')
        g.iloc[self.num,50] = self.label24.get(0.0,'end')

        g.iloc[self.num,51] = self.label25.get(0.0,'end')
        g.iloc[self.num,52] = self.label26.get(0.0,'end')
        g.iloc[self.num,53] = self.label27.get(0.0,'end')
        g.iloc[self.num,54] = self.label28.get(0.0,'end')
        g.iloc[self.num,55] = self.label29.get(0.0,'end')
        g.iloc[self.num,56] = self.label30.get(0.0,'end')
        g.iloc[self.num,57] = self.label31.get(0.0,'end')
        g.iloc[self.num,58] = self.label32.get(0.0,'end')
        g.iloc[self.num,59] = self.label33.get(0.0,'end')
        g.iloc[self.num,60] = self.label34.get(0.0,'end')
        g.iloc[self.num,61] = self.label35.get(0.0,'end')
        g.iloc[self.num,62] = self.label36.get(0.0,'end')
        g.iloc[self.num,63] = self.label37.get(0.0,'end')
        g.iloc[self.num,64] = self.label38.get(0.0,'end')

        g.to_excel("PhD_Study1_V8.xlsx",sheet_name="sheet1",index=False)
        
        self.num += 1
        self.clear_and_replace(self.num) 

root = tk.Tk()
PopUp(root)
root.mainloop()        
        
