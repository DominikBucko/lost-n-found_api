import yaml
import os
from misc import ObjectView

key = 'super-secret'

config = ObjectView(yaml.safe_load(open(os.environ["APP_CONFIG"])))

if os.environ["ENV"] == "dev":
    config.upload_folder = os.path.join(os.getcwd(), config.upload_folder)

def load_config(filename):
    with open(filename) as conf:
        global config
        config = ObjectView(yaml.safe_load(conf))
