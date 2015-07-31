from clapton import bootstrap
from clapton.api.app import app


def main():
    bootstrap.bootstrap()
    app.run(debug=True)
