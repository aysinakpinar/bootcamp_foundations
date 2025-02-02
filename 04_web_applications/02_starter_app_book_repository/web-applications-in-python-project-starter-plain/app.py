import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"


@app.route('/greet', methods=['GET'])
def get_hello():
    name = request.args["person"]
    return f"Hello {name}!"

@app.route('/greet', methods=['POST'])
def post_hello():
    name = request.form["person"]
    return f"Hello {name} via POST!"

@app.route('/submit', methods=['POST'])
def post_submit():
    name = request.form["name"]
    message = request.form["message"]
    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def get_wave():
    name = request.args["name"]
    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def count_vowels():
    text = request.form['text']
    count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for char in text:
        if char in vowels:
            count +=1
    return f'There are {count} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def sort_names():
    names = request.form['names']
    if names == '':
        return "There is no name to sort."
    else:
        names_list = names.split(",")
        sorted_names_list = sorted(names_list)
        return ','.join(sorted_names_list)

@app.route('/add-names', methods = ['GET'])
def add_names():
    inital_names_list = ['Julia', 'Alice', 'Karim',]
    names = request.args['names']
    if names == '':
        return 'There is no name to add!'
    else:
        names_list = names.split(',')
        for name in names_list:
            inital_names_list.append(name)
        return ', '.join(inital_names_list)

@app.route('/add-sort-names', methods = ['GET'])
def add__sort_names():
    inital_name_list = ['Julia', 'Alice', 'Karim']
    new_names = request.args['names']
    if new_names == '':
        return 'There is no name to add!'
    else:
        new_names_list = new_names.split(',')
        for name in new_names_list:
            inital_name_list.append(name)
            sorted_name_list = sorted(inital_name_list)
        return ', '.join(sorted_name_list)

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

