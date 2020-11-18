from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask
from flask import Response
from flask import render_template


app = Flask(__name__)


def cities_import() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'Nj1T531153@!',
        'host': 'localhost',
        'port': '3306',
        'database': 'new_schema1'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblcitiesimport1')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result

@app.route('/')
def index():
    user = {'username':'Pria'}
    cities_data = cities_import()

    return render_template('index.html',title='Home',user=user,cities=cities_data)


@app.route('/api/cities')
def cities() -> str:
    js = json.dumps(cities_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run()
