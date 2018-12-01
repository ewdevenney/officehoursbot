from flask import Flask
app = Flask(__name__)
PORT = 4390

@app.route('/')
def homepage():
  return "Howdy hacker!!"

@app.route('/scheduleme', methods=['POST'])
def ready():
  return 'I would like to schedule that, but I haven\'t quite figured out how...'

if __name__ == '__main__':
  app.run(debug=True, port=PORT)