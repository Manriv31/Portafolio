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
    lang = request.args.get("lang", "es").lower()
    cv_files = portfolio_data.get("cv_files", {})

    if lang == "es":
        # Compatibilidad con archivo nombrado como "sp" en este proyecto.
        filename = cv_files.get("es") or cv_files.get("sp")
    else:
        filename = cv_files.get("en")

    if not filename:
        abort(404)

    file_path = CV_DIR / filename
    if not file_path.exists():
        abort(404)

    # Use rendercv to render the YAML to PDF in a temporary directory, then serve the PDF
    temp_dir = tempfile.mkdtemp(prefix="rendercv_")

    try:
        # Prepare the YAML file name we want to render, and copy only
        # needed assets into temp_dir. Skip other CV YAML files to avoid
        # ambiguity when rendercv runs.
        src_name = Path(filename).name
        dest_yaml = Path(temp_dir) / src_name

        for item in CV_DIR.iterdir():
            dest = Path(temp_dir) / item.name
            if item.is_dir():
                shutil.copytree(item, dest)
                continue

            # If this is a YAML CV file but it's not the selected one, skip it
            if item.suffix in (".yaml", ".yml") and item.name != src_name:
                continue

            shutil.copy(item, dest)

        # Run rendercv in the temp dir against the copied file name.
        cmd = [
            "rendercv",
            "render",
            src_name,
            "-nomd",
            "-nohtml",
            "-nopng",
            "--quiet",
        ]

        # Ensure the subprocess uses UTF-8 for IO on Windows to avoid
        # UnicodeEncodeError when libraries (rich) write special chars.
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env["PYTHONUTF8"] = "1"

        proc = subprocess.run(
            cmd,
            cwd=temp_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )

        # Regardless of return code, check for produced PDFs (they may be
        # created even if the process returns a non-zero code). Prefer any
        # found PDF to serve to the user.
        pdfs = glob.glob(os.path.join(temp_dir, "*.pdf"))
        if not pdfs:
            # fallback: search recursively
            pdfs = glob.glob(os.path.join(temp_dir, "**", "*.pdf"), recursive=True)

        if pdfs:
            pdf_path = pdfs[0]

            @after_this_request
            def cleanup(response):
                try:
                    shutil.rmtree(temp_dir)
                except Exception:
                    pass
                return response

            download_name = f"{Path(filename).stem}_{lang}.pdf"
            return send_file(pdf_path, as_attachment=True, download_name=download_name)

        # No PDF produced — log and return 500.
        print("rendercv failed (no PDF produced):\n", proc.stdout, proc.stderr)

        @after_this_request
        def cleanup_err(response):
            try:
                shutil.rmtree(temp_dir)
            except Exception:
                pass
            return response

        abort(500, description="CV PDF not produced")
    except FileNotFoundError:
        # rendercv executable not found
        shutil.rmtree(temp_dir)
        abort(500, description="rendercv not installed on server")
    except Exception as e:
        try:
            shutil.rmtree(temp_dir)
        except Exception:
            pass
        print("Unexpected error generating CV:", e)
        abort(500)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
