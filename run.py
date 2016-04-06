from flask import Flask
from app import router

app = Flask(__name__)
FLASK_CONFIG = {
  'DEBUG': True
}
app.config.update(FLASK_CONFIG)

router(app)

if (__name__):
  app.run(port=8000, host='0.0.0.0')