"""This test the aboutpage"""


def test_r_prog(client):
    """This makes the index page"""
    response = client.get("/cicd")
    assert b' <h1>Continuous Integration and Deployment</h1>' in response.data
