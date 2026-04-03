import datetime

def log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}")


def log_error(error):
    log(f"ERROR: {error}")


def log_info(info):
    log(f"INFO: {info}")
