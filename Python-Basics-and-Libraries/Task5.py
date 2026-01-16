# Create a Flask form to accept a name and greet the user (HTML + Python).
from flask import Flask, render_template_string, request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def greet_user():
    greeting = ""
    if request.method == 'POST':
        name = request.form.get('name', 'Guest')
        greeting = f"Hello, {name}!"
    return render_template_string('''
        <html>
            <body>
                <h1>{{ greeting or "Welcome!" }}</h1>
                <form method="post">
                    <input type="text" name="name" placeholder="Enter your name">
                    <input type="submit" value="Greet ">
                </form>
            </body>
        </html>
    ''', greeting=greeting)
if __name__ == '__main__':
    app.run(debug=True)

