#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from elastic_search.utilities.login import login
from utilities.es_search import search_es
from transformers import pipeline
import json

# # Variables

# In[ ]:


# Get index name
with open('..\\elastic_search\\utilities\\index_config.json') as file:
    index_name = json.load(file)[0]['index_name']

# # Connect to elastic search

# In[ ]:


es = login()

# # Search in index

# In[ ]:


question_text = 'Was steht im Fokus des Studiums?'

es_answers = search_es(es_instance=es, index_name=index_name, question_text=question_text, number_of_results=10)

print(f'Question: {question_text}')
print(f'Query Duration: {es_answers["took"]} milliseconds')
print('Title, Relevance Score:')
[(hit['_source']['document_title'], hit['_score']) for hit in es_answers['hits']['hits']]

# In[ ]:


qas = pipeline(
    model='deutsche-telekom/bert-multi-english-german-squad2',
    task='question-answering'
    )

# In[ ]:


answer = qas(
    question=question_text,
    context=es_answers['hits']['hits'][0]['_source']['document_text']
    )
print(answer)

# In[ ]:


answer_dict = dict([
    ("question", question_text),
    ("answer", answer["answer"]),
    ("score", answer['score']),
    ('link', es_answers['hits']['hits'][0]['_source']['link'])
    ])

with open('answer.json', 'w') as file:
    json.dump(answer_dict, file, ensure_ascii=False)
