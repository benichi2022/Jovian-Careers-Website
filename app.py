from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('home.html')


#favicon using flask
# @app.route('/favicon.ico')
# def favicon():
#   return app.send_static_file('favicon.ico')

if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
