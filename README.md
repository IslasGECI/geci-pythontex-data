# Pythontex Tools
[![Tests](https://github.com/IslasGECI/pythontex_tools/actions/workflows/actions.yml/badge.svg)](https://github.com/IslasGECI/pythontex_tools/actions/workflows/actions.yml)

Pythontex Tools is a module to facilitate the interaction between python and latex.
With Pythontex Tools we can write titles, links and descriptions from our data directly to Latex.

## Example of use
To use this module it is necessary to import it on our LaTeX report that we are working on.

### Example of a datapackage.json
In Pythontex Tools we have the `Writer_Metadata()` tool with which we can obtain the metadata of a `datapackage.json` and write it in our LaTex report.
The `datapackage.json` can have 1 or more resources as in the following example.

```json
{
    "name": "tablas_de_datos",
    "schema": "tabular-data-package",
    "profile": "tabular-data-package",
    "institution": "Grupo de Ecología y Conservación de Islas",
    "resources": [
        {
            "name": "Tabla_1",
            "titulo": "Tabla 1",
            "description": "Descripción de la tabla 1",
            "drive": "Link de la ubicación de la tabla 1 en google drive"
            
        },
        {
            "name": "Tabla_2",
            "titulo": "Tabla 2",
            "description": "Descripción de la tabla 2",
            "drive": "Link de la ubicación de la tabla 2 en google drive"
        }
    ]
}
```

### Example of how to import
If we want to access the metadata of table 1 of the previous example, then we do it as follows:

```latex
\begin{pycode}

import pythontex_tools as ptt

search_nests_datapackage = '../data/raw/nidos_busqueda_aves_marinas/datapackage.json'

metadata_table_1 = ptt.Writer_Metadata()
metadata_table_1.load_metadata(search_nests_datapackage)

\end{pycode}
```

If we want the metadata of table 2 we change the index of the `Writer_Metadata()` as follows:

```latex
\begin{pycode}

import pythontex_tools as ptt

search_nests_datapackage = '../data/raw/nidos_busqueda_aves_marinas/datapackage.json'

metadata_table_1 = ptt.Writer_Metadata()
metadata_table_2 = ptt.Writer_Metadata(1)

metadata_table_1.load_metadata(search_nests_datapackage)
metadata_table_2.load_metadata(search_nests_datapackage)

\end{pycode}
```

Note: The resource index starts at 0.

### Example of how to get the metadata of a resource

To write the title of the database with the link to Google Drive:
```latex
\py{metadata_table_1.write_title_with_link()}. \\
```
To write the description of the database:
```latex
\py{metadata_table_1.description()}. \\
```
