from flask import Blueprint, render_template, request
from core import descPortaFL
from utils import noneToNumb

portas_bp = Blueprint("portas", __name__)

@portas_bp.route("/portas/<tipo>", methods=["GET","POST"])
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
            largura = float(request.form.get("largura",0))
            altura = float(request.form.get("altura",0))
            folhas = int(request.form.get("folhas",1))
            lateral = request.form.get("lateral","False") == "True"
            inferior = request.form.get("inferior","False") == "True"
            rold = request.form.get("rold","rol150")
            show = True
        except:
            show = False

    if tipo == "correrfl":

        cortes = descPortaFL.cortes(
            noneToNumb(largura),
            noneToNumb(altura),
            noneToNumb(folhas),
            lateral,
            inferior,
            rold
        )

        perdaLargura = descPortaFL.dtravessa(noneToNumb(folhas),lateral)
        perdaAltura = f"{noneToNumb(altura) - float(cortes['montante'][0]):.1f}"

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

    return "Porta não encontrada",404