from .controllers.twitter import search

def router(app):
  @app.route('/')
  def index():
    return 'OK'

  @app.route('/twitter/<hashtag>')
  def search_twitter(hashtag):
    return search(hashtag)