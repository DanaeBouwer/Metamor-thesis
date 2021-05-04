import pandas as pd
list_of_cit = pd.read_excel(r'C:\Users\DanaeBouwer\OneDrive - BSC Holdings\Documents\Thesis\Analysis\Microeconomics\Data Input\Microeconomics_Behavior, Institutions, and Evolution_Input.xlsx', sheet_name= 'Sheet1',header =0)
list_of_cit_edt = pd.DataFrame()
stringlong = ''


for x in range(0, len(list_of_cit)): #GOOD

    string = list_of_cit.iloc[x,0] # GOOD
    
    
    
    if str(string)[-1:] == '.' and str(string)[-2:] != 'p.' and 'Works Cited' not in str(string):
       stringlong = stringlong + ' ' + str(string)
       list_of_cit_edt = list_of_cit_edt.append({'Name':stringlong}, ignore_index = True)
       
       stringlong = ''
       #list_of_cit.iloc[x,0] = string
    elif 'Works Cited' in str(string):
        stringlong = ''
    else:
       stringlong = stringlong + str(string) 
   
print(list_of_cit_edt)

list_of_cit_edt.to_excel('Microeconomics_Behavior, Institutions, and Evolution_Output.xlsx')