from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from Dheevara.resources.Hello import Hello




# creating the flask app
app = Flask(__name__)
CORS(app)
# creating an API object
api = Api(app)
api.add_resource(Hello, '/dheevara/v1')


# driver function
if __name__ == '__main__':
    app.run(debug=True)

