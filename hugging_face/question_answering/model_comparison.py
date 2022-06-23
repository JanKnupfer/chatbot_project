import time

from transformers import pipeline

# All available models on huggingface.co/models tagged with the Task "Question Answering" and language "de"
models = [
    'deutsche-telekom/bert-multi-english-german-squad2',
    'deutsche-telekom/electra-base-de-squad2',
    'deepset/gelectra-base-germanquad',
    'deepset/gelectra-base-germanquad-distilled',
    'deepset/gelectra-large-germanquad',
    'Sahajtomar/German-question-answer-Electra',
    'Sahajtomar/GBERTQnA'
    ]


def main():
    for model_name in models:
        model_test(model_name)


def model_test(model_name):
    start_time = time.time()

    qas = pipeline(
        model=model_name,
        task='question-answering'
        )

    questions = [
        'Kann man ein Auslandssemester machen?',
        'Kan man ein Aulsandssemetser machen?',
        'In welche Länder kann man gehen?',
        'Kann man in die USA gehen?',
        'Wie viel kostet das 9€ Ticket?'
        ]
    answers = []
    score = []
    average_score = 0

    for q in questions:
        answer = qas(
            question=q,
            context="Der Studiengang Wirtschaftsinformatik bietet seinen Studierenden die Möglichkeit, in der Theoriephase ein Auslandssemester an einer Partneruniversität in Großbritannien, USA, Frankreich, Australien, Irland, Skandinavien und Singapur zu absolvieren. Ein solches Auslandssemester fügt sich nahtlos in den Studienablauf ein."
            )
        average_score += answer['score']
        answers.append(answer['answer'])
        score.append(answer['score'])

    average_score = average_score/len(questions)
    duration = time.time() - start_time

    print(f"Model {model_name} took {round(duration, 4)} seconds with an average score of {round(average_score, 4)}")
    for a, q, c in zip(answers, questions, score):
        print(f"Question: {q}, Answer: {a}, Confidence: {round(c, 4)}")

    print()


if __name__ == '__main__':
    main()
