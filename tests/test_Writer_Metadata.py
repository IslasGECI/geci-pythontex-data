import pythontex_tools as ptt

dictionary = {"resources": [{"description": "hola", "titulo": "Titulo", "drive": "Drive"}]}


def test_buildes(mocker):
    mocker.patch("pythontex_tools.writer_metadata.load_datapackage", return_value=dictionary)
    writer = ptt.Writer_Metadata()
    assert writer._information is None
    writer.load_metadata("example_dictionary.json")
    description = writer.description()
    assert description == "hola"
    link = writer.write_title_with_link()
    assert link == "\href{Drive}{Titulo}"


def test_load_datapackage():
    dictionary = ptt.load_datapackage("tests/data/example_dictionary.json")
    institution = dictionary["institution"]
    assert institution == "Grupo de Ecología y Conservación de Islas"
