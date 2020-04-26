from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'templates'

@app.route('/')
@app.route('/home_page.html')
def home():
   return render_template('home_page.html')

@app.route('/locality_drop_down.html')
def locality_chart():
   return render_template('locality_drop_down.html')

@app.route('/prediction_drop_down.html')
def prediction_risk():
   return render_template('prediction_drop_down.html')

@app.route('/resources.html')
def resources():
   return render_template('resources.html')

@app.route('/about.html')
def about():
   return render_template('about.html')

@app.route('/california_data.html')
def califorina_data():
   return render_template('california_data.html')

@app.route('/florida_data.html')
def florida_data():
   return render_template('florida_data.html')

@app.route('/california_month.html')
def california_month():
   return render_template('california_month.html')

@app.route('/florida_month.html')
def florida_month():
   return render_template('florida_month.html')

if __name__ == '__main__':
   app.run()