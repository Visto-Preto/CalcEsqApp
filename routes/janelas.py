from flask import Blueprint, render_template, request
from core import descJanelaFL
from utils import noneToNumb

janelas_bp = Blueprint("janelas", __name__)

@janelas_bp.route("/janelas/<tipo>", methods=["GET", "POST"])
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

        cortes = descJanelaFL.cortes(
            noneToNumb(largura),
            noneToNumb(altura),
            noneToNumb(folhas),
            lateral,
            inferior,
            rold
        )

        perdaLargura = descJanelaFL.dtravessa(noneToNumb(folhas), lateral)

        perdaAltura = f"{noneToNumb(altura) - float(cortes['montante'][0]):.1f}"

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

    return "Janela não encontrada", 404