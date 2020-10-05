import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.token.routes import router as auth_router
from app.user.routes import router as user_router
from app.config import jinja_env

app = FastAPI()


#app.add_middleware(HTTPSRedirectMiddleware)




app.mount("/static", StaticFiles(directory="static"), name="static")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")


app.include_router(user_router, prefix="/api/v1")
app.include_router(auth_router, prefix="/api/v1")

@app.get('/')
async def welcome():
    file = open('templates/index.html', mode="r")
    return HTMLResponse(content=file.read())