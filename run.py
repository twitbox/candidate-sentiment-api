from flask import Flask

app = Flask(__name__)

FLASK_CONFIG = {
  'DEBUG': True
}
app.config.update(FLASK_CONFIG)

if (__name__):
  app.run(port=8000, host='0.0.0.0')