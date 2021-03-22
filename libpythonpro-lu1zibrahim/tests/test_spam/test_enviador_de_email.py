import pytest

from spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador= Enviador()
    assert enviador is not None

@pytest.mark.parametrize(
    'remetente',
    ['luizibrahim@yahoo.com.br','luizibrahim@outlook.com']
)
def test_remetente(remetente):
    enviador=Enviador()
    resultado=enviador.enviar(
        remetente,
        'luizibrahim94@gmail.com',
        'Cursos Python Pro!',
        'Dados sobre o inicio das turmas',
    )
    assert remetente in resultado


@pytest.mark.parametrize(
    'remetente',
    ['','luiz']
)


def test_remetente_invalido(remetente):
    enviador=Enviador()
    with pytest.raises(EmailInvalido):
        resultado=enviador.enviar(
            remetente,
            'luizibrahim94@gmail.com',
            'Cursos Python Pro!',
            'Dados sobre o inicio das turmas',
        )