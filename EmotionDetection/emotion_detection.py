import requests
import json

def emotion_detector(text_to_analyse):
    # Define the URL for the emotion analysis API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json=myobj, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)

    # extract emotion scores
    predicted_emotion_dict = formatted_response['emotionPredictions'][0]['emotion']

    # emotion dict definition
    emotion_dict = {'anger': 0,
    'disgust': 0,
    'fear': 0,
    'joy': 0,
    'sadness': 0,
    'dominant_emotion': '<name of the dominant emotion>'}

    # find dominant emotion
    dominant_emotion_score = 0.0

    for emotion, score in predicted_emotion_dict.items():
        # updated emotion score and name with each iter
        emotion_dict[emotion] = score
        if (score > dominant_emotion_score):
            #update dominant emotion only when the score is higher than our current highest score
            dominant_emotion_score = score
            emotion_dict['dominant_emotion'] = emotion

    return emotion_dict