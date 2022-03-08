"""This test the aboutpage"""


def test_aboutpage(client):
    """This makes the index page"""
    response = client.get("/docker")
    assert b' <h1>Docker</h1>' in response.data
