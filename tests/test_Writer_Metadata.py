import pythontex_tools as ptt

dictionary = {
    "resources": [
        {"description": "hola", "titulo": "Titulo", "drive": "Drive"},
        {"description": "hola_2", "titulo": "Titulo_2", "drive": "Drive_2"},
    ]
}


def test_buildes_1(mocker):
    mocker.patch("pythontex_tools.writer_metadata.load_datapackage", return_value=dictionary)
    writer = ptt.Writer_Metadata()
    assert writer._information is None
    writer.load_metadata("example_dictionary.json")
    description = writer.description()
    assert description == "hola"
    title = writer.titulo
    assert "Titulo" == title
    link = writer.write_title_with_link()
    assert link == "\href{Drive}{Titulo}"


def test_buildes_2(mocker):
    mocker.patch("pythontex_tools.writer_metadata.load_datapackage", return_value=dictionary)
    level = 1
    writer = ptt.Writer_Metadata(level)
    assert writer._information is None
    writer.load_metadata("example_dictionary.json")
    description = writer.description()
    title = writer.titulo
    assert "Titulo_2" == title
    assert description == "hola_2"
    link = writer.write_title_with_link()
    assert link == "\href{Drive_2}{Titulo_2}"


def test_load_datapackage():
    dictionary = ptt.load_datapackage("tests/data/example_dictionary.json")
    institution = dictionary["institution"]
    assert institution == "Grupo de Ecología y Conservación de Islas"
