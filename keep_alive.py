from flask import Flask, render_template
from threading import Thread
#import json

app = Flask('')

@app.route('/')#,methods=['POST'])

#def Vote():
  #data = json.loads(request.data)
  #print(data)
  #return data
  
def index():
    return render_template('index.html')

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
  t = Thread(target=run)
  t.start()

