# Pythontex Tools
[![Tests](https://github.com/IslasGECI/pythontex_tools/actions/workflows/actions.yml/badge.svg)](https://github.com/IslasGECI/pythontex_tools/actions/workflows/actions.yml)

Pythontex Tools is a module to facilitate the interaction between python and latex.
With Pythontex Tools we can write titles, links and descriptions from our data directly to Latex.

## Ejemplo de uso
Para usar este módulo debemos importarlo al archivo de latex en el que estemos trabajando nuestro reporte.

```
\begin{pycode}

import pythontex_tools as ptt
data_information = '../data/raw/nidos_busqueda_aves_marinas/datapackage.json'

search_nests_datapackage = '../data/raw/nidos_busqueda_aves_marinas/datapackage.json'

metadata_writer = ptt.Writer_Metadata()
metadata_writer.load_metadata(search_nests_datapackage)

\end{pycode}
```
