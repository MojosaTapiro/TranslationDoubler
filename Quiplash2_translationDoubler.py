#! python3
# finds corresponding data.jet file in QuiplashQuestion folder for each prompt in QuiplashQuestion.jet and replaces untranslated prompt in data.jet with translation from QuiplashQuestion.jet
import os, json
os.chdir(os.path.realpath(__file__).replace('Quiplash2_translationDoubler.py', ''))

questionsMain = json.load(open(os.path.join('Quiplash2', 'content', 'QuiplashQuestion.jet'), 'r', encoding='utf-8'))
output = {}
for i in range(len(questionsMain['content'])):
    textID = str(questionsMain['content'][i]["id"])
    data = json.load(open(os.path.join('Quiplash2', 'content', 'QuiplashQuestion', textID, 'data.jet'), 'r', encoding='utf-8'))
    translatedText = questionsMain['content'][i]["prompt"]
    untranslatedText = data["fields"][5]["v"]
    data["fields"][5]["v"] = translatedText
    writer = open(os.path.join('Quiplash2', 'content', 'QuiplashQuestion', textID, 'data.jet'), 'w', encoding='utf-8')
    json.dump(data, writer)

