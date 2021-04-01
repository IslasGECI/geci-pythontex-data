import geci_pythontex_data as gpd

dictionary = {"resources": [{"description": "hola", "titulo": "Titulo", "drive": "Drive"}]}


def test_buildes(mocker):
    mocker.patch("geci_pythontex_data.writer_metadata.load_datapackage", return_value=dictionary)
    writer = gpd.Writer_Metadata()
    writer.load_metadata("diccionario.json")
    description = writer.description()
    assert description == "hola"
    link = writer.write_title_with_link()
    assert link == "\href{Drive}{Titulo}"


def test_load_metadata():
    writer = gpd.Writer_Metadata()
    writer.load_metadata("tests/data/diccionario.json")
    institution = writer.information["institution"]
    assert institution == "Grupo de Ecología y Conservación de Islas"
