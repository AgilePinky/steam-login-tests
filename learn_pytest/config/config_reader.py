import json

class ConfigReader:

    CONFIG_PATH = "config/config.json"

    def __init__(self, config_file=CONFIG_PATH):
        with open(config_file) as f:
            self.config = json.load(f)

    def get_base_url(self):
        return self.config["base_url"]

    def get_timeout(self):
        return self.config["timeout"]

    def get_poll_frequency(self):
        return self.config["poll_frequency"]