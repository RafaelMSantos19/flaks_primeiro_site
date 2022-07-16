from flask import Flask , render_template

app = Flask(__name__)


#cria primeiro site

#router
@app.route("/")
#função
def hello_word():
     return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contatos.html")

@app.route("/Rafael")
def rafael():
    return render_template("rafael.html")   

@app.route("/usuarios/<name>")
def usuario(name):
    return render_template("usuarios.html",name=name)



#colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)

