from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World - Welcome to Gaby's Class! Student: Sandro Barros"

if __name__ == '__main__':
    app.run()
