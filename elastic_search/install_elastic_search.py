#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# In[3]:


import zipfile
import os
import wget
import sys
from os.path import exists

# In[4]:


# Variables
store_dir = os.getcwd()
file_name_zip = 'elasticsearch.zip'
file_path_zip = store_dir + '\\' + file_name_zip
extraction_directory = store_dir + '\\elasticsearch'

download_url = 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.2.2-windows-x86_64.zip'


# # Download

# In[ ]:


# create this bar_progress method which is invoked automatically from wget
def bar_progress(current, total, width=80):
    progress_message = "Downloading: %d%% [%d / %d] bytes"%(current/total*100, current, total)
    # Don't use print() as it will print in new line every time.
    sys.stdout.write("\r" + progress_message)
    sys.stdout.flush()


file_exists = exists(store_dir + '\\' + file_name_zip)
if not file_exists:
    wget.download(download_url, out=file_name_zip, bar=bar_progress);
    print("File already downloaded")

# # Unzip

# In[ ]:


file_exists = exists(store_dir + '\\elasticsearch\\elasticsearch-8.2.2')
with zipfile.ZipFile(file_path_zip, 'r') as zip_ref:
    if file_exists:
        print("File already extracted")
    else:
        zip_ref.extractall(extraction_directory)

# # Start es

# In[ ]:


print("Starting elastic search")
print("Wait until elastic search displays your login password")
print("YOU HAVE TO COPY THE PASSWORD FROM THE COMMAND PROMPT INTO credentials.json!")

os.system('start /wait cmd /c "elasticsearch\\elasticsearch-8.2.2\\bin\\elasticsearch.bat"')
