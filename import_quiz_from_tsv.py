
import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Eolasquiz_back.settings")
import django
django.setup()

from quiz.models import Quiz, Question, Answer

Quiz.objects.all().delete()
with open("questions1_20000.tsv", "r", encoding="utf8") as f:
    data = f.readlines()
    current_quiz = None
    for line_number, line in enumerate(data):
        line = line.split('\t')
        if line[0] == '':
            continue
        if line[1].startswith('id: +'):
            quiz_title = line[0]
            current_quiz = Quiz(user_id=1, category='not set', difficulty=1, description='No description')
            current_quiz.name = quiz_title
            current_quiz.save()
            continue
        quiz_question = line[0]
        question_list = []
        current_question = Question(quiz=current_quiz, text=quiz_question)
        current_question.save()
        question_list.append(current_question)
        answer_list = []
        for it, answer in enumerate(line[1:]):
            if answer == '':
                is_result = True
                for correct in [l for l in line[it + 3:] if l != '\n']:
                    good_answer = correct
                    for ans in answer_list:
                        if ans.text == good_answer:
                            ans.is_correct = True
                            ans.save()

                for q in question_list:
                    q.quiz = current_quiz
                    q.save()
                for a in answer_list:
                    a.save()
                break
            quiz_anwser = answer
            answer_object = Answer(text=quiz_anwser, is_correct=False, question=current_question)
            answer_object.save()
            answer_list.append(answer_object)
        print(str( line_number * 100 / len(data)) + ' % ' + str(it))
