import uvicorn

if __name__ == "__main__":
    # Run the FastAPI application on a different port to avoid conflicts
    uvicorn.run("src.backend.main:app", host="0.0.0.0", port=8001, reload=False)