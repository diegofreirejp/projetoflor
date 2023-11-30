from typing import List
from Flores import Flores, Vasos
from Cliente import Cliente

class Pedidos:
    # Aqui é dado início a um vetor vazio de flores e vasos e o cliente que no momento do pedido ganhará um nome.
    # No momento que Pedido() for chamado, ele obrigatoriamente terá como parâmetro de entrada o nome do Cliente.
    def __init__(self, cliente):
        self.cliente = cliente
        self.flor = []
        self.vaso = []

    # Essa vai ser a função pra adicionar tanto flor, quanto vaso aos vetores previamente vazios.
    def add_flor(self, f):
        self.flor.append(f)

    def add_vaso(self, v):
        self.vaso.append(v)

    # Aqui estão os getters e setters. A diferença entre esses e os da outra classe são que esses são getters e setters da classe por completo,
    # cada uma com seus próprios getters e setters. Já o cliente apenas entra aqui para uma melhor busca.
    def get_flores(self):
        return self.flor

    def get_vasos(self):
        return self.vaso

    def get_cliente(self):
        return self.cliente

    def set_flores(self, flor):
        self.flor = flor

    def set_vasos(self, vaso):
        self.vaso = vaso

    def set_cliente(self, cliente):
        self.cliente = cliente


def main():

    # Como decidido no início da classe Pedido, o parâmetro de entrada dessa função será um cliente, e um cliente possui seu
    # nome, cpf e telefone. Por isso, foi chamado a função Cliente para determinar tais variáveis e, por fim, como parâmetro de
    # entrada na classe pedido foi colocado a variável que carrega as informações do cliente.
    nome_cliente = input("Digite o nome do Cliente: ")
    CPF_cliente = input("Digite o CPF do Cliente: ")
    telefone_cliente = input("Digite o telefone do Cliente: ")

    pedido_cliente = Cliente(nome_cliente, CPF_cliente, telefone_cliente)

    pedido = Pedidos(pedido_cliente)

    # Aqui iniciamos algumas flores() e atribuimos uma variável para carregar o seu conteúdo, neste caso, as flores e suas respectivas cores.
    orquidea_roxa = Flores("Orquidea", "Roxa")
    orquidea_amarela = Flores("Orquidea", "Amarela")
    rosa_vermelha = Flores("Rosa", "Vermelha")
    rosa_amarela = Flores("Rosa", "Amarela")
    tulipa_rosa = Flores("Tulipa", "Rosa")
    tulipa_branca = Flores("Tulipa", "Branca")
    girassol_amarelo = Flores("Girassol", "Amarelo")

    # Aqui adicionamos as flores que o cliente desejar ao pedido dele.
    pedido.add_flor(rosa_vermelha)
    pedido.add_flor(orquidea_amarela)
    pedido.add_flor(girassol_amarelo)
    pedido.add_flor(tulipa_branca)

    # Aqui iniciamos alguns vasos() e atribuímos uma variável para também carregar o conteúdo, mas neste caso, as flores supracitadas,
    # tamanho do vaso e a cor do vaso.
    vaso1 = Vasos(rosa_vermelha, "P", "Branco")
    vaso2 = Vasos(orquidea_amarela, "M", "Laranja")
    vaso3 = Vasos(girassol_amarelo, "P", "Transparente")
    vaso4 = Vasos(tulipa_branca, "G", "Branco")

    # Adicionamos ao pedido os vasos com as flores.
    pedido.add_vaso(vaso1)
    pedido.add_vaso(vaso2)
    pedido.add_vaso(vaso3)
    pedido.add_vaso(vaso4)

    # Aqui printará o nome do Cliente decidido no início
    print(f"Informações do Cliente \n {pedido.get_cliente()}")
    print("Flores do Cliente:")
    # Para cada flor no array flores de Pedidos(), irá printar a flor.
    for flor in pedido.get_flores():
        print(f"  -> {flor}")
    print("Vasos:")
    # Para cada vaso no array vasos de Pedidos(), irá printar os vasos com as flores.
    for vaso in pedido.get_vasos():
        print(f"  -> {vaso}")


if __name__ == "__main__":
    main()