import requests


class HelloSDK:
    @classmethod
    def hello(cls, name=""):
        url = "http://127.0.0.1:5000/api/hello"
        response = requests.get(url=url, params={"name": name})
        return response.text
