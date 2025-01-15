import os
import os.path


def safe_open_w(path):
    """
    Open a file for writing, creating any parent directories as needed.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, "wb")
