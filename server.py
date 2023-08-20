from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode = 'a') as txt:
        name = data['name']
        email = data['email']
        message = data['message']
        file = txt.write(f'\n Name: {name}, Email: {email}, Message: {message}')

def write_to_csv(data):
    with open('database.csv', newline = '', mode = 'a') as database:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return 'Thank you! I will get in touch with you shortly!'
        except:
            'Information was not saved to the database.'
    else:
        return 'Oops! Something went wrong. Try again.'

if __name__ == '__main__':
   app.run(debug = True)