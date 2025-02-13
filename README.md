# Meme Python Flask 

```bash
virtualenv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 app.py
python3 app_monitoring.py
```

To run with using docker
```bash
docker build -t meme-python-flask .
docker run -dit -p 5009:5000 meme-python-flask
```