import logging
from pathlib import Path
import os

from flask import Flask
from dotenv import load_dotenv

# breakpoint()


load_dotenv()

app = Flask(__name__)

from app import views, admin_views

app.config["MAX_CONTENT_LENGTH"] = 50 * 1024 * 1024
app.config["PHRASEFILE_EXTENSIONS"] = {".txt"}
app.config["SOUNDFILE_EXTENSIONS"] = {".wav"}

# TODO: remove this when the memory solution works
app.config["FILE_FOLDER"] = os.getenv("APG_FILE_FOLDER")
try:
    Path(app.config["FILE_FOLDER"]).mkdir(parents=True, exist_ok=True)
except OSError:
    pass

logging.basicConfig(
    filename="flask.log",
    level=logging.WARN,
    format=f"%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)
