from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from PIL import Image
import io
import os

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(BASE_DIR, "static")),
    name="static",
)
templates = Jinja2Templates(directory="templates")

RAMP = "@%#*+=-:. "

def to_ascii(img: Image.Image, width: int=120, aspect: float=0.55) -> str:
    img = img.convert("L")      # grayscale conversion
    
    w, h = img.size
    new_w = max(1, int(width))
    new_h = max(1, int((h / w) * new_w * aspect))
    img = img.resize((new_w, new_h))
    
    pix = img.load()
    lines = []
    for h in range(new_h):
        row = []
        for w in range(new_w):
            v = pix[w, h]
            idx = v * (len(RAMP) - 1) // 255
            row.append(RAMP[idx])
        lines.append("".join(row))
    return "\n".join(lines)

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})    

@app.post("/api/convert")
async def convert(
    file: UploadFile = File(...),
    width: int = 120,
):
    # Basic content-type check (not bulletproof but helpful)
    if not file.content_type or not file.content_type.startswith("image/"):
        return JSONResponse({"error": "Please upload an image file."}, status_code=400)

    data = await file.read()

    try:
        img = Image.open(io.BytesIO(data))
        ascii_art = to_ascii(img, width=width)
        return {"ascii": ascii_art}
    except Exception:
        return JSONResponse({"error": "Could not read that image."}, status_code=400)