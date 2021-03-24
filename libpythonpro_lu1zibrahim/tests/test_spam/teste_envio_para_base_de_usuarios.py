from unittest.mock import Mock

import pytest

from libpythonpro_lu1zibrahim.spam.main import EnviadorDeSpam
from libpythonpro_lu1zibrahim.spam.modelos import Usuario


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome="Luiz", email='luizibrahim@yahoo.com.br'),
            Usuario(nome="Otavio", email='luizibrahim@yahoo.com.br')
        ],
        [
            Usuario(nome="Luiz", email='luizibrahim@yahoo.com.br'),
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'luizibrahim@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Luiz", email='luizibrahim@yahoo.com.br')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        'otavio@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    enviador.enviar.assert_called_once_with(
        'otavio@yahoo.com.br',
        'luizibrahim@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
