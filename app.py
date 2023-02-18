from flask import Flask, render_template, jsonify

app = Flask(__name__)
JOBS = [
  {'id':1,
   'title':'Front end',
   'location':'Lviv,UA',
   'salary':'$2000'
  },
  {'id':2,
   'title':'Back end',
   'location':'Horodok,UA',
   'salary':'$3000'
  },
  {'id':3,
   'title':'QA',
   'location':'Remote',
   'salary':'$1000'
  },
  {'id':4,
   'title':'Manager',
   'location':'Uhry,UA',
   'salary':'$10 000'
  },
]
@app.route("/")
def HomePage():
  return render_template('home.html',jobs = JOBS,my_name='Ігор Живчин')

@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)
  
