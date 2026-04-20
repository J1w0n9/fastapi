from fastapi import *

app = FastAPI()


@app.get("/hello")
def hello_world():
    return "hello world"


@app.get("/hi1/{who}")
def greet(who):
    return f"Hello? {who}?"


@app.post("/hi2")
def greet(who: str = Body(embed=True)):
    return f"Hello? {who}?"

{
    "who" : "Mom"
}

@app.post("/hi3")
def greet(who: str = Header()):
    return f"Hello? {who}?"


@app.get("/agent")
def get_agent(user_agent: str = Header()):
    return user_agent


if __name__ == '__main__':
    import uvicorn

    uvicorn.run("hello:app", host="0.0.0.0", port=8000)
