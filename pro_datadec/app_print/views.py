from django.shortcuts import render
from .demo import main
import subprocess


def pri(request):

    subprocess.run(["streamlit", "run", main.st_app_path])
    streamlit_url = "http://localhost:8501"
    return render(request, "streamlit_iframe.html", {"streamlit_url": streamlit_url})
