# Memorama

Memorama aplicando principios de Programación Funcional

Para poder jugar correctamente el juego necesita descargar las dependencias necesarias

## Dependencias

Primero, necesita crear el ambiente virtual

```shell
py -m venv env
```

Despues activamos el entorno virtual

```shell
.\env\Scripts\activate
```

Luego instalamos las dependencias del ambiente

```shell
py -m pip install -r requirements.txt
```

Despues correr el siguiente comando

```shell
pyinstaller --onefile Main.py
```

Por ultimo para ejecutar el juego ejecutamos el siguiente comando

```shell
.\dist\Main
```

Para cerrar el ambiente virtual se ejecuta este comando

```shell
deactivate
```