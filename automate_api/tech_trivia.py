import requests
import html
import csv


url = "https://opentdb.com/api.php"

amount = input('How many questions do you want? ')
difficulty = input('What difficulty do you want? (easy, medium, hard) ')

request_params = {
    'amount': amount,
    'category': 18,
    'difficulty': difficulty
}
response = requests.get(url, headers={'Accept':'application/json'}, params=request_params)
response_json = response.json()
data = response_json['results']

qna = [['Question', 'Answer']]

for item in data:
    q = html.unescape(item['question'])

    if item['type'] == 'boolean':
        q = 'True or False? ' + q

    a = html.unescape(item['correct_answer'])  
    qna.append([q, a])
# print(qna)

with open('tech_trivia.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(qna)