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

@app.route("/su111", methods=["GET", "POST"])
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
	cortes = [	["largura", largura, 2], 
				["altura",altura, 2], 
				["lambril duplo", f'{(noneToNumb(largura) - dlamb):.1f}', f'{(noneToNumb(altura) - dlamb)/lambA:.1f}'],
				["baguete largura", noneToNumb(largura) - dbagL, 2], 
				["baguete altura", noneToNumb(altura) - dbagA, 2]
				]
	return render_template('Su111.html', show=show, cortes=cortes, vidro=vidro, largura=largura, altura=altura)



@app.route("/portacorrerav", methods=["GET", "POST"])
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
	vidro = [f'{(noneToNumb(largura) + transpasse) - (dtrav + dvidroL):.1f}', f'{noneToNumb(altura) - (daltura +  dvidroA):.1f}']
	cortes = [	["travessa", f'{(noneToNumb(largura) + transpasse) - dtrav:.1f}', 2], 
				["montante",f'{noneToNumb(altura) - daltura:.1f}', 2],
				["baguete largura", f'{(noneToNumb(largura) + transpasse) - (dtrav + dbagL):.1f}', 2],
				["baguete altura", f'{noneToNumb(altura) - (daltura + dbagA):.1f}', 2],
				["lambril duplo", f'{(noneToNumb(largura) + transpasse) - (dtrav + dlamb):.1f}', f'{((noneToNumb(altura) - daltura) - dvidroA)/lambA:.1f}'],
				["trilho superior", f'{2 * noneToNumb(largura) + transpasse:.1f}', 1],
				["trilho inferior", guiaI ,1],
				["complemento lateral", noneToNumb(altura), 1],
				["tubo lateral", f'{noneToNumb(altura) + tubo:.1f}',1]
			]
	return render_template('portacorrerav.html', show=show, cortes=cortes, vidro=vidro, largura=largura, altura=altura)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")