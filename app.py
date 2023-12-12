from json import load
from os import path, getcwd
from flask import Flask, request
from Cogs.auth import auth_cogs
from Cogs.home import home_cogs
from cantinaUtils.Database import DataBase 

app = Flask(__name__)
conf_file = open(path.abspath(getcwd()) + "/config.json", 'r')
config_data = load(conf_file)

# Connection aux bases de données
database = DataBase(user=config_data['database'][0]['database_username'],
                    password=config_data['database'][0]['database_password'], 
                    host=config_data['database'][0]['database_addresse'], 
                    port=int(config_data['database'][0]['database_port']))
database.connection()


@app.route('/')
def home():
    return home_cogs()


@app.route('/auth/<url_to_redirect>', methods=['GET', 'POST'])
@app.route('/auth/', methods=['GET', 'POST'])
def auth(url_to_redirect=None):
    return auth_cogs(request, database, url_to_redirect)


if __name__ == '__main__':
    app.run(port=config_data["port"])
