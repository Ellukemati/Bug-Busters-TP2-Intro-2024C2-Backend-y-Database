# TP2 Introduccion al Desarrollo de Software
Este repositorio fue creado por alumnos de Introducción al Desarrollo de Software TB022 curso Esteban, como parte de la entrega del TP2.

### Pre-requisitos

Version de Python 3.10.12 en adelante
(Opcional) Format Linter recomendado: Black Formatter
```
pip install pylint
```
### Archivos CSV:
- moves.csv
- move_damage_class
- move_effect_prose.csv
- type_names.csv
- pokemon.csv
- pokemon_stats.csv
- pokemon_types.csv
- type_names.csv
- pokemon_abilities.csv
- ability_names.csv
- pokemon_evolutions.csv
- moves_name.csv

### Crear archivo de DataBase:
 Se debe llamar _'database.db'_ , y debe estar en la carpeta app/db

## Instalación


### Crear Ambiente Virtual:

```
python3 -m venv venv
```
### Activar ambiente virtual:
```
source venv/bin/activate
```
## Dependencias:
### Sin el ambiente virtual activado:
```
pip install sqlite3 
```
### Con el ambiente virtual activado:
```
pip install pytest
```
```
pip install fastapi[standard]
```
```
pip install coverage
```
```
pip install slqmodel
```
```
pip install alembic
```

### Correr las migraciones (poner al dia la DB):
```
alembic upgrade head
```
## Ejecutar las pruebas
(Necesito tener el ambiente virtual activado)

_Parados en la carpeta test, con los archivos CSV ejecutamos:_
```
pytest <nombre_archivo_prueba>
```
_Para ver el coverage:_
```
coverage run -m pytest
```
```
coverage html
```
## Levantar Servidor:
(Desde la carpeta principal, junto con los archivos csv, y el ambiente virtual activado)
```
fastapi dev main.py
```
