# Tarea 01 – Flask

Aplicacion web desarrollada con **Python** y **Flask** que implementa un
CRUD completo de usuarios, endpoints tipo API (JSON) y un buscador dinamico
consumido desde el frontend con **HTMX**, sin usar frameworks como React,
Vue o Angular.

## Descripcion del proyecto

La aplicacion permite:

- Crear, listar, ver el detalle, editar y eliminar usuarios (`User`).
- Consultar los mismos datos mediante endpoints JSON (`/api/users`).
- Buscar usuarios por nombre en tiempo real, sin recargar la pagina,
  usando HTMX para consumir el endpoint `/api/users/search`.

## Requisitos previos

- [Python 3.12+](https://www.python.org/)
- [uv](https://docs.astral.sh/uv/) como administrador de dependencias
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/) (recomendado, con la
  extension oficial de Python)

## Instalacion

1. Clonar el repositorio:

   ```bash
   git clone <URL_DE_TU_REPOSITORIO>
   cd tarea01-flask
   ```

2. Crear el archivo de variables de entorno a partir del ejemplo:

   ```bash
   cp .env.example .env
   ```

   Luego edita `.env` y cambia `SECRET_KEY` por un valor propio.

3. Crear el entorno virtual e instalar las dependencias con **uv**:

   ```bash
   uv sync
   ```

   Esto crea automaticamente la carpeta `.venv/` con el entorno virtual e
   instala todo lo listado en `pyproject.toml`.

## Ejecutar el proyecto

```bash
uv run run.py
```

La aplicacion quedara disponible en `http://127.0.0.1:5000`.

La base de datos SQLite se crea automaticamente (`database/app.db`) la
primera vez que se ejecuta la aplicacion; no requiere pasos manuales.

### Ejecutar desde VS Code

1. Abre la carpeta del proyecto en VS Code (`File > Open Folder`).
2. Instala la extension **Python** de Microsoft si no la tienes.
3. Selecciona el interprete del entorno virtual: `Ctrl+Shift+P` →
   `Python: Select Interpreter` → elige el que apunta a `.venv`.
4. Abre una terminal integrada (`` Ctrl+` ``) y ejecuta `uv run run.py`.
5. Abre `http://127.0.0.1:5000` en el navegador.

## Rutas principales

### Vistas (HTML)

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/` | Pagina principal |
| GET | `/users` | Listado de usuarios |
| GET | `/users/new` | Formulario de creacion |
| POST | `/users` | Crea un usuario |
| GET | `/users/<id>` | Detalle de un usuario |
| GET | `/users/<id>/edit` | Formulario de edicion |
| POST | `/users/<id>` | Actualiza un usuario |
| POST | `/users/<id>/delete` | Elimina un usuario |
| GET | `/buscador` | Buscador dinamico con HTMX |

### API (JSON)

| Metodo | Ruta | Descripcion |
|---|---|---|
| GET | `/api/users` | Lista todos los usuarios |
| GET | `/api/users/<id>` | Retorna un usuario |
| GET | `/api/users/search?given_name=Juan` | Busca usuarios por nombre |

## Arquitectura utilizada

El proyecto sigue una separacion de responsabilidades en capas:

```
app/
├── config.py         -> Configuracion leida desde variables de entorno
├── database/         -> Instancia de SQLAlchemy compartida
├── models/            -> Entidades de datos (User)
├── schemas/           -> Validacion de datos de entrada
├── repositories/       -> Acceso a la base de datos (consultas SQLAlchemy)
├── services/          -> Logica de negocio (usa repositories, valida con schemas)
├── routes/            -> Controladores HTTP (web y API), usan services
├── templates/         -> Vistas Jinja2
└── static/            -> CSS
```

Flujo de una peticion: **routes -> services -> repositories -> models**.
Las rutas nunca acceden directamente a la base de datos: siempre pasan por
la capa de servicios, que aplica las validaciones antes de delegar en el
repositorio.

## Variables de entorno

| Variable | Descripcion |
|---|---|
| `SECRET_KEY` | Clave secreta de Flask (sesiones, flash messages) |
| `FLASK_ENV` | `development` o `production` |
| `DATABASE_URL` | Cadena de conexion de la base de datos (SQLite por defecto) |

El archivo `.env` **no** se sube al repositorio (esta en `.gitignore`).
Se incluye `.env.example` como plantilla.

## Capturas de pantalla

> Agregar aqui las capturas de: pagina principal, listado de usuarios,
> formulario de creacion, detalle de usuario y buscador HTMX en accion.

