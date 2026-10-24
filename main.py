
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api.routes import router
from core.config import get_settings, BASE_DIR
from core.logging import configure_logging
from services.audit import init_db


# Initialize application settings and services
configure_logging()
settings = get_settings()
init_db()


# Initialize FastAPI app
app = FastAPI(
    title=settings.app_name,
    version="1.0.0"
)


# Register API routes
app.include_router(router)


# Static files configuration
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)


# HTML templates configuration
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# Homepage
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": settings.app_name
        }
    )
