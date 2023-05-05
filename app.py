import uvicorn
from factory import create_app


if __name__ == '__main__':
    app = create_app()
    uvicorn.run(app, port=8080)
