from api import app
from os import getenv

from flask_jwt_extended import JWTManager

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port="8080")
    # Can't run below port 1024 as an unprivileged user

    app.run(host="0.0.0.0", port="8080")
