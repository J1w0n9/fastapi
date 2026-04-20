from fastapi import FastAPI, Depends, HTTPException, Query

app = FastAPI()


class Database:
    def __init__(self):
        self.connection = "데이터베이스 연결"

    def get_connect(self):
        return self.connection

def user_dep(name: str = Query(...), gender: str = Query(...)):
    return {"name": name, "gender": gender}

def check_admin(token: str = Query(...)):
    if token != "secure_token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"role" : "admin"}

def get_db():
    db = Database()
    return db.get_connect()

async def verify_token(token: str = Query(...)):
    if token != "secure":
        raise HTTPException(status_code=401, detail="Invalid token")
app_dep = FastAPI(dependencies=[Depends(verify_token)])

@app.get("/user")
def get_user(user: dict = Depends(user_dep)) -> dict:
    return user
@app.get("/check_admin")
def check_admin(user: dict = Depends(check_admin)) -> dict:
    return {"message" : "welcome", "user" : user}

@app.get("/db")
async def read_db(connection: str = Depends(get_db)):
    return {"db_connect": connection}

@app_dep.get("/public")
async def public_endpoint():
    return {"message": "public endpoint!"}


@app_dep.get("/private")
async def private_endpoint():
    return {"message": "private endpoint!"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("depends:app", host="0.0.0.0", port=8000)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("depends:app_dep", host="127.0.0.1", port=8000)