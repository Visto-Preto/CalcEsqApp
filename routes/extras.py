from flask import Blueprint, render_template, request
from utils import noneToNumb

extras_bp = Blueprint("extras", __name__)

@extras_bp.route("/su111", methods=["GET", "POST"])
def su111():

    lambA = 10.1
    dlamb = 10.3
    dbagL = 10.2
    dbagA = 12.5
    drecuo = 10.4

    show = False
    largura = None
    altura = None

    if request.method == "POST":
        try:
            largura = float(request.form.get("largura", 0))
            altura = float(request.form.get("altura", 0))
            show = True
        except Exception as e:
            print("Erro no POST:", e)
            show = False

    vidro = [noneToNumb(largura) - drecuo, noneToNumb(altura) - drecuo]

    cortes = [
        ["largura", largura, 2],
        ["altura", altura, 2],
        ["lambril duplo", f'{(noneToNumb(largura) - dlamb):.1f}', f'{(noneToNumb(altura) - dlamb)/lambA:.1f}'],
        ["baguete largura", noneToNumb(largura) - dbagL, 2],
        ["baguete altura", noneToNumb(altura) - dbagA, 2]
    ]

    return render_template(
        "Su111.html",
        show=show,
        cortes=cortes,
        vidro=vidro,
        largura=largura,
        altura=altura
    )


@extras_bp.route("/portacorrerav", methods=["GET", "POST"])
def portacorrerav():

    transpasse = 5.0
    daltura = 1.5
    lambA = 10.1
    dlamb = 0.3
    dvidroA = 18
    dvidroL = 0.4
    dbagL = 0.2
    dbagA = 20.2
    dtrav = 10.3
    guiaI = 30.0
    tubo = 5.0

    show = False
    largura = None
    altura = None

    if request.method == "POST":
        try:
            largura = float(request.form.get("largura", 0))
            altura = float(request.form.get("altura", 0))
            show = True
        except Exception as e:
            print("Erro no POST:", e)
            show = False

    vidro = [
        f'{(noneToNumb(largura) + transpasse) - (dtrav + dvidroL):.1f}',
        f'{noneToNumb(altura) - (daltura + dvidroA):.1f}'
    ]

    cortes = [
        ["travessa", f'{(noneToNumb(largura) + transpasse) - dtrav:.1f}', 2],
        ["montante", f'{noneToNumb(altura) - daltura:.1f}', 2],
        ["baguete largura", f'{(noneToNumb(largura) + transpasse) - (dtrav + dbagL):.1f}', 2],
        ["baguete altura", f'{noneToNumb(altura) - (daltura + dbagA):.1f}', 2],
        ["lambril duplo", f'{(noneToNumb(largura) + transpasse) - (dtrav + dlamb):.1f}', f'{((noneToNumb(altura) - daltura) - dvidroA)/lambA:.1f}'],
        ["trilho superior", f'{2 * noneToNumb(largura) + transpasse:.1f}', 1],
        ["trilho inferior", guiaI, 1],
        ["complemento lateral", noneToNumb(altura), 1],
        ["tubo lateral", f'{noneToNumb(altura) + tubo:.1f}', 1]
    ]

    return render_template(
        "portacorrerav.html",
        show=show,
        cortes=cortes,
        vidro=vidro,
        largura=largura,
        altura=altura
    )