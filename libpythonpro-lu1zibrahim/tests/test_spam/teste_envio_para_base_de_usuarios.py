import pytest

from spam.enviador_de_email import Enviador
from spam.main import EnviadorDeSpam
from spam.modelos import Usuario


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
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        'luizibrahim@yahoo.com.br',
        'Curso Python Pro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios)

