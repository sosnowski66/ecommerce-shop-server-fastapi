from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

from api import products_router, category_router, auth_router, users_router, orders_router, payments_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.add_middleware(SessionMiddleware, secret_key="random-string")

app.include_router(products_router)
app.include_router(category_router)
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(orders_router)
app.include_router(payments_router)
