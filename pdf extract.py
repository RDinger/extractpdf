# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 16:16:11 2017

@author: Remy Hertogs

http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using_Python_to_Extract_Tables_From_PDFs.php
"""

# van pagina 
# https://dirkmjk.nl/en/2017/04/how-automate-extracting-tables-pdfs-using-tabula
# 7-6 werkt eenmalig
# Originele code snippet voor inlezen pdf. Werkt bij één bestand tegelijk. 
# foutmelding bij meerdere bestanden.
import tabula
import os
import pandas as pd

folder = "C:\\Users\\Remy Hertogs\\Documents\\Python Scripts\\Machine Learning\\PDF extract\\pdf\\Vachon - 2014.pdf"
paths = [folder + fn for fn in os.listdir(folder) if fn.endswith('.pdf')]
for path in paths:
    df = tabula.read_pdf(path, encoding = 'latin1', pages = 8, nospreadsheet = True, multiple_tables=True)
    path = path.replace('pdf', 'csv')
    df.to_csv(path, index = False)
    
# weggehaald bij df=tabula.read_pdf , na pages=all en voor nospreadsheet.  area = [29.75,43.509,819.613,464.472]


#############################################################################
""" Meermalig, itereren over pdf's
13-6-2017. Dit lijkt te werken, al heb ik het idee dat er veel ruis in tabellen zit
bijv literatuurlijst of normale stukken tekst.
Nav stackoverflow post: 
https://tinyurl.com/y88hefej
"""
import tabula
import os
import pandas as pd

# creeëren van twee mappen, voor pdf en csv
pdf_folder = 'C:\\Users\\Remy Hertogs\\Documents\\Python Scripts\\Machine Learning\\PDF extract\\pdf\\'
csv_folder = 'C:\\Users\\Remy Hertogs\\Documents\\Python Scripts\\Machine Learning\\PDF extract\\csv\\'

# pad instellen waarmee alle bestanden in pdf folder worden gezocht.
paths = [pdf_folder + fn for fn in os.listdir(pdf_folder) if fn.endswith('.pdf')]

"""loop die een list creeërt (listdf) voor ieder pdf bestand (path in paths), en daar de 
tabel uit haalt.
Encoding, pages, nospreadsheet zijn parameters om tabellen te identificeren. 
Multitables geeft aan dat er meerdere tabellen zijn.
Daarna wordt path gewijzigd in csv map, alle dataframes uit listdf worden onder elkaar geplakt
en weggeschreven naar csv file met dezelfde naam als de pdf.
"""

for path in paths:
    listdf = tabula.read_pdf_table(path, encoding = 'latin1', pages = 'all', nospreadsheet = False,multiple_tables=True)
    path = path.replace('pdf', 'csv')
    df_concat = pd.concat(listdf)
    df_concat.to_csv(path, index = False)    


     
     
##################################################
########### Zelfde soort loop als naar csv #######
########### Ditmaal voor excel, met iedere #######
########### tabel op andere tabblad        #######    
########### dit lijkt het beste te werken  #######

import tabula
import os
import pandas as pd
from openpyxl import load_workbook

# creeëren van twee mappen, voor pdf en csv
# C:\\Users\\Remy Hertogs\\Documents\\Python Scripts\\Machine Learning\\PDF extract\\pdf\\
pdf_folder = 'Z:\\Rapporten\\Annemie\\Dhr Breug\\'
csv_folder = 'C:\\Users\\Remy Hertogs\\Documents\\Python Scripts\\Machine Learning\\PDF extract\\csv\\'         # niet nodig
xlsx_folder = 'C:\\Users\\Remy Hertogs\\Documents\\Python Scripts\\Machine Learning\\PDF extract\\xlsx\\'       # doelmap voor excel bestanden
    
paths = [pdf_folder + fn for fn in os.listdir(pdf_folder) if fn.endswith('.pdf')]    

for path in paths:
    listdf= tabula.read_pdf_table(path, encoding='latin1', pages='all', nospreadsheet= False, multiple_tables= True)
    path = path.replace('pdf', 'xlsx')     
    df_concat=pd.concat(listdf)     # deze is niet noodzakelijk, komt uit csv snippet
    writer=pd.ExcelWriter(path, engine='openpyxl')
    for n,df in enumerate(listdf):                   # toegevoegd n en enumerate en haakjes, dat werkt
        df.to_excel(writer,'sheets%s' % n, startrow=2, index=False)            #toegevoegd ,'sheets%s' % n    en len(df)+3 (was +2) achter len(df)-> werkt
    writer.save() 
   








