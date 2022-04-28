#! python3
# finds corresponding data.jet file in QuiplashQuestion folder for each prompt in QuiplashQuestion.jet and compares the prompt in data.jet with prompt in QuiplashQuestion.jet
import os, json
os.chdir(os.path.realpath(__file__).replace('Quiplash2_translationChecker.py', ''))

questionsMain = json.load(open(os.path.join('Quiplash2', 'content', 'QuiplashQuestion.jet'), 'r', encoding='utf-8'))
output = {}
for i in range(len(questionsMain['content'])):
    textID = str(questionsMain['content'][i]["id"])
    data = json.load(open(os.path.join('Quiplash2', 'content', 'QuiplashQuestion', textID, 'data.jet'), 'r', encoding='utf-8'))
    translatedText = questionsMain['content'][i]["prompt"]
    untranslatedText = data["fields"][5]["v"]
    if translatedText != untranslatedText:
        print(textID + ", " + untranslatedText)