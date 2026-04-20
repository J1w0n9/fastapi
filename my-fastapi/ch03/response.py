from fastapi import FastAPI
from starlette import status
from starlette.responses import JSONResponse, HTMLResponse, RedirectResponse

app = FastAPI()

@app.get("/resp_json/{item_id}", response_class=JSONResponse)
async def get_resp_json(item_id: int) -> JSONResponse:
    return JSONResponse(content={"message":"Hello World", "item_id": item_id}, status_code=status.HTTP_200_OK)

@app.get("/resp_html/{item_id}", response_class=HTMLResponse)
async def get_resp_html(item_id: int) -> HTMLResponse:
    html = f'''
    <html>
        <head>
            <title>Hello World</title>
        </head>
        <body>
            <h1>Hello World</h1>
            <p> item_id: {item_id} </p>
        </body>
    </html>'''
    return HTMLResponse(content=html, status_code=status.HTTP_200_OK)

@app.get("/redirect")
async def redirect_only(comment: str | None = None):
    return RedirectResponse(url=f"/resp_html/3?item_name={comment}")

@app.post("/create_redirect")
async def create_item(item_id: int, item_name: str):
    return RedirectResponse(
        url=f"/resp_html/{item_id}?item_name={item_name}",
        status_code=status.HTTP_302_FOUND
    )

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("response:app", host="0.0.0.0", port=8000)