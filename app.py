from pathlib import Path
import subprocess
import tempfile
import shutil
import glob
import os

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
    return render_template("index.html", data=portfolio_data)


@app.route("/experiencia")
def experience():
    social = {
        "github": _get_social_url("github"),
        "linkedin": _get_social_url("linkedin"),
    }
    return render_template("experience.html", data=portfolio_data, social=social)


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
