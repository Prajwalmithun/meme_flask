from flask import Flask, jsonify, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url).text)
    meme_large_image = response['preview'][-1]
    # print(json.dumps(response, indent=4))
    # print(meme_large_image)
    return meme_large_image

@app.route('/')
def home():
    meme = get_meme()
    return render_template('index.html', meme=meme)

app.run(host='0.0.0.0', port=5000) 

