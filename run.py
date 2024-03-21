# pylint: disable=import-error
from dotenv import load_dotenv
from src.main.server.server import app

if __name__ == "__main__":
    load_dotenv()
    app.run(
        debug=False
        )
