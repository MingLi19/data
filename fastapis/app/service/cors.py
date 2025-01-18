from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    origins = [
        "http://127.0.0.1:8000"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
