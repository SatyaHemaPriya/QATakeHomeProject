from fastapi import FastAPI

from src import router

app = FastAPI(debug=True, docs_url="/docs")
app.include_router(router=router)
