from clapton import service
from clapton.api.app import app


def main():
    service.prepare_service()
    app.run(debug=True)
