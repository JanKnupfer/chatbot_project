#!/usr/bin/env python
# coding: utf-8

# In[ ]:
from IPython import get_ipython

get_ipython().run_line_magic('pip', 'install elasticsearch')

# In[ ]:


from elastic_search.utilities.login import login
import json
import time

# # Variables

# In[ ]:


# Get index name
with open('..\\elastic_search\\utilities\\index_config.json') as file:
    index_name = json.load(file)[0]['index_name']

# # Connect to elastic search

# In[ ]:


es = es = login()


# # delete index if it already exists

# In[ ]:


print('Creating new database...')
print('Deleting existing index')

if es.indices.exists(index=index_name):
    status = es.indices.delete(index=index_name)
    if status.body['acknowledged']:
        print('Deleted existing index')
    else:
        print('Could not delete index')

else:
    print('Not existing index found')


# # create new index

# In[ ]:


print('Creating index...')

with open('..\\elastic_search\\utilities\\index_config.json') as file:
    index_config = json.load(file)[1]

if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name, body=index_config, ignore=400)
    print('Created index', index_name)
else:
    print('Index already exists')


# # populate index

# In[ ]:


print("Populating index...")

wrong_status = False
with open('..\\elastic_search\\data\\wirtschaftsinformatik.json') as file:
    data = json.load(file)
    for document in data:
        status = es.index(index=index_name, body=document)
        if not status.meta.status == 201:
            wrong_status = True
            print('Something went possibly wrong')
            print('Expected status code 201 but was', status.meta.status)
            print(status)

time.sleep(5)
if not wrong_status and es.count() != 0:
    print("Index successfully populated")

