from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import auth, location, payment, funds

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(location.router)
app.include_router(payment.router)
app.include_router(funds.router)
