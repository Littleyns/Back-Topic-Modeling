import PyPDF4
import os
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
import io
import shutil

import re
from tika import parser
from bs4 import BeautifulSoup
from io import StringIO
import bz2
import zipfile
import numpy as np
#importing names of all the articles
listnames = os.listdir("process/Articles")
#converting process functions
def digitize_pdf(file_path):
    file_data = []
    _buffer = StringIO()
    data = parser.from_file(file_path, xmlContent=True)
    xhtml_data = BeautifulSoup(data['content'], features="lxml")
    for page, content in enumerate(xhtml_data.find_all('div', attrs={'class': 'page'})):
        #print('Parsing page {} of pdf file...'.format(page+1))
        _buffer.write(str(content))
        parsed_content = parser.from_buffer(_buffer.getvalue())
        _buffer.truncate()
        file_data.append({'id': str(page+1), 'content': parsed_content['content']})
    return file_data

def clean_document(doc):
    for i in reversed(range(1,len(doc))) :
        content = doc[i]['content']
        sustract = doc[i-1]['content']
        modified_content = content.replace(sustract, "")
        doc[i]['content'] = modified_content
    return doc
def convert(listnames):
    for j in range(len(listnames)):
        path = 'process/Articles/' + listnames[j]
        tika = digitize_pdf(path)
        # need to clean tika data
        tika = clean_document(tika)
        for i in range(len(tika)):

            with io.open("process/Articlestxt/" + listnames[j][0:-4] + ".txt", "a", encoding="utf-8") as f:
                f.write(tika[i]['content'])

    shutil.make_archive("process/static/Articlestxt", 'zip', "process/Articlestxt")
    print("success")
