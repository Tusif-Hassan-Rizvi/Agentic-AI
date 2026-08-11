from fastapi import FastAPI, Request, status, HTTPException
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.database import engine, Base
from app.models import user_model  # Registers User model with SQLAlchemy
from app.routers import auth_router

# Auto-create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Expense Tracker API",
    description="Production-ready Expense Tracker Backend",
    version="1.0.0"
)


# 1. Converts Validation Errors to {"message": "..."}
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    first_error = exc.errors()[0]
    field = first_error["loc"][-1]
    msg = first_error["msg"]
    
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"message": f"{field.capitalize()}: {msg}"}
    )


# 2. Converts HTTPExceptions to {"message": "..."}
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )


# Mount Routers
app.include_router(auth_router.router)


@app.get("/")
def health_check():
    return {
        "status": "success",
        "message": "Expense Tracker API is running smoothly!"
    }