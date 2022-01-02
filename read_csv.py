import urlopen
import requests 
from bs4 import BeautifulSoup

import csv
import pandas as pd

import regex as re

complete_data, invalid_data = [], []


def preprocess_text(text):
    
    text = re.sub(r'[^0-9a-zA-Z]', ' ', text)
    text = re.sub(r'_', ' ', text)
    return " " .join(text.split())
    

def get_contents(data):
    
    modify_data = {}

    for name, url in data.items(): 

      # Read the homepage of the teacher      
      try:
         html = requests.get(url)
         html.raise_for_status()
         modify_data = {} 
         soup = BeautifulSoup(html.text, 'html.parser')
      
         # Get phone number / email
         get_info, personal_info = ['Email', 'email'], []
         for string in soup.body.strings:
             if 'Email' in string or 'email' in string:
                personal_info.append(string.strip())
      
         # Save only relevant content for the teacher
         text_data = [preprocess_text(string) for string in soup.body.strings if preprocess_text(string)!='']
         text_data = ' '.join(text_data)

         # Add the data to a dict
         modify_data['name'] = name
         modify_data['personal_info'] = personal_info
         modify_data['content'] = text_data  
         complete_data.append(modify_data)

      except:
         invalid_data.append((name, url))

    text_file = open("data/error_file.txt","w")
    for val in invalid_data:
        text_file.write(str(val) + "\n")

    text_file = open("data/output.txt","w")
    text_file.write(str({'complete_data':complete_data}))


def main_csv():
    # Read csv file 
    csv_file = pd.read_csv('data/csv_data/csrankings.csv') # ['name', 'affiliation', 'homepage', 'scholarid']
    data = dict(zip(csv_file.name, csv_file.homepage))
    
    # Use a sample size
    test_size = 20
    test_data = dict(list(data.items())[:test_size])
    #print(test_data)

    get_contents(test_data)

