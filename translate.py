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

    path = '/translate'
    url_translate = endpoint + path


    translate_from = req.params.get('translate_from')
    logging.info(translate_from)

    translate_to = req.params.get('translate_to')
    logging.info(translate_to)

    req_body_bytes = req.get_body()
    logging.info(req_body_bytes)

    user_statement = req_body_bytes.decode("utf-8")
    logging.info(user_statement)


    params_translate = {
    'api-version': '3.0',
    'from': translate_from,
    'to': translate_to
    }
    

    body_translate = [{
    'text': user_statement
    }   ]

    request_translate = requests.post(url_translate, params=params_translate, headers=headers, json=body_translate)
    request_translate.raise_for_status()
    response_translate = request_translate.json()

    response_translate_text = response_translate[0]["translations"][0]["text"]

    return func.HttpResponse(response_translate_text)
