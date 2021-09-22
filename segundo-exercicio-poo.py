class  tv:
    def __init__(self, tamanho) -> None:
        self.cor = "preta"
        self.ligada = False
        self.tamanho = tamanho
        self.canal = "Netflix"
        self.volume = 10


    def mudar_canal(self, novo_canal):    
        self.canal = novo_canal


    
        
tv_sala = tv(tamanho=33)
tv_quarto = tv(tamanho=45)

print(tv_quarto.cor)
print(tv_sala.volume)

tv_sala.mudar_canal("Globo")
tv_quarto.mudar_canal("YouTube")
print(tv_sala.tamanho)
print(tv_quarto.tamanho)