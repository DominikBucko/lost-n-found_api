import yaml
from misc import ObjectView


config = ObjectView({})


def load_config(filename):
    with open(filename) as conf:
        global config
        config = ObjectView(yaml.safe_load(conf))
