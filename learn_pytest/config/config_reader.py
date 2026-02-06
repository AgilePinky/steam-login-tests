import json

class ConfigReader:
    def __init__(self, config_file="learn_pytest/config/config.json"):
        with open(config_file) as f:
            self.config = json.load(f)

    def get_base_url(self):
        return self.config("base_url")

    def get_timeout(self):
        return self.config("timeout")