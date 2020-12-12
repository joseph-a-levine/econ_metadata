#------------------Header---------------------
# This script takes the output .csv of econlit_concat.py and delimits the fields as
# needed. That .csv has all JEL codes in a single column and all authors in
# another column and all author affiliations in another column. This script
# delimits each of those columns, so each row becomes paper-author-author
# affiliation-JEL code unique panel dataset. While cumbersome, it allows me to
# analyze at the deparment and JEL code level.
#
# econlit_delimiting.py
# Last edited date: 2020-12-12
# Last edited by: Joseph Levine
#---------------------------------------------




#------------------Outline--------------------
#	Outline
#	Program set-up
#	Part 1: Delimit for JEL codes
#	Part 2: Delimit for authors and author affiliations
#---------------------------------------------




#-------------------Program set-up-------------------------------
import time, glob
import os
import shutil
from io import StringIO
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import re
#----------------------------------------------------------------




#----------------------------------------------------------------
#	Part 1: Delimit for JEL codes
#----------------------------------------------------------------

articles_wide = pd.read_csv('C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Temp/2016-2019_articles.csv')
print('one')
articles_wide.columns = ['idx', 'Title', 'Author(s)', 'Author Affiliation(s)', 'Publication', 'Date', 'JEL Codes', 'IS', 'Type', 'UD', 'AN']


#Just dropping these fields for size; will want some of these fields back
articles_wide = articles_wide.drop(['IS','UD','Type','Publication'], axis=1)

articles_wide = articles_wide.dropna(subset=['JEL Codes', 'Author(s)'])

JELs = pd.DataFrame(articles_wide['JEL Codes'].str.split(';').tolist(), index=articles_wide['idx']).stack()

articles_wide = articles_wide.set_index('idx')

JELs = JELs.str.extract(r"\(([A-Za-z0-9]+)\)", expand=False).dropna()
joined_jels = articles_wide.join(JELs.rename('JEL')).drop(['JEL Codes'], axis=1)


joined_jels.to_csv('C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Temp/JELs_16-19_joined.csv', chunksize=10000)

#----------------------------------------------------------------
# Checkpoint, saving to .csv
#----------------------------------------------------------------

#----------------------------------------------------------------
#	Part 2: Delimit for authors and author affiliations
#----------------------------------------------------------------

articles_wide = pd.read_csv('C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Temp/JELs_16-19_joined.csv')


articles_wide = articles_wide.reset_index()

articles_wide.columns = ['idx', 'idx_paper','idx_jel','Title', 'Author(s)', 'Author Affiliation(s)', 'Date', 'AN','JEL']

articles_wide = articles_wide.dropna(subset=['JEL', 'Author(s)','Title'])

affs = pd.DataFrame(articles_wide['Author Affiliation(s)'].str.split(';').tolist(), index=articles_wide['idx']).stack().dropna()

articles_wide = articles_wide.set_index('idx')

joined_affs = articles_wide.join(affs.rename('Affiliation')).drop(['Author Affiliation(s)'], axis=1)


joined_affs.to_csv('C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Temp/JELs_joined_16-19_affs.csv', chunksize=10000)
