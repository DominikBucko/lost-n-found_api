import yaml
import config
from app import app, initialize_api


if __name__ == '__main__':
    config.load_config("config.yaml")

    initialize_api()
    app.run(host="::", port=config.config.port)
