from flask import Flask, render_template

app = Flask(__name__)
    

@app.route('/home')
def index2():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

# @app.route('/greet')
# def greet():
#     name = "Ukanah Dean Onesi"
#     return render_template('greeting.html', name=name)
@app.route('/<name>')
def greet(name):
    name = name
    return render_template('greeting.html', name=name)

@app.route('/<first_name>/<last_name>')
def greet2(first_name, last_name):
    full_name = f'{first_name} {last_name}'
    return render_template('greeting.html', name=full_name)

if __name__ == "__main__":
    app.run(debug=True)