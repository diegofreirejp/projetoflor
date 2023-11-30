class Cliente:

    #Assim como em Pedidos, os parâmetros de entrada ao chamar a função Cliente() serão esses:
    def __init__(self, nome, cpf, telefone):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone

    #Como não precisa de um cadastro muito elaborado e apenas o necessário, aqui estão os getters e setters
    # do Nome, CPF e telefone.
    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_cpf(self):
        return self.cpf

    def set_cpf(self, cpf):
        self.cpf = cpf

    def get_telefone(self):
        return self.telefone

    def set_telefone(self, telefone):
        self.telefone = telefone

    #Essa é a string de retorno ao printar a variável com as informações do cliente.
    def __str__(self):
        return f"Cliente: {self.nome} \n  CPF: {self.cpf} \n Telefone: {self.telefone}"