import yaml
import easydict as edict

def load_config(config_path):
    with open(config_path) as f:
        config = edict.EasyDict(yaml.load(f))
    return config

