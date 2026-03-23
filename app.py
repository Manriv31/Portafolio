from pathlib import Path
import subprocess
import tempfile
import shutil
import glob
import os
import copy
import re

from flask import Flask, abort, render_template, request, send_from_directory, send_file, after_this_request
from data import portfolio_data

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
CV_DIR = BASE_DIR / "static" / "cv"


def _get_social_url(icon_name: str) -> str:
    for social in portfolio_data.get("social_links", []):
        if social.get("icon") == icon_name:
            return social.get("url", "#")
    return "#"


@app.route("/")
def index():
    # Attach per-project image lists (from static/img/projects/<slug> folders) before rendering
    data = _attach_project_images(portfolio_data)
    return render_template("index.html", data=data)


@app.route("/experiencia")
def experience():
    social = {
        "github": _get_social_url("github"),
        "linkedin": _get_social_url("linkedin"),
    }
    return render_template("experience.html", data=portfolio_data, social=social)


@app.route("/projects")
def projects():
    # Página dedicada que muestra todos los proyectos con imagen, título, descripción y stack
    data = _attach_project_images(portfolio_data)
    return render_template("projects.html", data=data)


def _attach_project_images(data_source: dict) -> dict:
    """Return a deepcopy of data_source where each project has an 'images' list populated
    from folders under static/img/projects/<slug>/ if present. The slug is derived from the
    project's `image` filename stem (e.g. akira.svg -> akira) or fallback to a slugified name.
    """
    data = copy.deepcopy(data_source)
    projects = data.get("projects", [])
    projects_dir = BASE_DIR / "static" / "img" / "projects"

    for p in projects:
        # derive slug from image path if available
        slug = None
        img_path = p.get("image")
        if img_path:
            try:
                slug = Path(img_path).stem
            except Exception:
                slug = None

        if not slug:
            name = p.get("name", "") or ""
            slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or None

        found = False
        if slug:
            folder = projects_dir / slug
            if folder.exists() and folder.is_dir():
                imgs = sorted([f.name for f in folder.iterdir() if f.suffix.lower() in ('.png', '.jpg', '.jpeg', '.webp', '.svg')])
                if imgs:
                    # overwrite any existing images list with the folder contents
                    p['images'] = [f"/static/img/projects/{slug}/{name}" for name in imgs]
                    found = True

        if not found:
            # fallback to existing single image or site default
            p['images'] = [p.get('image') or '/static/img/Manu-pixel.png']

    return data


@app.route("/cv/download")
def download_cv():
    # Serve pre-generated PDF files from static/cv/ based on `lang`
    lang = request.args.get("lang", "es").lower()

    # Map languages to the PDF filenames present in static/cv/
    pdf_map = {
        "es": "Manuel_Rivera_CV_es.pdf",
        "en": "Manuel_Rivera_CV_en.pdf",
    }

    filename = pdf_map.get(lang, pdf_map["es"])  # default to Spanish
    file_path = CV_DIR / filename

    if not file_path.exists():
        abort(404)

    download_name = f"{file_path.stem}.pdf"
    return send_file(file_path, as_attachment=True, download_name=download_name)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
