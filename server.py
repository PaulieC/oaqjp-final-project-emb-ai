from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the emotion_detector function and store the response
    res = emotion_detector(text_to_analyze)

    # result_str = "For the given statement, the system response is "
    # for emotion, score in response.items():
    #     if (emotion !== "dominant_emotion"):
    #         result_str + emotion + ":" + score + ", "
    #     else:
    #         result_str + ". The dominant emotion is " + emotion

    return (
        f"For the given statement, the system response is "
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, "
        f"'fear': {res['fear']}, 'joy': {res['joy']} and "
        f"'sadness': {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

