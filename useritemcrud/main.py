from configuration.config import *
from app.api.user.router import *
import uvicorn

Base.metadata.create_all(bind=engine)
print("Fast api")
if __name__=="__main__":
    uvicorn.run("main:router",port=8000,reload=True)