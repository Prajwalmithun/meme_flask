from flask import Flask, jsonify, render_template
import requests
import json
from prometheus_client import start_http_server, Counter, Summary, generate_latest
from prometheus_client.exposition import CONTENT_TYPE_LATEST

app = Flask(__name__)

# FlaskInstrumentor().instrument_app(app)

# Define Prometheus metrics
REQUEST_COUNT = Counter("flask_requests_total", "Total number of requests", ["method", "endpoint"])
REQUEST_LATENCY = Summary("flask_request_latency_seconds", "Request latency in seconds")


def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.get(url).text)
    meme_large_image = response['preview'][-1]
    # print(json.dumps(response, indent=4))
    # print(meme_large_image)
    return meme_large_image

@app.route('/')
def home():
    REQUEST_COUNT.labels(method="GET", endpoint="/").inc()
    meme = get_meme()
    with REQUEST_LATENCY.time():
        return render_template('index.html', meme=meme)

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

app.run(host='0.0.0.0', port=5001) 