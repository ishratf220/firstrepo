import os
from bs4 import BeautifulSoup as bs
import pandas as pd
import csv
dictionary = {}
df = pd.DataFrame.from_dict(dictionary, orient="index")
pathToDir = r'C:\Users\Ishrat Fatima\Desktop\court\_Pagina_0-500\_Pagina_0-500'
arr = os.listdir(pathToDir)
for newFile in os.listdir(pathToDir):

    fileName = os.path.join(pathToDir, newFile)
    # create soup.
    fileNameOpen = open(fileName, encoding="utf8")
    soup = bs(fileNameOpen, 'html.parser')
    try:
        sentence = soup.find('p', {'class': 'popolo'})
        sentenceChild = sentence.text
        dictionary['Contro'] = sentenceChild
    except:
        pass
#    try:
#        pqm = soup.find('p', {'class': 'fatto'})
#        pqmChild = pqm.text
#        dictionary['PQM'] = pqmChild
#    except:
#        pass
#    try:
#        pqmName = pqmChild.find_next('p', {'class': 'popolo'}).text + ' and others'
#        dictionary['Name of the pqm'] = pqmName
    
#    except:
#        pass
    df = pd.DataFrame.from_dict(dictionary, orient="index")
    outputFile = open('C:\\Users\\Ishrat Fatima\\Desktop\\court\\csvFiles\\Files_' + str(arr.index(newFile)) + ".csv", "w")
    df.to_csv(outputFile)
    outputFile.close()
