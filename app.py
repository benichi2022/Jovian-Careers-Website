from flask import Flask, render_template, jsonify

app = Flask(__name__)

Jobs = [{
    "id": 1,
    "title": "Data Analyst",
    "location": "Bengaluru, India",
    "salary": " Rs. 10,000,000"
}, {
    "id": 2,
    "title": "Data Scientist",
    "location": "Delhi, India",
    "salary": " Rs. 15,000,000"
}, {
    "id": 3,
    "title": "Frontend Engineeri",
    "location": "Remote",
    "salary": " Rs. 12,000,000"
}, {
    "id": 4,
    "title": "Backend Engineer",
    "location": "San Franscico, USA",
    "salary": " $12,000"
}]


@app.route('/')
def index():
  return render_template('home.html', jobs=Jobs)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(Jobs)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
