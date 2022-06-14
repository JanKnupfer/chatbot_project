import wget
import zipfile
from os.path import exists
from elastic_search.utilities.progress_bar import bar_progress

import os

# Variables
store_dir = os.getcwd() + '\\elastic_search'
file_name_zip = 'elasticsearch.zip'
file_path_zip = store_dir + '\\' + file_name_zip
extraction_directory = store_dir + '\\elasticsearch'

download_url = 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.2.2-windows-x86_64.zip'

# # Download


file_exists = exists(store_dir + '\\' + file_name_zip)
if not file_exists:
    wget.download(download_url, out=file_name_zip, bar=bar_progress);
    print("File already downloaded")

# # Unzip


file_exists = exists(store_dir + '\\elasticsearch\\elasticsearch-8.2.2')
with zipfile.ZipFile(file_path_zip, 'r') as zip_ref:
    if file_exists:
        print("File already extracted")
    else:
        zip_ref.extractall(extraction_directory)

# # Start es

print("Starting elastic search")
print("Wait until elastic search displays your login password")
print("YOU HAVE TO COPY THE PASSWORD FROM THE COMMAND PROMPT INTO credentials.json!")

os.system('start /wait cmd /c "elasticsearch\\elasticsearch-8.2.2\\bin\\elasticsearch.bat"')
