#------------------Header---------------------
# This script takes the .txt files which I scraped from EconLit for each year
# 2010-2019 and concatenates them. I also format them in a way which enables
# the analysis later on.
#
# econlit_concat.py
# Last edited date: 2020-12-12
# Last edited by: Joseph Levine
#---------------------------------------------




#------------------Outline--------------------
#	Outline
#	Program set-up
#	Part 1: For all years, compile .txt to pandas dataframe
#	Part 2: Concatenate dataframes and export
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
#	Part 1: For all years, compile .txt to pandas dataframe
#----------------------------------------------------------------

outfilepath = 'C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Data/econlit_txt/'
outfilename = outfilepath + 'all_files' + ".txt"

years = {}



for i in range(0,10):
    i = str(i).zfill(1)
    filenames = os.listdir('C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Data/econlit_txt/txt_files201'+i)



    path_txt = 'C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Data/econlit_txt/txt_files201'+i
    col_list = [ 'AU', 'AF', 'SO', 'DT', 'DE', 'PT', 'IS', 'UD', 'AN','\n']

    with open(outfilename, 'wt') as outfile:
        for fname in filenames:
            with open(path_txt+'/'+fname, 'rt') as readfile:
                infile = readfile.readlines()
                for line in infile:
                    if line[:2] in col_list: outfile.write(line[4:])
                    elif line[:2] == 'TI': outfile.write('\n'+line[4:])
                outfile.write("\n\n")
    with open(outfilename, 'r') as f:
        data = f.read().replace('\n','@').replace('@@','\n')


    data = data[1:]


    year_set = pd.read_csv(pd.compat.StringIO(data), header=None, sep = '@', low_memory=True, error_bad_lines=False)

    years['set_'+i] = year_set


#----------------------------------------------------------------
#	Part 2: Concatenate dataframes and export
#----------------------------------------------------------------

#just for 2016-2019; change dataframe names to be comprehensive
all_papers = pd.concat([years['set_6'],years['set_7'],years['set_8'],years['set_9']], ignore_index=True).dropna()

print(type(all_papers))


#change the export file name appropriately
all_papers.to_csv('C:/Users/240-370-8956/Dropbox/Research/JEL_codes/Temp/2016-2019_articles.csv',chunksize=10000)
