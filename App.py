from flask import Flask, render_template, request
from core import portacorrerfl, janelacorrerfl


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portas/<tipo>", methods=["GET", "POST"])
def portas(tipo):
    largura = None
    altura = None
    folhas = None
    lateral = "sem"
    inferior = "trilho"
    rold = "150"
    show = False

    if request.method == "POST":
        try:
            largura = float(request.form.get("largura", 0))
            altura = float(request.form.get("altura", 0))
            folhas = int(request.form.get("folhas", 1))
            lateral = request.form.get("lateral", "sem")
            inferior = request.form.get("inferior", "trilho")
            rold = request.form.get("rold", "150")
            show = True

        except Exception as e:
            print("Erro no POST:", e)
            show = False

    if tipo == "correrfl":
        def noneToNumb(x):
            if x == None:
                x = 1
            else:
                pass
            return x
        porta = portacorrerfl.Porta_CFL(noneToNumb(largura), noneToNumb(altura), noneToNumb(folhas), inferior, rold, lateral)
        larguras = porta.CalcLargPFL()
        alturas = porta.CalcAltPFL()
        quantidades = porta.CalcQtdPFL()
        return render_template(
            "portas/correrflsu.html",
            largura=largura,
            altura=altura,
            folhas=folhas,
            lateral=lateral,
            inferior=inferior,
            rold=rold,
            larguras=larguras,
            alturas=alturas,
            quantidades=quantidades,
            show=show
        )

    elif tipo == "correrfc":
        return render_template(
            "portas/correrfcsu.html",
            largura=largura,
            altura=altura,
            folhas=folhas,
            lateral=lateral,
            inferior=inferior,
            show=show
        )

    return "Porta não encontrada", 404

@app.route("/janelas/<tipo>", methods=["GET", "POST"])
def janelas(tipo):
    largura = None
    altura = None
    folhas = None
    lateral = "sem"
    inferior = "trilho"
    rold = "150"
    show = False

    if request.method == "POST":
        try:
            largura = float(request.form.get("largura", 0))
            altura = float(request.form.get("altura", 0))
            folhas = int(request.form.get("folhas", 1))
            lateral = request.form.get("lateral", "sem")
            inferior = request.form.get("inferior", "trilho")
            rold = request.form.get("rold", "150")
            show = True

        except Exception as e:
            print("Erro no POST:", e)
            show = False

    if tipo == "correrfl":
        def noneToNumb(x):
            if x == None:
                x = 1
            else:
                pass
            return x
        janela = janelacorrerfl.Janela_CFL(noneToNumb(largura), noneToNumb(altura), noneToNumb(folhas), inferior, rold, lateral)
        larguras = janela.CalcLargJFL()
        alturas = janela.CalcAltJFL()
        quantidades = janela.CalcQtdJFL()
        return render_template(
            "portas/correrflsu.html",
            largura=largura,
            altura=altura,
            folhas=folhas,
            lateral=lateral,
            inferior=inferior,
            rold=rold,
            larguras=larguras,
            alturas=alturas,
            quantidades=quantidades,
            show=show
        )

    elif tipo == "correrfc":
        return render_template(
            "portas/correrfcsu.html",
            largura=largura,
            altura=altura,
            folhas=folhas,
            lateral=lateral,
            inferior=inferior,
            show=show
        )

    return "Porta não encontrada", 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")