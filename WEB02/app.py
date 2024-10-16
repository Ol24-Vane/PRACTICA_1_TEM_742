from flask import Flask, render_template, redirect, request, url_for  # importa la libreria Flask

app = Flask(__name__)     #instanciar el objeto app, __name__ direccion de la libreria de manera exacta
 
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quienes_somos")           #implementacion de las rutas 
def quienes_somos():
    return render_template("quienes_somos.html")

@app.route("/servicios")
def servicios():
    return render_template("servicios.html")

@app.route("/noticias")
def noticias():
    return render_template("noticias.html")

@app.route("/contactos", methods=['GET', 'POST'])
def contactos():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        mensaje = request.form['mensaje']
       
        return redirect(url_for("index"))
    return render_template("contactos.html")

if __name__ == "__main__":
    app.run(debug=True)           # iniciar el servidor 