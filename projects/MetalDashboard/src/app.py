import src.pipe.extract
import src.pipe.load
import src.pipe.transform


from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
  return "Home Page"

if __name__ == "__main__":
  app.run()




