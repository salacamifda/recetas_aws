from flask_app import app

#Importando Controlador
from flask_app.controllers import users_controller, recipes_controller

#Pasos a seguir:
#pipenv install flask pymysql
#pipenv shell
#python server.py -> python3, py o python

if (__name__=="__main__"):
    app.run(debug=True)

    #Para ingresar usuario: ca@codingdojo.com y contra: Camicami