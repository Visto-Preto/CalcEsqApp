class Janela_CFL:

    def __init__(self, largura, altura, folhas, trilho, lateral):
        self.largura = largura
        self.altura = altura
        self.folhas = folhas
        self.trilho = trilho
        self.lateral = lateral

    def CalcLargJFL(self):
        # descontos das larguras
        dmarcoL = 2.6 if self.lateral == "com" else 0
        dmontC = 5.5
        dmontMA = 4.2
        dbagL = 0.2
        dlargVD = 0.4
         
        # cálculos das larguras
        marcoS = self.largura - dmarcoL
        marcoI = self.largura - dmarcoL
        travessa = ((self.largura - (((self.folhas - 1) * dmontMA) + (2 * dmontC)))- dmarcoL) / self.folhas
        bagueteL = travessa - dbagL
        largVD = travessa - dlargVD
        
        return {
            "marcoS": f"{marcoS:.1f}",
            "marcoI": f"{marcoI:.1f}",
            "travessa": f"{travessa:.1f}",
            "bagueteL": f"{bagueteL:.1f}",
            "largVD": f"{largVD:.1f}",
        }
        
    def CalcAltJFL(self):
        # descontos das alturas
        dmarcoI = 2 if self.trilho == "marco" else 0
        dmontA = 2.6 if self.roldana == "120" else 3
        dcomp = 1.5
        dbagA = 20.2
        daltVD = 18
        
        # cálculos das alturas
        marcoL = self.altura
        complemento = self.altura - dcomp
        montante = self.altura - (dmontA + dmarcoI)
        bagueteA = montante - dbagA
        altVD = montante - daltVD
        
        return {
            "marcoL": f"{marcoL:.1f}",
            "complemento": f"{complemento:.1f}",
            "montante": f"{montante:.1f}",
            "bagueteA": f"{bagueteA:.1f}",
            "altVD": f"{altVD:.1f}"
            
            }
            
    def CalcQtdJFL(self):
        #quantidades de cortes
        
        qmarcoS = 1
        qmarcoI = 1 if self.trilho == "marco" else self.folhas
        qlateral = 2
        qcompL = 2
        qmontC = 2
        qmontMA = self.folhas - 1
        qtdsTrav = self.folhas * 2
        qtdsBagL = self.folhas * 2
        qtdsBagA = self.folhas * 2
        qtdsVD = self.folhas
        
        return { 
            "qmarcoS": f"{qmarcoS:.0f}",
            "qmarcoI": f"{qmarcoI:.0f}",
            "qlateral": f"{qlateral:.0f}",
            "qcompL": f"{qcompL:.0f}",
            "qmontC": f"{qmontC:.0f}",
            "qmontMA": f"{qmontMA:.0f}",
            "qtdsTrav": f"{qtdsTrav:.0f}",
            "qtdsBagL": f"{qtdsBagL:.0f}",
            "qtdsBagA": f"{qtdsBagA:.0f}",
            "qtdsVD": f"{qtdsVD:.0f}"
                }
        
# porta = Porta_CFL(451.5, 280.5, 4, "trilho", "150", "sem")
# print(porta.CalcLargPFL())
# print(porta.CalcAltPFL())
# print(porta.CalcQtdPFL())


