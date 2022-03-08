"""This test the aboutpage"""


def test_big_data(client):
    """This makes the index page"""
    response = client.get("/bdata")
    assert b' <h1>Big Data</h1>' in response.data
