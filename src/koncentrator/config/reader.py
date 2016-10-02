import yaml

class Settings:
    content = None

    def __init__(self, file):
        conf = open(file)
        self.content = yaml.load(conf)
        conf.close()

    def get_settings(self):
        return self.content['settings']

    def get_content(self):
        return self.content
