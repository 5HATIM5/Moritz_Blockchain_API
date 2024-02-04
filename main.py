import uvicorn
import os
from dotenv import load_dotenv
from app.api import app

load_dotenv()

PORT = int(os.getenv("PORT", 8000))
HOST = "0.0.0.0"

if __name__ == "__main__":
    uvicorn.run(app, port=PORT, host=HOST, reload=True)
