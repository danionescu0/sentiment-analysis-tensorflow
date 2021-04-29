import os

config = {
    "language": "ro"
}


def read_env_var(name: str) -> str:
    if os.environ.get(name) is None:
        return config[name]
    try:
        with open(os.environ.get(name), 'r') as file:
            return file.read()
    except:
        return os.environ.get(name)