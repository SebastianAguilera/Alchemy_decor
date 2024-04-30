from flask import jsonify, Blueprint

#Se define un blueprint llamado home
home = Blueprint('home', __name__) 


@home.route('/', methods=['GET'])
def index():
  resp = jsonify("ok")
  resp.status_code = 200 #estado correcto del codigo
  return resp 
