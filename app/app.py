from config import app
from auth import *
from quiz_routes import *

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True)
