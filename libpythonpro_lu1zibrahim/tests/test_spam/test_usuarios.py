from spam.modelos import Usuario

def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Luiz", email='luizibrahim@yahoo.com.br')
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)



def test_listar_usuario(sessao):
    usuarios = [Usuario(nome="Luiz", email='luizibrahim@yahoo.com.br'),
                Usuario(nome="Otavio", email='luizibrahim@yahoo.com.br')
                ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()