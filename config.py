CONFIG = {
    "max_retries": 3,
    "timeout": 5,
    "default_file": "data.txt"
}


def get_config(key):
    return CONFIG.get(key, None)
