from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index(name: str | None = None, message: str | None = None):
    if not name:
        return "Specify `?name=` query parameter."
    if not message:
        return "Specify `?message=` query parameter."
    
    return f"Hello {name}! {message}!"