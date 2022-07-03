from flask import Flask, request
from sentiment_analysis_service import start_sentiment_analysis


app = Flask(__name__)
app.debug = True


@app.route('/get_sentiment', methods=['POST'])
def get_sentiment():
    data = request.get_json()
    text = data['text']
    sentiment =start_sentiment_analysis(text)
    return {'sentiment' : sentiment,
            'code' : 200
    }

if __name__ == "__main__": 
    app.run(host="127.0.0.1", port=5000)