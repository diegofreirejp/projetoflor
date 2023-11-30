class Flores:
    # Self no Python vai ser equivalente ao this. em Java. Por isso ele antecede todos os getters e setters.
    def __init__(self, flor, cor_flor):
        self.flor = flor
        self.cor_flor = cor_flor

    def get_flor(self):
        return self.flor

    def set_flor(self, flor):
        self.flor = flor

    def get_cor_flor(self):
        return self.cor_flor

    def set_cor_flor(self, cor_flor):
        self.cor_flor = cor_flor

    # Esse def STRING é o que vai ser retornado caso a função Flores() seja printada.
    def __str__(self):
        return f"{self.flor} de cor {self.cor_flor}"


class Vasos:
    # Novamente os Getters e Setters dos Vasos das flores, e, pra isso, eu preciso da classe Flor.
    def __init__(self, flores, tamanho, cor_vaso):
        self.flores = flores
        self.tamanho = tamanho
        self.cor_vaso = cor_vaso

    def get_cor_vaso(self):
        return self.cor_vaso

    def set_cor_vaso(self, cor_vaso):
        self.cor_vaso = cor_vaso

    def get_tamanho(self):
        return self.tamanho

    def set_tamanho(self, tamanho):
        self.tamanho = tamanho

    # Aqui ele irá, além de printar a cor do vaso e o tamanho dele, ele irá retornar, em string, o resultado de Flores(),
    # como foi decidido acima.
    def __str__(self):
        return f"({self.flores} em um vaso {self.cor_vaso} de tamanho {self.tamanho})"


# Aqui é apenas um teste com main para garantir que todas as classes estão funcionando corretamente.
#if __name__ == "__main__":

    #tulipa = Flores("Tulipa", "Amarela")

    # Em vez de botar uma String, é necessário botar a variável que carrega o conteúdo de Flores().
    #vaso_tulipa = Vasos(tulipa, "Pequeno", "Laranja")

    #print(vaso_tulipa)
