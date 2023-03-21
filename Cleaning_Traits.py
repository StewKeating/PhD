#Trait1, Trait2_RankRate, Trait3_Researchers, Trait4_MoreCharacter
#Competence, Integrity, Trustworthiness, Charisma, Empathy, Warmth
#Expertise, Similarity,	Familiarity,Likeability, Attractiveness
#y,z,aa,ab,ac,ad,ae,af,ag,ah,ai,aj,ak,al,am


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
'''
class PopUp():
    
    def __init__(self, parent):
        super().__init__()
        root.columnconfigure(0, weight=1, minsize=350)
        root.rowconfigure(0, weight=1, minsize=25)
        self.num = 0
        self.Label = tk.Text(parent)#, width=500, height=500)
        self.Label.insert(0.0,f'{MainDF.iloc[self.num,27]}')
        self.Label.grid(row=0, column=0)
        self.Label.place(height=400, width=300)

        self.LabelNum = tk.Label(parent, text=f'{self.num}')
        self.LabelNum.grid(row=12, column=2)

        
        self.Label2 = tk.Label(parent, text='Competence')
        self.Label2.grid(row=1, column=1)
        self.Label2 = tk.Label(parent, text='Integrity')
        self.Label2.grid(row=2, column=1)
        self.Label2 = tk.Label(parent, text='Trust')
        self.Label2.grid(row=3, column=1)
        self.Label2 = tk.Label(parent, text='Charisma')
        self.Label2.grid(row=4, column=1)
        self.Label2 = tk.Label(parent, text='Empathy')
        self.Label2.grid(row=5, column=1)
        self.Label2 = tk.Label(parent, text='Warmth')
        self.Label2.grid(row=6, column=1)
        self.Label2 = tk.Label(parent, text='Expertise')
        self.Label2.grid(row=7, column=1)
        self.Label2 = tk.Label(parent, text='Similarity')
        self.Label2.grid(row=8, column=1)
        self.Label2 = tk.Label(parent, text='Familirity')
        self.Label2.grid(row=9, column=1)
        self.Label2 = tk.Label(parent, text='Likeability')
        self.Label2.grid(row=10, column=1)
        self.Label2 = tk.Label(parent, text='Attractiveness')
        self.Label2.grid(row=11, column=1)

        self.RowSkip = tk.Entry(parent)
        self.RowSkip.grid(row=13, column=1)
        SkpBtn = tk.Button(parent,text='RowSkip',command=self.SkpPress).grid(row=13, column=2)

        self.Competence = tk.Entry(parent)
        self.Competence.grid(row=1,column=2)
        self.Integrity = tk.Entry(parent)
        self.Integrity.grid(row=2,column=2)
        self.Trust = tk.Entry(parent)
        self.Trust.grid(row=3,column=2)
        self.Charisma = tk.Entry(parent)
        self.Charisma.grid(row=4,column=2)
        self.Empathy = tk.Entry(parent)
        self.Empathy.grid(row=5,column=2)
        self.Warmth = tk.Entry(parent)
        self.Warmth.grid(row=6,column=2)
        self.Expertise = tk.Entry(parent)
        self.Expertise.grid(row=7,column=2)
        self.Similarity = tk.Entry(parent)
        self.Similarity.grid(row=8,column=2)
        self.Familiarity = tk.Entry(parent)
        self.Familiarity.grid(row=9,column=2)
        self.Likeability = tk.Entry(parent)
        self.Likeability.grid(row=10,column=2)
        self.Attractiveness = tk.Entry(parent)
        self.Attractiveness.grid(row=11,column=2)
        self.Competence.insert(0,f'{MainDF.iloc[self.num,28]}')
        self.Integrity.insert(0,f'{MainDF.iloc[self.num,29]}')
        self.Trust.insert(0,f'{MainDF.iloc[self.num,30]}')
        self.Charisma.insert(0,f'{MainDF.iloc[self.num,31]}')
        self.Empathy.insert(0,f'{MainDF.iloc[self.num,32]}')
        self.Warmth.insert(0,f'{MainDF.iloc[self.num,33]}')
        self.Expertise.insert(0,f'{MainDF.iloc[self.num,34]}')
        self.Similarity.insert(0,f'{MainDF.iloc[self.num,35]}')
        self.Familiarity.insert(0,f'{MainDF.iloc[self.num,36]}')
        self.Likeability.insert(0,f'{MainDF.iloc[self.num,37]}')
        self.Attractiveness.insert(0,f'{MainDF.iloc[self.num,38]}')
               
        PshBtn = tk.Button(parent,text='Save+Next',command=self.BtnPress).grid(row=12, column=1)

    def SkpPress(self):
        self.num = int(self.RowSkip.get())
        self.LabelNum["text"] = f'Row number = {self.num}'
        self.Label.delete(0.0,'end')
        self.Competence.delete(0,'end')
        self.Integrity.delete(0,'end')
        self.Trust.delete(0,'end')
        self.Charisma.delete(0,'end')
        self.Empathy.delete(0,'end')
        self.Warmth.delete(0,'end')
        self.Expertise.delete(0,'end')
        self.Similarity.delete(0,'end')
        self.Familiarity.delete(0,'end')
        self.Likeability.delete(0,'end')
        self.Attractiveness.delete(0,'end')
        
        self.Label.insert(0.0,f'{MainDF.iloc[self.num,27]}')

        self.Competence.insert(0,f'{MainDF.iloc[self.num,28]}')
        self.Integrity.insert(0,f'{MainDF.iloc[self.num,29]}')
        self.Trust.insert(0,f'{MainDF.iloc[self.num,30]}')
        self.Charisma.insert(0,f'{MainDF.iloc[self.num,31]}')
        self.Empathy.insert(0,f'{MainDF.iloc[self.num,32]}')
        self.Warmth.insert(0,f'{MainDF.iloc[self.num,33]}')
        self.Expertise.insert(0,f'{MainDF.iloc[self.num,34]}')
        self.Similarity.insert(0,f'{MainDF.iloc[self.num,35]}')
        self.Familiarity.insert(0,f'{MainDF.iloc[self.num,36]}')
        self.Likeability.insert(0,f'{MainDF.iloc[self.num,37]}')
        self.Attractiveness.insert(0,f'{MainDF.iloc[self.num,38]}')
        
    def BtnPress(self):
        MainDF.iloc[self.num,27] = self.Label.get(0.0,'end')

        MainDF.iloc[self.num,28] = self.Competence.get()
        MainDF.iloc[self.num,29] = self.Integrity.get()
        MainDF.iloc[self.num,30] = self.Trust.get()
        MainDF.iloc[self.num,31] = self.Charisma.get()
        MainDF.iloc[self.num,32] = self.Empathy.get()
        MainDF.iloc[self.num,33] = self.Warmth.get()
        MainDF.iloc[self.num,34] = self.Expertise.get()
        MainDF.iloc[self.num,35] = self.Similarity.get()
        MainDF.iloc[self.num,36] = self.Familiarity.get()
        MainDF.iloc[self.num,37] = self.Likeability.get()
        MainDF.iloc[self.num,38] = self.Attractiveness.get()
        MainDF.to_excel("PhD_Study1_V5.xlsx",sheet_name="sheet1",index=False)
        self.num+=1

        self.LabelNum["text"] = f'Row number = {self.num}'
        
        self.Label.delete(0.0,'end')
        self.Competence.delete(0,'end')
        self.Integrity.delete(0,'end')
        self.Trust.delete(0,'end')
        self.Charisma.delete(0,'end')
        self.Empathy.delete(0,'end')
        self.Warmth.delete(0,'end')
        self.Expertise.delete(0,'end')
        self.Similarity.delete(0,'end')
        self.Familiarity.delete(0,'end')
        self.Likeability.delete(0,'end')
        self.Attractiveness.delete(0,'end')
        
        self.Label.insert(0.0,f'{MainDF.iloc[self.num,27]}')

        self.Competence.insert(0,f'{MainDF.iloc[self.num,28]}')
        self.Integrity.insert(0,f'{MainDF.iloc[self.num,29]}')
        self.Trust.insert(0,f'{MainDF.iloc[self.num,30]}')
        self.Charisma.insert(0,f'{MainDF.iloc[self.num,31]}')
        self.Empathy.insert(0,f'{MainDF.iloc[self.num,32]}')
        self.Warmth.insert(0,f'{MainDF.iloc[self.num,33]}')
        self.Expertise.insert(0,f'{MainDF.iloc[self.num,34]}')
        self.Similarity.insert(0,f'{MainDF.iloc[self.num,35]}')
        self.Familiarity.insert(0,f'{MainDF.iloc[self.num,36]}')
        self.Likeability.insert(0,f'{MainDF.iloc[self.num,37]}')
        self.Attractiveness.insert(0,f'{MainDF.iloc[self.num,38]}')
'''
pd.set_option("display.max_rows", None)
#pd.set_option("display.max_columns", None)
MainDF = pd.read_excel('PhD_Study1_V7.xlsx')
#print(MainDF.head())
#print(MainDF.columns)

#for i in MainDF['Trait1']:
#    print(i)
'''
root = tk.Tk()
PopUp(root)
root.mainloop()

#MainDF.to_excel("PhD_Study1_V6.xlsx",sheet_name="sheet1",index=False)
'''
#for Column in MainDF.columns:
#    print(Column)

#if Eligable to vote == No, remove row?

MainDemos = MainDF.drop(['CoBirth','CoRes','Employment','FirstLang',
             'nationality','StudentStatus','AgeQualtrics','EthnicityQual',
             'NationalID','EligableUKvote',
             'Trait1','Trait2_RankRate',
             'Trait3_Researchers','Trait4_MoreCharacter'],axis=1)


#Upper case and fill NaNs for most of the data set
MainDemos['MemberOfParty'] = MainDemos['MemberOfParty'].str.upper()
MainDemos['MemberOfParty'] = MainDemos['MemberOfParty'].fillna('NONE')

MainDemos['MemberWhich'] = MainDemos['MemberWhich'].fillna('NONE')
MainDemos['MemberWhich'] = MainDemos['MemberWhich'].str.upper()

MainDemos['OtherParty'] = MainDemos['OtherParty'].str.upper()
MainDemos['OtherParty'] = MainDemos['OtherParty'].fillna('NONE')

MainDemos['AlwaysSameParty'] = MainDemos['AlwaysSameParty'].fillna('YES')#
MainDemos['AlwaysSameParty'] = MainDemos['AlwaysSameParty'].str.upper() # Make all leaders upper case

MainDemos['DescribeParty'] = MainDemos['DescribeParty'].fillna('N/A')
MainDemos['DescribeParty'] = MainDemos['DescribeParty'].str.upper()

MainDemos['HearFrom'] = MainDemos['HearFrom'].str.upper()
MainDemos['HearFrom'] = MainDemos['HearFrom'].fillna('N/A')

MainDemos['AnythingElse'] = MainDemos['AnythingElse'].str.upper()
MainDemos['AnythingElse'] = MainDemos['AnythingElse'].fillna('NONE')

MainDemos['ExpertInArea'] = MainDemos['ExpertInArea'].str.upper()
MainDemos['ExpertInArea'] = MainDemos['ExpertInArea'].fillna('NONE')

MainDemos['Condition'] = MainDemos['Condition'].str.upper()
MainDemos['Condition'] = MainDemos['Condition'].fillna('NONE')

MainDemos['LikeLeaders'] = MainDemos['LikeLeaders'].str.upper()
MainDemos['LikeLeaders'] = MainDemos['LikeLeaders'].fillna('NONE')

MainDemos['Ethnicity'] = MainDemos['Ethnicity'].str.upper()
MainDemos['Ethnicity'] = MainDemos['Ethnicity'].fillna('NONE')

MainDemos['Line'] = MainDemos['Line'].fillna(50)

MainDemos['RecentVote'] = MainDemos['RecentVote'].fillna('NO')

MainDemos['LeaderInMind'] = MainDemos['LeaderInMind'].fillna('NONE')

MainDemos['GenderID'] = MainDemos['GenderID'].fillna('NONE')

#print(MainDemos)

#Fill NaNs for each of the traits
MainDemos['Competence'] = MainDemos['Competence'].fillna(-99)
MainDemos['Integrity'] = MainDemos['Integrity'].fillna(-99)
MainDemos['Trustworthiness'] = MainDemos['Trustworthiness'].fillna(-99)
MainDemos['Charisma'] = MainDemos['Charisma'].fillna(-99)
MainDemos['Empathy'] = MainDemos['Empathy'].fillna(-99)
MainDemos['Warmth'] = MainDemos['Warmth'].fillna(-99)
MainDemos['Expertise'] = MainDemos['Expertise'].fillna(-99)
MainDemos['Similarity'] = MainDemos['Similarity'].fillna(-99)
MainDemos['Familiarity'] = MainDemos['Familiarity'].fillna(-99)
MainDemos['Likeability'] = MainDemos['Likeability'].fillna(-99)
MainDemos['Attractiveness'] = MainDemos['Attractiveness'].fillna(-99)


##########################################################
#Make them all upper case
##########################################################
MainDemos['mt1'] = MainDemos['mt1'].fillna('NONE')
MainDemos['mt1n'] = MainDemos['mt1n'].fillna(-99)
MainDemos['mt1'] = MainDemos['mt1'].str.upper()
MainDemos['mt2'] = MainDemos['mt2'].fillna('NONE')
MainDemos['mt2n'] = MainDemos['mt2n'].fillna(-99)
MainDemos['mt2'] = MainDemos['mt2'].str.upper()
MainDemos['mt3'] = MainDemos['mt3'].fillna('NONE')
MainDemos['mt3n'] = MainDemos['mt3n'].fillna(-99)
MainDemos['mt3'] = MainDemos['mt3'].str.upper()
MainDemos['mt4'] = MainDemos['mt4'].fillna('NONE')
MainDemos['mt4n'] = MainDemos['mt4n'].fillna(-99)
MainDemos['mt4'] = MainDemos['mt4'].str.upper()
MainDemos['mt5'] = MainDemos['mt5'].fillna('NONE')
MainDemos['mt5n'] = MainDemos['mt5n'].fillna(-99)
MainDemos['mt5'] = MainDemos['mt5'].str.upper()
MainDemos['mt6'] = MainDemos['mt6'].fillna('NONE')
MainDemos['mt6n'] = MainDemos['mt6n'].fillna(-99)
MainDemos['mt6'] = MainDemos['mt6'].str.upper()
MainDemos['mt7'] = MainDemos['mt7'].fillna('NONE')
MainDemos['mt7n'] = MainDemos['mt7n'].fillna(-99)
MainDemos['mt7'] = MainDemos['mt7'].str.upper()
MainDemos['mt8'] = MainDemos['mt8'].fillna('NONE')
MainDemos['mt8n'] = MainDemos['mt8n'].fillna(-99)
MainDemos['mt8'] = MainDemos['mt8'].str.upper()
MainDemos['mt9'] = MainDemos['mt9'].fillna('NONE')
MainDemos['mt9n'] = MainDemos['mt9n'].fillna(-99)
MainDemos['mt9'] = MainDemos['mt9'].str.upper()
MainDemos['mt10'] = MainDemos['mt10'].fillna('NONE')
MainDemos['mt10n'] = MainDemos['mt10n'].fillna(-99)
MainDemos['mt10'] = MainDemos['mt10'].str.upper()
MainDemos['mt11'] = MainDemos['mt11'].fillna('NONE')
MainDemos['mt11n'] = MainDemos['mt11n'].fillna(-99)
MainDemos['mt11'] = MainDemos['mt11'].str.upper()
MainDemos['mt12'] = MainDemos['mt12'].fillna('NONE')
MainDemos['mt12n'] = MainDemos['mt12n'].fillna(-99)
MainDemos['mt12'] = MainDemos['mt12'].str.upper()
MainDemos['mt13'] = MainDemos['mt13'].fillna('NONE')
MainDemos['mt13n'] = MainDemos['mt13n'].fillna(-99)
MainDemos['mt13'] = MainDemos['mt13'].str.upper()
##########################################################




#for colname in MainDemos.columns:
#    print(MainDemos[colname].isnull().values.any())

MainDemosNoNaN = MainDemos.dropna() # remove NaNs
#print(MainDemosNoNaN)

#print(MainDemosNoNaN['RecentVote'])

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
#CONVERT POLITICAL PARTIES/LEADER TO UPPER CASE AND UNIFORM LABELS



MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].str.upper() # Make all votes upper case
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace=['LAB.*$', 'JEREMY.*$', 'THE LAB.*$','I THINK.*$',"CAN'T .*$",], value='LABOUR', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace='LIB.*$', value='LIBDEM', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace='CON.*$', value='CONSERVATIVE', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace='GRE.*$', value='GREEN', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace=['BREX.*$'], value='BREXIT', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace='ALL.*$', value='ALLIANCE', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace=['YESCYM.*$','PLAID.*$'], value='CYMRU', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace=['SNP.*$','SCOTTISH NAT.*$'], value='SNP', regex=True)
MainDemosNoNaN['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace=['NO.*$','DID NOT.*$','SPOIL.*$','I DID NOT.*$','DID NO.*$','I DIDN.*$',
                                                                                'I NO.*$','N/A.*$','I AM NO.*$','DIDN.*$','ABS.*$','I NO VOTE'], value='NO VOTE', regex=True)

print(MainDemosNoNaN['RecentVote'].value_counts())
print(MainDemosNoNaN['AlwaysSameParty'].value_counts())

#print(MainDemosNoNaN['RecentVote'])
#VoteCounts = MainDemosNoNaN['RecentVote'].value_counts()
#print(MainDemosNoNaN['RecentVote'].value_counts())

#print(MainDemosNoNaN.head())
#for i in MainDemosNoNaN['RecentVote']:
#    print(i)

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
#CONVERT EDUCATIONAL LEVEL TO UPPER CASE AND UNIFORM LABELS

EduCounts = MainDemosNoNaN['EduLevel'].value_counts()
MainDemosNoNaN['EduLevel'] = MainDemosNoNaN['EduLevel'].str.upper()
#print(MainDemosNoNaN['EduLevel'].value_counts())

MainDemosNoNaN['EduLevel'] = MainDemosNoNaN['EduLevel'].replace(to_replace=['BA.*$','BSC.*$','UNI.*$','UNDER.*$','UNDERGRADUATE.*$','HONOUR.*$','OPEN.*$',
                                                                            'HIST.*$','FIRST.*$','DEGREE','FOUNDATION.*$','LLB.*$','SOME U.*$']
                                                                            , value='UNDERGRADUATE', regex=True)
MainDemosNoNaN['EduLevel'] = MainDemosNoNaN['EduLevel'].replace(to_replace=['PHD.*$','DOCT.*$'], value='PHD', regex=True)
MainDemosNoNaN['EduLevel'] = MainDemosNoNaN['EduLevel'].replace(to_replace=['MA.*$','M.A.*$','MS.*$','POST.*$','DOUBLE.*$','PGCE.*$'
                                                                            ,'LEVEL 2 D.*$','PROFESS.*$','GRAM.*$'], value='POSTGRADUATE', regex=True)
MainDemosNoNaN['EduLevel'] = MainDemosNoNaN['EduLevel'].replace(to_replace=['A LEV.*$','A-LE.*$','HND.*$','HNC.*$','NVQ.*$','ONC.*$','BTEC.*$'
                                                                            ,'COLL.*$','FURTHER.*$','SOME C.*$','CURRENTLY STU.*$'], value='COLLEGE', regex=True)
MainDemosNoNaN['EduLevel'] = MainDemosNoNaN['EduLevel'].replace(to_replace=['GCS.*$','SECON.*$','HIGH SC.*$','SCHOO.*$','O LEVE.*$','O-LEVEL.*$','CURRENTLY A .*$',
                                                                            "O'LEV.*$","O'LEVEL'S"], value='SCHOOL', regex=True)
#print(MainDemosNoNaN['EduLevel'].value_counts())

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
#CONVERT SEX, SAME AS BIRTH & GENDERID TO UPPER CASE AND UNIFORM LABELS

SexCounts = MainDemosNoNaN['sex'].value_counts()
MainDemosNoNaN['sex'] = MainDemosNoNaN['sex'].str.upper()

SameAsBirthCounts = MainDemosNoNaN['GenderSameAsBirth'].value_counts()
MainDemosNoNaN['GenderSameAsBirth'] = MainDemosNoNaN['GenderSameAsBirth'].str.upper()

GendIDCounts = MainDemosNoNaN['GenderID'].value_counts()
MainDemosNoNaN['GenderID'] = MainDemosNoNaN['GenderID'].str.upper()

MainDemosNoNaN['GenderID'] = MainDemosNoNaN['GenderID'].replace(to_replace='M.*$', value='MALE', regex=True)
MainDemosNoNaN['GenderID'] = MainDemosNoNaN['GenderID'].replace(to_replace=['W.*$','F.*$','HET.*$'], value='FEMALE', regex=True)

#CALCUALTES IF 2 COLUMNS ARE SAME 1 = SAME 0 = DIFFERENT (ADDS COLUMN TO DF)
#MainDemosNoNaN['Diff'] = np.where( MainDemosNoNaN['sex'] == MainDemosNoNaN['GenderID'] , '1', '0')


#198 sex = male gender = female age = 27 vote = labour # IN EXCEL CHANGED SEX TO FEMALE PHD_STUDY1_V3.XLSX
#print(MainDemosNoNaN)
#print(MainDemosNoNaN['sex'].value_counts())
#print(MainDemosNoNaN['GenderSameAsBirth'].value_counts())
#print(MainDemosNoNaN['GenderID'].value_counts())

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
#CONVERT LEADER IN MIND UNIFORM LABELS (LIKELY ONLY POLITICIANS SIDE)
MainDemosNoNaN['LeaderInMind'] = MainDemosNoNaN['LeaderInMind'].str.upper() # Make all leaders upper case
LeaderMind = MainDemosNoNaN['LeaderInMind'].value_counts()
#MainDemosNoNaN['LeaderInMind'] = MainDemosNoNaN['LeaderInMind'].replace(to_replace=['BOR.*$','BOR.*$',], value='BORIS JOHNSON', regex=True)
#MainDemosNoNaN['LeaderInMind'] = MainDemosNoNaN['LeaderInMind'].replace(to_replace=['BA.*$','OB.*$',], value='BARACK OBAMA', regex=True)

LeaderMind = MainDemosNoNaN['LeaderInMind'].value_counts()
#print(LeaderMind)
Col = MainDemosNoNaN.columns.get_loc('LeaderInMind')

def Pol_Leader(LookFor, ReplaceWith,ColumnSpecific, shouldPrint = False):
    for items in LookFor:
        for Row in range(0,len(MainDemosNoNaN['LeaderInMind'])):
            Check = MainDemosNoNaN.iloc[Row,ColumnSpecific]
            if items in Check:
                if shouldPrint:
                    print(Check)
                MainDemosNoNaN.iloc[Row,ColumnSpecific] = ReplaceWith

Pol_Leader(['JOHNSON','BORIS','BORRIS'],'BORIS JOHNSON',Col)
Pol_Leader(['KEIR','STARMER'],'SIR KEIR STARMER',Col)
Pol_Leader(['CEO','CHIEF EXEC','INDUSTRY','COMPANY','STEVE','GATES','DAVIES','BEZOS','MUSK','BUSINESS'],'CEO BUSINESS LEADER',Col)
#Pol_Leader(['BLAIR'],'TONY BLAIR',Col)
Pol_Leader(['VAN TAM','WHITTY','WITTY','SCIENTIST','CHIEF MEDICAL'],'SCIENTIST',Col)
#Pol_Leader(['VAN TAM'],'PROFESSOR JOHNATHAN VAN TAM',Col)
#Pol_Leader(['WHITTY','WITTY'],'PROFESSOR CHRIS WHITTY',Col)
Pol_Leader(['JEREMY CORBYN','CORBYN','CORBIN'],'JEREMY CORBYN',Col)
Pol_Leader(['OBAMA','BARAK','BARACK','OBARMA'],'BARACK OBAMA',Col)
Pol_Leader(['JACINDA','ZEALAND'],'JACINDA ARDERN',Col)
Pol_Leader(['STURGEON'],'NICOLA STURGEON',Col)
Pol_Leader(['UNIVERSITY','HIGHER EDUCATION','DEAN OF EDU','EDUCATIONAL DEPARTMENT'],'UNIVERSITY RELATED',Col)
Pol_Leader(['SUNAK'],'RISHI SUNAK',Col)
Pol_Leader(['PRIME','PRIMIN'],'PRIME MINISTER',Col)
Pol_Leader(['NONE','NO ONE','NO-ONE','REAL','EXIST','IDEAL','MIXTURE',
            'DONT HAVE','IMAGINARY','NO SPECIFIC', 'I DON','NOBODY','EXPERTISE','DETERMINATION'],'NONE',Col)#,True)
Pol_Leader(['MY B','MY D','MY I','MY P','MY F','MY M','MY O','BOSS','AT WORK'
            'I WORK FOR','I WORKED FOR','I WORKED AT','I USED TO WORK','THE LEADER OF THE GROUP'
            ,'FORMER WORK COL','VE MET','MYSELF'],'F2F',Col)#,True)
Pol_Leader(['NHS','NATIONAL HEALTH','THE MEDICAL PERSON','HEAD OF A HOSPITAL',
            'OF THE HOSPITAL','MEDICAL STAFF','GENERAL PRACTI'],'NHS MEDICAL',Col)#,True)
Pol_Leader(['HEAD TEACHER','HEADTEACHER','HEADMASTER','BROWNIE'],'SCHOOL',Col)
Pol_Leader(['MINISTER FOR HEALTH','MINISTER OF HEALTH','HEALTH SEC','HEALTH MINISTER'],'MINISTER OF HEALTH',Col)
Pol_Leader(['COUNCIL','LOCAL'],'LOCAL AUTHORITY',Col)
Pol_Leader(['CHARITY'],'CHARITY LEADER',Col)
Pol_Leader(['MANAGER'],'MANAGER',Col)
Pol_Leader(['POLICE','CRESSIDA'],'LAW ENFORCEMENT',Col)
Pol_Leader(['SHAPPS','REES-MOGG','DUNCAN','HANDCOCK','PATEL','CAMERON','TRUSS','TERESA','THATCHER','CHURCHILL'],'CONSERVATIVE MP PRES/FORMER',Col)
Pol_Leader(['SHAMI','BLAIR','ATLEE','LABOUR LEADER','BLUNKETT','GORDON','BURNHAM','RAYNER','DODDS','MILIBAND'],'LABOUR MP PRES/FORMER',Col)
Pol_Leader(['BRAGG','NADER','FIGUERES','LINCOLN','SANDERS','PUTIN','MANDELLA','MERKEL','LUTHER KING','MANDELA','KHALIFAH','TRUDEAU','LULA','ISTVAN','SANKARA','MODI','ERDOGAN','RO PRESIDENT'],'NON UK POLITICS',Col)

#Row 205 was ME = F2F


#for i in range(0,len(MainDemosNoNaN['LeaderInMind'])):
#    Check = MainDemosNoNaN.iloc[i,Col]
#    if 'JOHNSON' in Check or 'BORIS' in Check or 'BORRIS' in Check:
#        #print(f'{i}==Row, {Check} == Cell content')
#        MainDemosNoNaN.iloc[i,Col] = 'BORIS JOHNSON'
#    if 'KEIR' in Check or 'STARMER' in Check:
#        MainDemosNoNaN.iloc[i,Col] = 'SIR KEIR STARMER'
#    if 'CEO' in Check:
#        #print(Check)
#        MainDemosNoNaN.iloc[i,Col] = 'CEO'
#    if 'BLAIR' in Check:
#        MainDemosNoNaN.iloc[i,Col] = 'TONY BLAIR'
#    if 'VAN TAM' in Check:
#        MainDemosNoNaN.iloc[i,Col] = 'PROF JONATHAN VAN TAM'
#    if 'JEREMY CORBYN' in Check or 'CORBYN' in Check or 'CORBIN' in Check:
#        MainDemosNoNaN.iloc[i,Col] = 'JEREMY CORBYN'
#    if 'OBAMA' in Check or 'BARAK' in Check or 'BARACK' in Check:
#        #print(Check)
#        MainDemosNoNaN.iloc[i,Col] = 'BARACK OBAMA'
#    if 'JACINDA' in Check or 'ZEALAND' in Check:
#        print(Check)
#        MainDemosNoNaN.iloc[i,Col] = 'JACINDA ARDERN'
#    if 'STURGEON' in Check:
#        #print(Check)
#        MainDemosNoNaN.iloc[i,Col] = 'NICOLA STURGEON'
#    if 'UNIVERSITY' in Check:
#        #print(Check)
#        MainDemosNoNaN.iloc[i,Col] = 'UNVERSITY RELATED'
#    if 'SUNAK' in Check:
#        #print(Check)
#        MainDemosNoNaN.iloc[i,Col] = 'RISHI SUNAK'
    #if 'PRIME' in Check:
    #    print(Check)
    #    MainDemosNoNaN.iloc[i,Col] = ''

#for cell in MainDemosNoNaN['LeaderInMind']:
#    if 'OBAMA' in cell:
#        print('Obama llama')
#    if 'VAN TAM' in cell:
#        print('JONATHAN VAN TAM')
#    if 'JOHNSON' in cell or 'BORIS' in cell or 'BORRIS' in cell:
#        Col = MainDemosNoNaN.columns.get_loc('LeaderInMind')
        #print(MainDemosNoNaN.iloc[cell,Col])
#        print(cell)
#        print(Col)
LeaderMind = MainDemosNoNaN['LeaderInMind'].value_counts()
#for i in MainDemosNoNaN['LeaderInMind']:
#    print(i)
#print(LeaderMind)
#MainDemosNoNaN['LeaderInMind'] = MainDemosNoNaN['LeaderInMind'].replace(to_replace=['BA.*$','OB.*$',], value='BARACK OBAMA', regex=True)
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
#Organise HearFrom
HeardFrom = MainDemosNoNaN['HearFrom'].value_counts()
Col = MainDemosNoNaN.columns.get_loc('HearFrom')
#print(HeardFrom)
def Hear_From(LookFor, ReplaceWith,ColumnSpecific, shouldPrint = False):
    for items in LookFor:
        for Row in range(0,len(MainDemosNoNaN['HearFrom'])):
            Check = MainDemosNoNaN.iloc[Row,ColumnSpecific]
            if items in Check:
                if shouldPrint:
                    print(Check)
                ReplaceWith = input()
                MainDemosNoNaN.iloc[Row,ColumnSpecific] = ReplaceWith
                
#Hear_From(['DAILY', 'DAY'],'x',Col,True)
#Hear_From(['WEEKLY', 'WEEK'],'x',Col,True)
#Hear_From(['MONTHLY','MONTH'],'MONTHLY',Col,True)
#Hear_From(['NECESSARY'],'NECESSARY',Col,True)
#Hear_From(['QUARTERLY'],'QUARTERLY',Col,True)
#Hear_From(['YEAR','ANNUALLY'],'YEARLY',Col,True)
#Hear_From(['NO IDEA'],'DONT KNOW',Col,True)
#Hear_From(['important','crisis','gone wrong'],'IMMEDIATELY',Col,True)

HeardFrom = MainDemosNoNaN['HearFrom'].value_counts()
#print(HeardFrom)

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################





Parties = MainDemosNoNaN

#Convert all parties with frequency less than 5 to be 'other'
Parties['RecentVote'] = MainDemosNoNaN['RecentVote'].replace(to_replace=['ALL.*$','BRE.*$','YES.*$','INDE.*$','HOWARD.*$','UKIP.*$','THE NDP.*$','DUP.*$','GROEN.*$','SCOTTISH CON.*$','FORTIE.*$','CYMRU'], value='OTHER<5', regex=True)


#Convert all education with frequency less than 2 to be 'other'
Parties['EduLevel'] = MainDemosNoNaN['EduLevel'].replace(to_replace=['WORKPLACE.*$','VOCATION.*$','PROMO.*$','NO QUAL.*$'], value='OTHER', regex=True)

####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################
####################################################################################

#print(Parties['RecentVote'].value_counts())
#print(Parties['RecentVote'])
#print(Parties.head())
#for Column in Parties.columns:
#    print(Column)

#plt.hist(Parties['RecentVote'],bins=20,align='left')
#plt.show()

#SexCounts = Parties['sex'].value_counts()
#SameAsBirthCounts = Parties['GenderSameAsBirth'].value_counts()
#GendIDCounts = Parties['GenderID'].value_counts()
#EduCounts = Parties['EduLevel'].value_counts()
#SamePartyCounts = Parties['AlwaysSameParty'].value_counts()


#print(Parties['GenderSameAsBirth'].value_counts())
#print(Parties['sex'].value_counts())
#print(Parties['GenderSameAsBirth'].value_counts())
#print(Parties['GenderID'].value_counts())
#print(Parties['EduLevel'].value_counts())
#print(Parties['AlwaysSameParty'].value_counts())
#print(Parties.columns)

#Parties.to_excel("PartiesV12.xlsx",sheet_name="sheet1",index=False)

