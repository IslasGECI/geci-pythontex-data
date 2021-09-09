import json


class Writer_Metadata:
    def __init__(self, level=0):
        self._information = None
        self.level = level

    def load_metadata(self, path):
        self._information = load_datapackage(path)

    @property
    def titulo(self):
        return self._information["resources"][self.level]["titulo"]

    @property
    def link_to_drive(self):
        return self._information["resources"][self.level]["drive"]

    def write_title_with_link(self):
        title_with_link = f"\href{ {self.link_to_drive} }{ {self.titulo} }".replace("'", "")
        return title_with_link

    def description(self):
        return self._information["resources"][self.level]["description"]


def load_datapackage(path):
    with open(path, encoding="utf8") as info_file:
        information = json.load(info_file)
    return information
