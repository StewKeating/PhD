library('readxl')
library('dplyr')
library('writexl')


DF1 = read_excel('Contents.xlsx')
DF2 = DF1%>%
	select(GivenText, WhatCat)
	mutate(WhatCat = tolower(WhatCat))
	recode(DF1$WhatCat, ambition = 'A')

#DF1$WhatCat = recode(DF1$WhatCat, ambition = 'A')

DF3 = read_excel('ContentAnalysis_For_Supervisors_JR.xlsx')
DF4 = DF3%>%
	select(GivenText, JR)

DF5 = read_excel('ContentAnalysis_For_Supervisors_VB.xlsx')
DF6 = DF5%>%
	select(GivenText, VB_coding)


Joiners = c('Ambition'='A','Appearance'='B','Attitude'='C','Communication'='D',
		'Creative'='E','Cultural'='F','Decision Making'='G','Dutiful'='H',		
		'emotional'='I','Fair'='J','Finance'='K','For others'='L','Health'='M',
		'Integrity'='N','Intelligence'='O','Interested'='P',
		'Kind, Caring, Compassionate'='Q','Lawful'='R','Leadership'='S',
		'Nationalist'='T','Organised'='U','Personality'='V',
		'Political leaning'='W','Reflective'='X','Relatable'='Y',
		'Skilled'='Z','Stout'='1','Team work'='2','Thick Skin'='3',
		'Trust'='4','Work Ethic'='5')

Joiners = c(ambition='A',appearance='B',attitude='C',communication='D',
		creative='E',cultural='F',decision making='G',dutiful='H',		
		emotional='I',fair='J',finance='K',for others='L',health='M',
		integrity='N',intelligence='O',interested='P',
		,lawful='R',leadership='S',
		nationalist='T',organised='U',personality='V',
		political leaning='W',reflective='X',relatable='Y',
		skilled='Z',stout='1',team work='2',thick skin='3',
		trust='4',work ethic='5')

DF7 = DF2%>%
	full_join(DF4, by = 'GivenText')
DF8 = DF7%>%
	full_join(DF6, by = 'GivenText')

write_xlsx(DF8,"Contents_Matched_JR_VB.xlsx")