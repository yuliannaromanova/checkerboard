from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def first():
    return render_template('index.html')

@app.route('/<int:num>')
def second(num):
    return render_template('index2.html', num = num)

@app.route('/<int:num1>/<int:num2>')
def third(num1, num2):
    return render_template('index3.html', num1 = num1, num2 = num2)


if __name__ =='__main__':
    app.run(debug=True)