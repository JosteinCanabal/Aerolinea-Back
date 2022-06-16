from typing import Union
from app.user.userController import userRouter
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.catalog.flightcontroller import flightRouter
from app.auth.authController import auth
from app.database.database import Base, engine
from app.booking.bookingController import bookingRouter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# nombre @nombre de la variable que define FastApi
# uvicorn main:nombre

Base.metadata.create_all(bind=engine)


@app.get("/")
def docs():
    return RedirectResponse("http://localhost:8000/docs")


app.include_router(bookingRouter)
app.include_router(flightRouter)
app.include_router(userRouter)
app.include_router(auth)
