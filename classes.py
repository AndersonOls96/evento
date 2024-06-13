class Pessoa:
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone
    
    def __str__(self):
        return f"Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}"

class Evento:
    def __init__(self, titulo, data, horario, local):
        self.titulo = titulo
        self.data = data
        self.horario = horario
        self.local = local
        self.participantes = []
    
    def adicionar_participante(self, participante):
        if not participante in self.participantes:
            self.participantes.append(participante)
        else:
            print("Participante já existe")
    
    def remover_participante(self, participante):
        self.participantes.remove(participante)
    
    def listar_participantes(self):
        for participante in self.participantes:
            print(participante)
    
    def __str__(self):
        return f"Título: {self.titulo}, Data: {self.data}, Horário: {self.horario}, Local: {self.local}"