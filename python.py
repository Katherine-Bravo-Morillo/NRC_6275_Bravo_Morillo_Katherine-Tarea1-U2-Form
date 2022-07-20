#importamos la libreria Flask
from flask import Flask, render_template

app = Flask(__name__)
#---------------------------------------
#Ruta de pagina index layauts
#---------------------------------------
@app.route('/')
def index():
    return render_template('/layouts/index.html')

#iniciamos la aplicacion
if __name__ == '__main__':
    app.run(debug=True)
