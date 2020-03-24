from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

from api.services.contact_management import ContactManagement

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///hcms_db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
api = Api(app)

api.add_resource(ContactManagement, "/data/contact/v1")


@app.route("/", methods=["POST", "GET"])
def index():
    app.run(debug=True)


if __name__ == "__main__":
    app.run(debug=True)
