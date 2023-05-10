from flask import Flask
import json

from models.user import User

app = Flask(__name__)

user = User()

# index route
@app.route('/', methods=['GET'])
def index():
    return "Bienvenue dans notre application de messagerie (partie API)"

# login route
@app.post('/api/login')
def login_user():
    result = user.login()
    return json.dumps(result)


if __name__ == "__main__":
    app.run()