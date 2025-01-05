import requests


def test_create_film():
    url = "http://127.0.0.1:3000/api/films"
    data = {
        "title": "The Matrix Resurrections",
        "year": 2021,
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post(url, json=data, headers=headers)
    print(response.text)

def test_delete_film(uuid: str):
    url = f"http://127.0.0.1:3000/api/films/{uuid}"
    response = requests.delete(url)
    print(response.text)


if __name__ == '__main__':
    test_create_film()
    test_delete_film("67c95824-99e6-4b13-8d13-78dbc484fdff")  # just for manual tests
