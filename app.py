from flask import Flask
from flask import request
from flasgger import Swagger
from flasgger import swag_from

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/api/hello')
@swag_from('hello.yml')
def hello_world():
    """ 打招呼的服务，10块钱打一次招呼 """
    name = request.args.get("name", "")
    print(f"name: {name}")
    if name:
        return "Hello " + name
    else:
        return "Hello World"


if __name__ == '__main__':
    app.run()
