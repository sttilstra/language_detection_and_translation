import logging
import requests

import azure.functions as func

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    def tell_joke():
        request = requests.get("https://v2.jokeapi.dev/joke/Programming?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single")
        request.raise_for_status()
        response = request.json()
        return response["joke"]


    return func.HttpResponse(tell_joke())
