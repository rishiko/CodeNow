from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/execute', methods=['POST'])
def execute_code():
    code = request.form['code']
    result = subprocess.run(['python', '-c', code], capture_output=True, text=True)
    return result.stdout + result.stderr

if __name__ == '__main__':
    app.run(debug=True)
