from unittest.mock import Mock

import pytest

import github_api




@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/61382982?v=4'
    resp_mock.json.return_value = {
        'login': 'lu1zibrahim',
        'avatar_url': url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original

def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('lu1zibrahim')
    assert avatar_url == url


def test_buscar_avatar_integração():
    url = github_api.buscar_avatar('lu1zibrahim')
    assert 'https://avatars.githubusercontent.com/u/61382982?v=4' == url