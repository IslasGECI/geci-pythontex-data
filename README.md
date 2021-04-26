# Pythontex Tools
[![Tests](https://github.com/IslasGECI/pythontex_tools/actions/workflows/actions.yml/badge.svg)](https://github.com/IslasGECI/pythontex_tools/actions/workflows/actions.yml)

Pythontex Tools is a module to facilitate the interaction between python and latex.
With Pythontex Tools we can write titles, links and descriptions from our data directly to Latex.

## Example of use
To use this module it is necessary to import it on our LaTeX report that we are working on.

### To import
```
\begin{pycode}

import pythontex_tools as ptt

search_nests_datapackage = '../data/raw/nidos_busqueda_aves_marinas/datapackage.json'

metadata_writer = ptt.Writer_Metadata()
metadata_writer.load_metadata(search_nests_datapackage)

\end{pycode}
```
### To use
To write the title of the database with the link to Google Drive:
```
\py{metadata_writer.write_title_with_link()}. \\
```
To write the description of the database:
```
\py{metadata_writer.description()}. \\
```
