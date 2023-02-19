from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, RedirectResponse

app = FastAPI()

# allow any origin
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root() -> RedirectResponse:
    """API root."""
    return RedirectResponse(url="/docs")


@app.get("/hello")
async def hello() -> HTMLResponse:
    return HTMLResponse("<h1>Hello World!</h1>")
