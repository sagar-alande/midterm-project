"""This test the aboutpage"""


def test_big_data(client):
    """This makes the index page"""
    response = client.get("/github")
    assert b' <h1>Git Hub</h1>' in response.data
