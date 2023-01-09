import os
import files


def generate_path_upload(file):
    return os.path.abspath(os.path.join(os.path.dirname(files.__file__), file))
