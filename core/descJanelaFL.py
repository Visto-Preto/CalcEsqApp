#descontos
dmarcoL = 2.6
dmontC = 4.2
dmontMA = 2.2
dmarcoI = 2
dmont120 = 2.6
dmont150 = 3
dmont49 = 3
dcomp = 1.5
dbagA = 10.3
dbagL = 0.2
dlargVD = 0.4
daltVD = 8.2

def dtravessa(folhas, lateral):
    tMA = (folhas - 1) * dmontMA
    tMC = 2 * dmontC
    trav = tMA + tMC + dmarcoL if lateral == True else tMA + tMC
    return float(f"{trav:.1f}")
# fim dos descontos


def cortes(largura, altura, folhas, lateral, inferior, roldana):
    #Cortes
    marcoS = largura - dmarcoL if lateral == True else largura
    marcoI = largura - dmarcoL if lateral == True else largura
    marcoL = altura
    compL = altura - (2 * dcomp) if inferior == True else altura - dcomp

    if roldana == "rol49" and inferior == True:
        montante = altura - (dmont49 + dmarcoI)
    elif roldana == "rol120" and inferior == True:
        montante = altura - (dmont120 + dmarcoI)
    elif roldana == "rol120" and inferior == False:
        montante = altura - dmont120
    elif roldana == "rol150" and inferior == True:
        montante = altura - (dmont150 + dmarcoI)
    elif roldana == "rol150" and inferior == False:
        montante = altura - dmont150
    else:
        montante = 0

    travessa = (largura - dtravessa(folhas, lateral)) / folhas
    bagueteL = travessa - dbagL
    bagueteA = montante - dbagA
    vidroL = travessa - dlargVD
    vidroA = montante - daltVD

    #quantindades

    qmarcoS = 1
    qmarcoI = 1 if inferior == True else folhas
    qmarcoL = 2
    qcompL = 2
    qmontante = 2
    qmontanteMA_ce = folhas - 1
    qmontanteMA_se = folhas - 1
    qtravessa = 2 * folhas
    qbagueteL =  2 * folhas
    qbagueteA = 2 * folhas
    qvidro = folhas

    return{
        "marcoS": [f"{marcoS:.1f}", qmarcoS],
        "marcoI": [f"{marcoI:.1f}", qmarcoI],
        "marcoL": [f"{marcoL:.1f}", qmarcoL],
        "compL": [f"{compL:.1f}", qcompL],
        "montante": [f"{montante:.1f}", qmontante],
        "montanteMA_ce": [f"{montante:.1f}", qmontanteMA_ce],
        "montanteMA_se": [f"{montante:.1f}", qmontanteMA_se],
        "travessa": [f"{travessa:.1f}", qtravessa],
        "bagueteL": [f"{bagueteL:.1f}", qbagueteL],
        "bagueteA": [f"{bagueteA:.1f}", qbagueteA],
        "vidro": [f"{vidroL:.1f}",  f"{vidroA:.1f}", qvidro]

    }