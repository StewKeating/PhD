#Write a script that picks up the rank of the final round, and what the ratings were per participant

#if any ratings are the same, the highest rank maintains the rating, the newxt highest is 1 less and so on

#and ratings that are over lapped are then at the bottom of the -1 pile

#PhD_Study1_V7.xlsx

#Descriptive stats
import pandas as pd

pd.set_option("display.max_rows", None)
#pd.set_option("display.max_columns", None)


MainDF = pd.read_excel('PhD_Study_V7.xlsx')

#s.drop(['a','c'])#Drop values from rows (axis=0)
#df.drop('Country', axis=1)#Drop values from columns(axis=1)
MainDF.columns # Get Column names

PostDrop = MainDF.drop(['Age', 'CoBirth', 'CoRes', 'Employment', 'Ethnicity',
       'FirstLang', 'nationality', 'sex', 'StudentStatus', 'GenderSameAsBirth',
       'GenderID', 'AgeQualtrics', 'EthnicityQual', 'NationalID', 'EduLevel',
       'EligableUKvote', 'RecentVote', 'AlwaysSameParty', 'DescribeParty',
       'MemberOfParty', 'MemberWhich', 'OtherParty', 'Line','Condition'],axis=1)

#Read along each row, check each of the researcher traits columns and mt1/mt1n >> for equal numbers
#if thre are the same number use column PostDrop['Trait4_MoreCharacter'] as a rank list
#alt
#use Trait4_MoreCharacter to create a new column for each trait list stating the rank from top to bottom
#will likely need a GUI and go through row by row, then complete above task

