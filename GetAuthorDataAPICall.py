# Load required packages
import requests
import json     
import pandas as pd 

# Bring in the output dataframe that is produced by the r-code
CitationData = pd.read_excel('CitationData_PY.xlsx')

# Retrieve the author ID column
AuthorID = CitationData['Author Scopus ID'].fillna(0).astype('int64').to_list()

# Create the new dataframe to hold author information
AuthorData = pd.DataFrame(columns = ['Author ID','Co-author Count','h-index','Citation Count','Cited by Count','Document Count'])

# Loop through the ID's to get data
for x in AuthorID:

    # API call to get data
    resp = requests.get(f"http://api.elsevier.com/content/author?author_id={x}&view=metrics",
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': "44f055d2666f0d63b928f6d10e2f77d2"})
                              
    # Add results in JSON format
    element = json.dumps(resp.json(),
                 sort_keys=True,
                 indent=4, separators=(',', ': ')) 
    
    # Convert to a dictionary
    json_acceptable_string = element.replace("'", "\"")
    dictionary = json.loads(json_acceptable_string)

    # Get the required data from the dictionary and add to the author dataframe
    for i in dictionary['author-retrieval-response']:
        if i['@status'] == 'found':
            CoauthorCount = i['coauthor-count']
            hindex = i['h-index']
            citationcount = i['coredata']['citation-count']
            citedbycount = i['coredata']['cited-by-count']
            authorID = i['coredata']['dc:identifier']
            documentcount = i['coredata']['document-count']

        else:
            CoauthorCount = ''
            hindex = ''
            citationcount = ''
            citedbycount = ''
            authorID = x
            documentcount = ''

    AuthorData = AuthorData.append({'Author ID' : authorID, 'Co-author Count' : CoauthorCount, 'h-index' : hindex, 'Citation Count' : citationcount, 'Cited by Count' : citedbycount, 'Document Count' : documentcount},ignore_index = True)

    # Export dataframe to Excel file
    AuthorData.to_excel('AuthorData.xlsx')