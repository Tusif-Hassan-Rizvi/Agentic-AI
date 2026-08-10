from fastapi import FastAPI

app=FastAPI(
    title="Expense Tracker API",
    description="Production-ready Expense Tracker Backend with Authentication",
    version="1.0.0"
)


@app.get('/')
def health_check():
     return {
        "status": "success",
        "message": "Expense Tracker API is running smoothly!"
    }