from fastapi import FastAPI  # pyright: ignore[reportMissingImports]

app = FastAPI(
    title="KaushalSetu API",
    description="Government skilling intelligence platform",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "kaushalsetu-api"
    }