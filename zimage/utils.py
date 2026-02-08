import os
from datetime import datetime

def create_output_dir():
    folder = "outputs"
    os.makedirs(folder, exist_ok=True)
    return folder

def generate_filename(prefix="img"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{prefix}_{timestamp}.png"
