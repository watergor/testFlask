from flask import Flask, render_template, jsonify
from database import load_jobs_from_db,load_job_fron_db

app = Flask(__name__)

@app.route("/")
def HomePage():
  jobs = load_jobs_from_db()
  return render_template('home.html',jobs = jobs,my_name='Ігор Живчин')

@app.route("/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)
  
@app.route("/job/<id>")
def show_job(id):
  job = load_job_fron_db(id)
  
  if not job:
    return 'Not Found',403
  else:
    return render_template('jobpage.html',job =job)

if __name__ == "__main__":
  app.run(host = "0.0.0.0", debug = True)
  
