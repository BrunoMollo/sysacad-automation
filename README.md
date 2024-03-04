# Automatizacion para inscribirse a cursar en el Sysacad FRRO

## Como correrlo
1. Instalar dependecias para Linux/Mac (Windows queda como un ejercicio para el lector):
```sh
python3 -m venv .venv
source .venv/bin/activate
pip install selenium
```
2. Cambiar la configuracion de las variables en el archivo `main.py`, esta al principio y con comentarios
3. Correr el script con el siguiente comando:
```sh
source .venv/bin/activate
python3 main.py
```
4. Esperar a que termine. Puede parecer que salen un monton de errores, ignoralos. Durante la ejecucion se van a ir sacando screen de las distintas pantallas para que veas que va ocurriendo.

## Aclaración
Esta cosa no fue muy testeada, la arme en una hora durante la inscripcion y la probe con 3 materias de quinto nomas en 2024. 
Cualquier actualizacion del Sysacad puede romper todo al carajo. No se si se podra usar en otras regionaeles.
Si al usar esto terminas inscripto en Licenciatura en Turismo en Tucuman, es tu problema por confiar.

Saludos.

