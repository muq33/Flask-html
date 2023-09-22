from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Define a dictionary of users and their passwords (for demonstration purposes)
users = {
    'user1': 'password1',
    'user2': 'password2',
}

# Authentication function
def check_auth(username, password):
    return username in users.keys() and password == users.get(username)

# Unauthorized access response
def unauthorized():
    return jsonify({'message': 'Unauthorized access'}), 401

# Protected route
@app.route('/protected', methods=['GET'])
def protected_resource(username):
    return jsonify({'message': 'This is a protected resource.', 'user': username})



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_auth(username, password):
            return protected_resource(username)
        else:
            return unauthorized()
    return render_template('login.html')
   
if __name__ == '__main__':
    app.run(debug=True)
