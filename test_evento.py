from classes import *
import pytest


@pytest.fixture
def pessoa1():
    return Pessoa("Lucas", "lucas@me.com", "123456789")
@pytest.fixture
def pessoa2():
    return Pessoa("Maria", "maria@me.com", "123456789")
@pytest.fixture
def evento():
    return Evento("Python Workshop", "2022-12-25", "10:00", "Python Workshop Room")


def test_adicionar_participante(pessoa1, evento):
    evento.adicionar_participante(pessoa1)
    assert len(evento.participantes) == 1
    

def test_adicionar_participante_existente(pessoa1, evento):
    evento.adicionar_participante(pessoa1)
    evento.adicionar_participante(pessoa1)
    assert len(evento.participantes) == 1
    

def test_remover_participante(evento, pessoa1, pessoa2):
    evento.adicionar_participante(pessoa1)
    evento.adicionar_participante(pessoa2)
    evento.remover_participante(pessoa1)
    assert len(evento.participantes) == 1

def test_str_pessoa(pessoa1):
    assert str(pessoa1) == "Nome: Lucas, Email: lucas@me.com, Telefone: 123456789"

def test_str_evento(evento):
    assert str(evento) == "Título: Python Workshop, Data: 2022-12-25, Horário: 10:00, Local: Python Workshop Room"