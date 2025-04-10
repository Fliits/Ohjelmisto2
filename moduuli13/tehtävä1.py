from flask import Flask, request

app = Flask(__name__)
@app.route('/prime/<p>')

def alkuluku(p):
    p = int(p)
    Prime = False
    for i in range(2, p):
        if p % i == 0:
            print("LUKU EI OLE ALKULUKU")
            break
        else:
            print("LUKU ON ALKULUKU")
            Prime = True
    vastaus = {
        'Number' : p,
        'IsPrime': Prime
    }
    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)