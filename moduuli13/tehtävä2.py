from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/airport/<icao>')
def airport(icao):
    yhteys = mysql.connector.connect(
        database='flight_game',
        user='pythonuser',
        password='salasana',
        autocommit=True
    )
    sql = f"SELECT ident, name, municipality from airport where ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    if tulos:
        vastaus = {
            'ICAO': tulos[0],
            'Name': tulos[1],
            'Municipality': tulos[2]
        }
        return vastaus
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)