import json


def is_basic_question(question):
    return any(question.lower() in default_question.lower() for default_question in basic_questions)


def basic_answer(question):
    y = [s for s in basic_questions if question.lower() in s.lower()]
    question = y[0]
    answer = basic_questions.get(question)

    return json.dumps({
        'status': 'Basic answer found',
        'statuscode': '200',
        'question': question,
        'answer': answer,
        'score': "-",
        'link': ''
        })


basic_questions = {
    "Hilfe": "Du kannst mir Fragen stellen und ich versuche eine präzise Antwort zu finden. "
             "Stelle die Fragen bitte als Ausformulierten Text und nicht nur einzelne Worte.",
    "Wie heißt du?": "Mein Name ist Bert. Ich bin ein Roboter, der dir die Fragen beantwortet.",
    "Hallo": "Hallo, ich bin ein Bot.",
    "Wie geht es dir?": "Gut, ich bin ein Bot.",
    "Was kannst du?": "Ich kann dir helfen, Fragen zu beantworten.",
    "Kann ich dir Fragen stellen?": "Du kannst mich alles zum Studiengang Wirtschaftsinformatik fragen",
    "Was kann ich dich fragen?": "Alles zum Thema Wirtschaftsinformatik",
    }
