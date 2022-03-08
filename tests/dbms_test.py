"""This test the aboutpage"""


def test_aboutpage(client):
    """This makes the index page"""
    response = client.get("/dbms")
    assert b' <h1>DBMS(DATABASE MANAGEMENT SYSTEM)</h1>' in response.data
