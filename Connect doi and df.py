# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:44:17 2017

@author: Remy Hertogs

Koppelen van elementen uit csv met gedownloade metadata en de ge-extracte tabellen uit de meta-analyses.

info excel sheets importeren
http://pandas.pydata.org/pandas-docs/version/0.17.1/generated/pandas.read_excel.html

Vooraf excel sheet in orde maken, werkbladen/rijen/ kolommen verwijderen, hernoemen. Naar eigen inzicht. 
Te veel verschil tussen tabellen en artikelen om dit gestandaardiseerd te doen.
18-10-17 Veel art bevatten tabellen, maar niet met auteurs?
"""
import pandas as pd
# excel file met tabellen
df_original = pd.read_excel('Cerasoli2014.xlsx', sheetname=[6,7,8,9,10,11,12]) # kies de relevante sheets uit excel. Dit levert dict op


# aan elkaar zetten van dataframes, indien één tabel in tweeën of meer delen is opgesneden
# http://tinyurl.com/ya5ykksr
df_Vachon_ES1=df_or[0] # enkele dataframe uit dict hierboven selecteren
df_Vachon_ES2=df_or[1]

# verwijder overbodige kolommen 
del df_Vachon_ES1['Empathy']
del df_Vachon_ES2['Empathy']

# bekijk de verschillende kolomnamen en welke hernoemd moeten worden
df_Vachon_ES1 = df_Vachon_ES1.rename(columns={'Published': 'Study', 'Unnamed: 4': 'Unnamed: 3'})



# Indien nu twee of meer exacte dataframes, deze mergen. Syntax voor meerdere dataframes:
# ignore_index=true regelt nummering
df_Vachone_compl_ES = pd.concat([df_Vachon_ES1, df_Vachon_ES2],ignore_index=True)



# importeren doi csv file
df2=pd.read_csv("DOI extract\_Archief\meta analyse extracted doi's Vachon.csv")

# ook hier weer handmatig dataframe bewerken
del df2['Unnamed: 0']

# selecteren rij/ kolommen dataframe
# http://tinyurl.com/cecjj9e
df_sel_doi=df2[:1]
df_sel_ES=df_Vachone_compl_ES[:1]

# deze twee rijen matchen.
aut_ES=df_sel_ES.loc[0, 'Study']
aut_doi=df_sel_doi.loc[0,'Authors']

# splitten van auteurs string
sep_aut=aut_ES.split(' ')

# en vergelijken van cel inhoud
if sep_aut[0] in aut_doi:
    print('Author match = true')
else:
    print('Author match= false')
    
    
# zelfde verhaal voor jaartal.
# van df_sel_ES hebben we al het jaartal, deze stond bij auteurs. Dit is laatste element van de list sep_aut (niet gebruikt hieronder)
year_doi=df_sel_doi.loc[0,'Pub_Year'] 
sep_year=year_doi.split(' ')   

if sep_year[0] in aut_ES:
    print('Publication year match = true')
else:
    print('Publication year match= false')   
    
# Bovenstaande samen:
if (sep_aut[0] in aut_doi) and (sep_year[0] in aut_ES):
    print('Publication year and author match = true')
else:
    print('Publication year and/or author match= false') 

# de gevonden DOI bij oorspronkelijke dataframe ES zetten   
# of
# de relevante gegevens kopiëren in de dataframe van daniel
df_daniel1 = pd.read_excel("PDF extract\\MetaDataCodingForm.xlsx", sheetname='Coding') 


# '0000-0001-9462-4196' ORCHID remy

dfX=df_daniel1.append({'ARTICLE_NAME': aut_ES, \
                    'ARTICLE_DOI': df_sel_doi.loc[0,'Meta_Doi'], \
                    'CODED_BY': '0000-0001-9462-4196' , \
                    'ANALYSIS_N': df_sel_ES.loc[0,'N'],\
                    'STUDY_EFFECT_SIZE_AS_REPORTED_IN_META': df_sel_ES.loc[0,'ES']}, \
                    ignore_index=True)

# In loop voor alle rijen van de dataframe














