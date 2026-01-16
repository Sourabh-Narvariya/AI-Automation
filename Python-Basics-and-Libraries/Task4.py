#  Build a simple Flask app that serves a "Hello World" page with a form input.
from flask import Flask, render_template_string, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def hello_world():
    message = ""
    if request.method == 'POST':
        name = request.form.get('name', 'World')
        message = f"Hello, {name}!"
    return render_template_string('''
        <html>
            <body>
                <h1>{{ message or "Hello, World!" }}</h1>
                <form method="post">
                    <input type="text" name="name" placeholder="Enter your name">
                    <input type="submit" value="Submit">
                </form>
            </body>
        </html>
    ''', message=message)
if __name__ == '__main__':
    app.run(debug=True)