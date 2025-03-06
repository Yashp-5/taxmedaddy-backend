from fastapi import FastAPI
from app.auth.auth import router as auth_router

app=FastAPI()
app.include_router(auth_router,prefix="/auth",tags=["Authentication"])
@app.get("/")
def read_root():
    return{"message":"TaxMeDaddy backend is running now🚀"}
