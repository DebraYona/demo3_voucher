from flask import Flask, jsonify, request
from flaskext.mysql import MySQL


app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'digimon'
app.config['MYSQL_DATABASE_DB'] = 'voucher'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)
@app.route('/add', methods=['GET'])
def get():
    numero_voucher=request.args.get('numero_voucher')
    nombre_alumno=request.args.get('nombre_alumno')
    codigo_alumno=request.args.get('codigo_alumno')
    
    print(numero_voucher)
    conn =mysql.connect()
    cur = conn.cursor()

    cur.callproc('transaccion_deposito', (remitente,receptor,monto,nombreT,tipo))
    cur.fetchall()

    conn.commit()

    return jsonify({'resultado' :'exito' })

if __name__ == '__main__':
    app.run()