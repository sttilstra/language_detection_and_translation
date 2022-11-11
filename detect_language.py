import logging
import requests
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential
from urllib.parse import parse_qs


import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    key = "<key>"
    endpoint = "<endpoint>"
    location = "<location>"

    headers = {
        'Ocp-Apim-Subscription-Key': key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json'
    }

    req_body_bytes = req.get_body()
    logging.info(req_body_bytes)

    user_statement = req_body_bytes.decode("utf-8")
    logging.info(user_statement)


    # this section detects the language from the initial interaction
    path_detect = '/detect'
    url_detect = endpoint + path_detect

    params_detect = {
        'api-version': '3.0'
    }

    body_detect = [{
        'text': user_statement
    }]

    request_detect = requests.post(url_detect, params=params_detect, headers=headers, json=body_detect)
    request_detect.raise_for_status()
    response_detect = request_detect.json()
    detected_language = response_detect[0]["language"]

    return func.HttpResponse(detected_language)
