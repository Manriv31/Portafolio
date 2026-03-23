# 🌐 Portfolio Personal

Sitio web de portafolio personal construido con **Python (Flask)**, inspirado en el diseño minimalista y moderno de [hirok.io](https://hirok.io/).

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)

## ✨ Características

- **Tema oscuro** moderno con acentos en púrpura
- **Animaciones suaves** fade-in al hacer scroll (Intersection Observer)
- **Navbar fija** con efecto blur/glassmorphism
- **Diseño responsive** — móvil, tablet y escritorio
- **Reloj local** en tiempo real
- **Grid de proyectos** con estadísticas (estrellas, descargas)
- **Secciones:** Hero, Proyectos, Experiencia, Consultoría, Contacto
- **Fácil personalización** — toda la data en un solo archivo Python

## 📁 Estructura

```
Portafolio/
├── app.py                 # Servidor Flask
├── data.py                # Datos del portafolio (editar aquí)
├── requirements.txt
├── static/
│   ├── css/style.css      # Estilos
│   ├── js/main.js         # Interactividad
│   └── img/               # Imágenes (ej. portrait.webp)
└── templates/
    ├── base.html           # Template base
    └── index.html          # Página principal
```

## 🚀 Inicio rápido

### Requisitos previos

- Python 3.8+

### Instalación

```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/portafolio.git
cd portafolio

# Crear entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python app.py
```

Abre **http://127.0.0.1:5000** en tu navegador.

## 🧰 Desarrollo y notas útiles

- El proyecto usa un entorno virtual; por convención local se suele usar `venv` o `.venv`.
- Si trabajas en Windows recuerda activar el entorno con:

```
venv\Scripts\activate
```

- Para generar el PDF del CV desde la UI el servidor invoca una herramienta externa (`rendercv`). Asegúrate de tenerla instalada en el mismo entorno que ejecuta `app.py` si quieres usar la función "Descargar CV".

- Archivos temporales y PDFs generados por la herramienta se excluyen mediante `.gitignore` (`static/cv/*.pdf`).

## Contribuir

- Modifica `data.py` para actualizar contenido y textos.
- Abre una rama nueva para cambios mayores y crea PR con una descripción breve de los cambios.


## 🎨 Personalización

Edita `data.py` para cambiar todo el contenido del sitio:

| Campo | Descripción |
|-------|-------------|
| `name` | Tu nombre completo |
| `role` | Tu cargo / título profesional |
| `tagline` | Descripción corta sobre ti |
| `timezone` / `location` | Zona horaria y ubicación |
| `projects` | Lista de proyectos destacados |
| `work` | Experiencia laboral actual y previa |
| `freelance` | Info de servicios freelance (o `enabled: False` para ocultar) |
| `social_links` | Redes sociales (GitHub, X, LinkedIn, Email) |
| `additional_links` | Links extra para el footer |

Para tu foto de perfil, coloca una imagen en `static/img/portrait.webp` y actualiza el campo `portrait` en `data.py`.

## 🛠 Tecnologías

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3 (custom properties, grid, flexbox), JavaScript vanilla
- **Fuente:** Inter (Google Fonts)

## 📄 Licencia

MIT — úsalo libremente para tu propio portafolio.
