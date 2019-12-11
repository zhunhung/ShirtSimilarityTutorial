import logging
from . import keras_shirt_sim
import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    file_sent = None
    try:
        # Retrieve photo via HTTP Request
        file_sent = req.files['file']
        file_sent.seek(0)
    except Exception as e:
        return func.HttpResponse(
             str(e),
             status_code=400
        )

    filename = file_sent.filename
    # If file received
    if file_sent:

        # Get the most similar shirt and similarity score
        similar_shirt, sim_score = keras_shirt_sim.find_similar(file_sent.read())

        # There exists a shirt above certain threshold
        if similar_shirt:
            return func.HttpResponse(
                json.dumps([{
                    "result": similar_shirt, 
                    "filename":filename,
                    "score": sim_score
                    }]),
                status_code=200)

        # No similar shirt found
        return func.HttpResponse(
                json.dumps([{
                    "result": 'No similar shirt found', 
                    "filename":filename
                    }]),
                status_code=200)

    # No photo received
    else:
        return func.HttpResponse(
             "Please pass a file",
             status_code=400
        )
