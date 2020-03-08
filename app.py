from flask import Flask, g, jsonify, make_response, request
from flask_restplus import Api, Resource, fields
import sqlite3
from os import path

app = Flask(__name__)
api = Api(app, version='1.0', title='Data Service for NSW government schools information by suburb',
          description='This is a Flask-Restplus data service that allows a client to consume APIs related to NSW government schools information by suburb.',
          )

#Database helper
ROOT = path.dirname(path.realpath(__file__))
def connect_db():
    sql = sqlite3.connect(path.join(ROOT, "governmentschools.db"))
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@api.route('/all')
class GovernmentSchoolsAll(Resource):
    @api.response(200, 'SUCCESSFUL: Contents successfully loaded')
    @api.response(204, 'NO CONTENT: No content in database')
    @api.doc(description='Retrieving all records from the database for all suburbs.')
    def get(self):
        db = get_db()
        details_cur = db.execute('select * from [master_dataset]')
        details = details_cur.fetchall()

        return_values = []

        for detail in details:
            detail_dict = {}
            detail_dict['School_name'] = detail['School_name']
            detail_dict['Street'] = detail['Street']
            detail_dict['Town_suburb'] = detail['Town_suburb']
            detail_dict['Postcode'] = detail['Postcode']
            detail_dict['Phone'] = detail['Phone']
            detail_dict['School_email'] = detail['School_email']
            detail_dict['Website'] = detail['Website']
            detail_dict['Fax'] = detail['Fax']
            return_values.append(detail_dict)

        return make_response(jsonify(return_values), 200)


@api.route('/<string:SUBURB>', methods=['GET'])
class GovernmentSchools(Resource):
    @api.response(200, 'SUCCESSFUL: Contents successfully loaded')
    @api.response(204, 'NO CONTENT: No content in database')
    @api.doc(description='Retrieving all records from the database for one suburb.')
    def get(self, SUBURB):
        db = get_db()
        details_cur = db.execute(
            'select * from [master_dataset] where lower(rtrim(Town_suburb)) = lower(rtrim(?))', [SUBURB])
        details = details_cur.fetchall()

        return_values = []

        for detail in details:
            detail_dict = {}
            detail_dict['School_name'] = detail['School_name']
            detail_dict['Street'] = detail['Street']
            detail_dict['Town_suburb'] = detail['Town_suburb']
            detail_dict['Postcode'] = detail['Postcode']
            detail_dict['Phone'] = detail['Phone']
            detail_dict['School_email'] = detail['School_email']
            detail_dict['Website'] = detail['Website']
            detail_dict['Fax'] = detail['Fax']
            return_values.append(detail_dict)

        return make_response(jsonify(return_values), 200)


if __name__ == '__main__':
    app.run()