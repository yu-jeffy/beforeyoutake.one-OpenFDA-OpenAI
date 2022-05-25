#Your API Key is:NzqneujAaEFAalp5LYumL13pYRyCOgXh0zr6Xkdi

import requests
import json

import os
import openai

from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app._static_folder = 'static'
@app.route('/')

def index():
   return render_template('index.html')




def getDrugInfo(drugName):

    queryURL = "https://api.fda.gov/drug/label.json?search=description:" +  drugName + "&limit=1"

    queryResult = requests.get(queryURL)

    drugInfoRawText = json.loads(queryResult.text)

    drugInfoOutput = dict()

    for item in drugInfoRawText['results']:
        #drugInfoOutput['Description:'] = [drugInfoRawText['results'][0]['description']]
        #for item in drugInfoRawText['results'][0]['information_for_patients']:
            #drugInfoOutput['Information for Patients:'] = [drugInfoRawText['results'][0]['information_for_patients']]
        drugInfoOutput['Indications and Usage:'] = [drugInfoRawText['results'][0]['indications_and_usage']]
        #drugInfoOutput['Adverse Reactions'] = [drugInfoRawText['results'][0]['adverse_reactions']]
        #drugInfoOutput['Box Warnings'] = [drugInfoRawText['results'][0]['boxed_warning']]
        #drugInfoOutput['Abuse and Dependence'] = [drugInfoRawText['results'][0]['drug_abuse_and_dependence']]


    return drugInfoOutput



# Load your API key from an environment variable or secret management service
openai.api_key = "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"



@app.route('/getInfo/', methods=['POST', 'GET'])
def getDrugSummary():

    input = request.form.to_dict()

    drugName = input["inputDrugName"]

    drugInfoOutput = getDrugInfo(drugName)

    outputList = []

    for x in drugInfoOutput:
        entryTemp = str(x) + " " + str(drugInfoOutput[x])
        outputList.append(entryTemp)

    drugInfoPlaintext = ''.join(outputList)

    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt="Describe this drug in detail: " + drugInfoPlaintext,
      temperature=0,
      max_tokens=256,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    outputResponse = str(response['choices'][0]['text'])

    outputResponse = outputResponse.replace("\n", "")

    return render_template('index.html', outputResponse = outputResponse, drugName = drugName)





if __name__ == '__main__':
   app.run(debug=True)
