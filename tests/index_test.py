"""This test the aboutpage"""


def test_indexpage(client):
    """This makes the index page"""
    response = client.get("/")
    assert b'Professional Summary' in response.data
