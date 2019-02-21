import json
import urllib.request

import mechanicalsoup
import requests

urls = []
for i in range(0,1000):
    urls.append('https://api-digischool.kontinium.com/access/user/quiz/'+str(i)+'?embed=display')

# for validate : https://api-digischool.kontinium.com/access/user/questions/{id_questiion}/validate

result = ''
for it, url in enumerate(urls):
    try:
        with urllib.request.urlopen(url) as response:
            temps_res = ''
            json_question = json.loads(response.read())
            quiz_id = json_question['id']
            name = json_question['name']
            temps_res += '\n' + name.replace('\r\n', ' ') + '| id: + ' + str(quiz_id) + '\n'
            print(name)
            questions = json_question['questions']
            for question in questions:
                question_id = question['id']
                for q in question['subquestions']:
                    question_text = q['text']
                    temps_res += question_text.replace('\r\n', ' ') + '|'
                    print('--- ' + question_text)
                    for answer in q['possibleAnswers']:
                        answer_text = answer['text']
                        temps_res += answer_text.replace('\r\n', ' ') + '|'
                        print('------ ' + answer_text)
                    url_answer = 'https://api-digischool.kontinium.com/access/user/questions/' + str(question_id) + '/validate'
                    with requests.patch(url_answer, json={ str(q['id']): 0 }) as resp:
                        json_answer = json.loads(resp.text)
                        temps_res += '|ANSWERS|'
                        try:
                            for good_answer in json_answer['data'][str(q['id'])]['goodAnswer']:
                                answer = [a['text'] for a in q['possibleAnswers'] if a['id'] == good_answer][0]
                                print(answer)
                                temps_res += answer.replace('\r\n', ' ') + '|'
                            temps_res += '\n'
                        except Exception as e:
                            temps_res = ''
            result += temps_res
            print(str(it * 100 / 1000) + ' %')
    except Exception as e:
        pass

with open('questions.csv', 'w') as file:
    file.write(result)

# quiz call : 62
#
# patch: url: 612 => id question
# content: 590	2359 -> id de la reponse
#             --> id subquestion
#
# recup 590
