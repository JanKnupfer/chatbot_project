# Question Answer System

This is a Question Answer System that allows you to ask questions about the website of the DHBW Stuttgart about
Wirtschaftsinformatik and get answers.
It uses a Elasticsearch database to store the content
of https://www.dhbw-stuttgart.de/studium/bachelor-studienangebot/wirtschaft/wirtschaftsinformatik-application-management
.
To get the answer of your question it uses a Hugging Face model to get the exact answer out of the document from
Elasticsearch.

## How to run the programm

If you want to run this application yourself download the repository.
Run the install_elastic_search.py script, then the load_data_into_elastic_search.py script.
Start the Django server with the command:

## How to start the Frontend

1. Setup your own environment (venv name of environment): py -m venv venv
2. Change to virtual environment: env\Scripts\activate
3. Install django: pip install django
4. Start django Project: django-admin startproject pychar
5. Create new Django App: python manage.py startapp chatbotUI
6. Start Server: python manage.py runserver

[//]: # (TODO)
