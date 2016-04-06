from .controllers.twitter import search

def router(app):
  @app.route('/')
  def index():
    return 'OK'

search()