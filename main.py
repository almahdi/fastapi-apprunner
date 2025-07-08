from fastapi import FastAPI

from starlette.requests import Request
import logging

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# Add request logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger = logging.getLogger("request_logger")
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)