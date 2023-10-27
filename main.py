from fastapi import FastAPI

from src import router

app = FastAPI(debug=True)
app.include_router(router=router)
