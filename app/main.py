from fastapi import FastAPI,Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from urllib.parse import urljoin  


# ======Static files config===========
STATIC_ROOT = "/vol/web/static/"
STATIC_URL = "/pub/static/"
# ====================================

# ======App config====================
app = FastAPI()
app.mount(STATIC_URL, StaticFiles(directory=STATIC_ROOT), name="static")
# ====================================


@app.get("/docs", include_in_schema=False)
async def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        swagger_favicon_url=f"{STATIC_URL}images/poonga.jpeg"
    )

@app.get("/") 
def read_root(request:Request):
    base_url = str(request.base_url)  # Convert to string
    # Construct full URL for the image
    full_image_url = urljoin(base_url, STATIC_URL + "images/poonga.jpeg")
    return {"Hello": full_image_url} 