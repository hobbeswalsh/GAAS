from flask import Flask
import random
import string


key = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in range(50))

app = Flask(__name__)
app.secret_key = key
