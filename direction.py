#######################################
'''------------------------------------
#Programming Language used :: Python
#Author :: Anubhav Choudhary

---------------------------------------'''
########################################

#-----------------code-----------------#

import pandas as pd
input_url = '/Users/anubhavchoudhary/desktop/github/Hatchways/input/'		
output_url = '/Users/anubhavchoudhary/desktop/github/Hatchways/output/'	

#----------Reads text files and save them----------#
def read_file(input_file):
    list_df = []
    df = pd.read_csv(input_url+input_file)    
    return df

#-----------Result output---------------#
def write_new_file(filename):
    f= open(output_url+filename,"w+")    
    f.close()
    
def write_end_file(file,line):
    f=open(output_url+file, 'a')
    f.write(line)
    f.close()
    
#pip install pandas (if this dosnt work try with --user flag )
