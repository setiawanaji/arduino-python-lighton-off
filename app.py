from flask import Flask
from routers.appBlueprint import appBlueprint

app = Flask(__name__)
app.register_blueprint(appBlueprint, url_prefix="/")
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)