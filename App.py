from flask import Flask, render_template, request
from core import descJanelaFL, descPortaFL

def noneToNumb(x):
    if x == None:
        x = 1
    else:
        pass
    return x


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/portas/<tipo>", methods=["GET", "POST"])
def portas(tipo):
    largura = None
    altura = None
    folhas = None
    lateral = False
    inferior = False
    rold = "rol150"
    show = False

    if request.method == "POST":
        try:
            largura = float(request.form.get("largura", 0))
            altura = float(request.form.get("altura", 0))
            folhas = int(request.form.get("folhas", 1))
            lateral = request.form.get("lateral", "False") == "True"
            inferior = request.form.get("inferior", "False") == "True"
            rold = request.form.get("rold", "rol150")
            show = True

        except Exception as e:
            print("Erro no POST:", e)
            show = False

    if tipo == "correrfl":
        cortes = descPortaFL.cortes(noneToNumb(largura), noneToNumb(altura), noneToNumb(folhas), lateral, inferior, rold)
        perdaLargura = descPortaFL.dtravessa(noneToNumb(folhas),lateral)
        perdaAltura = f"{noneToNumb(altura) - float(cortes["montante"][0]):.1f}"

        return render_template(
            "portas/correrflsu.html",
            largura=largura,
            altura=altura,
            folhas=folhas,
            lateral=lateral,
            inferior=inferior,
            rold=rold,
            cortes=cortes,
            perdaLargura=perdaLargura,
            perdaAltura=perdaAltura,
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
    lateral = True
    inferior = True
    rold = "rol49"
    show = False

    if request.method == "POST":
        try:
            largura = float(request.form.get("largura", 0))
            altura = float(request.form.get("altura", 0))
            folhas = int(request.form.get("folhas", 1))
            lateral = request.form.get("lateral", "True") == "True"
            inferior = request.form.get("inferior", "True") == "True"
            rold = request.form.get("rold", "rol49")
            show = True

        except Exception as e:
            print("Erro no POST:", e)
            show = False

    if tipo == "correrfl":
        cortes = descJanelaFL.cortes(noneToNumb(largura), noneToNumb(altura), noneToNumb(folhas), lateral, inferior, rold)
        perdaLargura = descJanelaFL.dtravessa(noneToNumb(folhas),lateral)
        perdaAltura = f"{noneToNumb(altura) - float(cortes["montante"][0]):.1f}"

        return render_template(
            "janelas/correrflsu.html",
            largura=largura,
            altura=altura,
            folhas=folhas,
            lateral=lateral,
            inferior=inferior,
            rold=rold,
            cortes=cortes,
            perdaLargura=perdaLargura,
            perdaAltura=perdaAltura,
            show=show
        )










    elif tipo == "correrfc":
        return render_template(
            "janelas/correrfcsu.html",
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