import json


class Writer_Metadata:
    def load_metadata(self, path):
        with open(path, encoding="utf8") as info_file:
            self.information = json.load(info_file)

    def titulo(self):
        return self.information["resources"][0]["titulo"]

    def link_to_drive(self):
        return self.information["resources"][0]["drive"]

    def write_title_with_link(self):
        title_with_link = "\href{%s}{%s}" % (self.link_to_drive(), self.titulo())
        return title_with_link

    def description(self):
        return self.information["resources"][0]["description"]
