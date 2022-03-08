"""This test the aboutpage"""


def test_r_prog(client):
    """This makes the index page"""
    response = client.get("/r_prog")
    assert b' <h1>R-Programming</h1>' in response.data
