from crypt import methods
from flask import Blueprint
from controllers.appController import index

appBlueprint = Blueprint("app", __name__)
appBlueprint.route("/",methods=["GET"])(index)
