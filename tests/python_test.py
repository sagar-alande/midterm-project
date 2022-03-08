"""This test the aboutpage"""


def test_python(client):
    """This makes the index page"""
    response = client.get("/python")
    assert b' <h1>Python/Flask</h1>' in response.data
