from fastapi import FastAPI
from routers import user

app = FastAPI()

# Sử dụng router đã tạo
app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
