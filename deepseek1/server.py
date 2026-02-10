from flask import Flask, request, Response, stream_with_context
from flask_cors import CORS
import ollama
import json

app = Flask(__name__, static_folder="public", static_url_path='')
CORS(app)