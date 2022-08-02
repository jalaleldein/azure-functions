import datetime
import json
import logging
import requests
import azure.functions as func

def main(mytimer: func.TimerRequest, outputBlob: func.Out [str])  -> None:
    response = requests.get('http://api.weatherapi.com/v1/current.json?key=5bd8a9107488438db57171650212212&q=szeged&aqi=no')
    logging.info(response.content)
    outputBlob.set(response.content)
    