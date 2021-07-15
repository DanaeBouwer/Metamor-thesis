import requests
import json     
import pandas as pd

CitationData = pd.read_excel('CitationData_PY.xlsx')

AuthorID = CitationData['Author Scopus ID'].fillna(0).astype('int64').to_list()

# Retrieve a list of documents written by a specific author
ProxiArticles = pd.DataFrame(columns = ['Author ID','Proxi Article ID'])
x = AuthorID
for x in AuthorID:
    resp = requests.get(f"http://api.elsevier.com/content/search/scopus?query=AU-ID({x})&field=dc:identifier&count=100",
                    headers={'Accept':'application/json',
                             'X-ELS-APIKey': "44f055d2666f0d63b928f6d10e2f77d2"})

    results = resp.json()

    results = json.dumps(resp.json(),
                 sort_keys=True,
                 indent=4, separators=(',', ': ')) 
    
    json_acceptable_string = results.replace("'", "\"")
    dictionary = json.loads(json_acceptable_string)

    for a in range(0,len(dictionary['search-results']['entry'])):
        ProxiArticle = dictionary['search-results']['entry'][a]['dc:identifier']
        ProxiArticles = ProxiArticles.append({'Author ID': x,'Proxi Article ID': ProxiArticle},ignore_index = True)    

ProxiArticles.to_excel('AuthorData.xlsx')        


