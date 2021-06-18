import os

BASE_DIR = os.path.dirname(__file__)

# To get the file path in base dir
def base(filename):
    return os.path.join(BASE_DIR, filename)

# To get the file path in static dir
def static(filename):
    return os.path.join(BASE_DIR, 'static', filename)

# To get the file path in data dir
def data(filename):
    return os.path.join(BASE_DIR, 'data', filename)

# To get the file path in generated dir
def generated(filename):
    return os.path.join(BASE_DIR, 'generated', filename)
     