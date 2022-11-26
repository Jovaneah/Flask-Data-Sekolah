from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from flask_restful import Resource, Api

app = Flask(__name__)
mysql = MySQL()
api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'backend'

mysql.init_app(app)
class Sekolah(Resource):
    def get(self):
        try:
            sql =  mysql.connection.cursor()
            sql.execute("""SELECT * FROM data_sekolah""")
            data_sekolah = sql.fetchall()
            result = jsonify(data_sekolah=data_sekolah)
            result.status_code = 200
            return(result)
        except Exception as err:
            print(err)
            result = jsonify("failed to fetch database...")
            result.status_code = 400
            return(result)
        finally:
            sql.close()
    def post(self):
        try:
            sql = mysql.connection.cursor()
            _nama = request.form['nama']
            _kelas = request.form['kelas']
            _pekerjaan = request.form['pekerjaan']
            create_data = """INSERT INTO data_sekolah (nama, kelas, pekerjaan) VALUES (%s,%s,%s)"""
            sql.execute(create_data, (_nama, _kelas, _pekerjaan))
            mysql.connection.commit()
            result = jsonify(data="Data berhasil ditambahkan!")
            result.status_code = 200
            return(result)
        except Exception as err:
            print(err)
            result = jsonify(data="Data gagal ditambahkan!")
            result.status_code = 400
            return(result)
        finally:
            sql.close()
    def delete(self):
        try:
            sql = mysql.connection.cursor()
            _id = request.form['id']
            delete_data = """DELETE FROM data_sekolah WHERE id =  %s """
            sql.execute(delete_data, (_id))
            mysql.connection.commit()
            result = jsonify(data="Data berhasil dihapus!")
            result.status_code = 200
            return(result)
        except Exception as err:
            print(err)
            result = jsonify(data="Data gagal dihapus!")
            result.status_code = 400
            return(result)
        finally:
            sql.close()


api.add_resource(Sekolah, "/data_sekolah", endpoint="data_sekolah")
app.run(host="localhost", port="3200")




