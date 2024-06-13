from classes import *

def test_adicionar_participante():
    evento = Evento("Python Workshop", "2022-12-25", "10:00", "Python Workshop Room")
    participane = Pessoa("Lucas", "lucas@me.com", "123456789")

    evento.adicionar_participante(participane)
    assert len(evento.participantes) == 1

def test_adicionar_participante_existente():
    evento = Evento("Python Workshop", "2022-12-25", "10:00", "Python Workshop Room")
    participane = Pessoa("Lucas", "lucas@me.com", "123456789")

    evento.adicionar_participante(participane)
    evento.adicionar_participante(participane)
    assert len(evento.participantes) == 1

def test_remover_participante():
    evento = Evento("Python Workshop", "2022-12-25", "10:00", "Python Workshop Room")
    participane = Pessoa("Lucas", "lucas@me.com", "123456789")

    evento.adicionar_participante(participane)
    evento.remover_participante(participane)
    assert len(evento.participantes) == 0

def test_str_pessoa():
    pessoa = Pessoa("Lucas", "lucas@me.com", "123456789")
    assert str(pessoa) == "Nome: Lucas, Email: lucas@me.com, Telefone: 123456789"

def test_str_evento():
    evento = Evento("Python Workshop", "2022-12-25", "10:00", "Python Workshop Room")
    assert str(evento) == "Título: Python Workshop, Data: 2022-12-25, Horário: 10:00, Local: Python Workshop Room"