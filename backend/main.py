from fastapi import FastAPI
# from auth import router as auth_router
from routers.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware
# from routers import products
from routers.products import router as products_router

app = FastAPI()

# Routing
app.include_router(auth_router)
app.include_router(products_router)
# app.include_router(products.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti "*" dengan domain spesifik jika diperlukan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)


