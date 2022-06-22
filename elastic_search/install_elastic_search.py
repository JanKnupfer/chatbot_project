import os
import zipfile
from os.path import exists

import wget

from elastic_search.utilities.progress_bar import bar_progress

# Variables
working_dir = os.getcwd()
file_name_zip = 'elasticsearch.zip'
file_path_zip = working_dir + '\\' + file_name_zip
extraction_directory = working_dir + '\\elasticsearch'
download_url = 'https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-8.2.2-windows-x86_64.zip'


def main():
    download()
    unzip()
    start_elasticsearch()


def download():
    global file_exists
    file_exists = exists(working_dir + '\\' + file_name_zip)
    if not file_exists:
        wget.download(download_url, out=file_name_zip, bar=bar_progress);
        print("File already downloaded")


def unzip():
    global file_exists
    file_exists = exists(working_dir + '\\elasticsearch\\elasticsearch-8.2.2')
    with zipfile.ZipFile(file_path_zip, 'r') as zip_ref:
        if file_exists:
            print("File already extracted")
        else:
            zip_ref.extractall(extraction_directory)


def start_elasticsearch():
    print("Starting elastic search...")
    print("Wait until elastic search displays your login password")
    print("YOU HAVE TO COPY THE PASSWORD FROM THE COMMAND PROMPT INTO credentials.json!")
    os.system('start /wait cmd /c "elasticsearch\\elasticsearch-8.2.2\\bin\\elasticsearch.bat"')


if __name__ == '__main__':
    main()
