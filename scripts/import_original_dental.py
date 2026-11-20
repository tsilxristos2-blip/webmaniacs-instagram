from urllib.request import urlopen
from PIL import Image
from io import BytesIO
from pathlib import Path
URL="https://d2jqrm6oza8nb6.cloudfront.net/datasets/ba1aea5b-155a-4c73-9bd7-297ed64948a5.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMGIwYzJlOTNkNWFhNGE1NSIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTMyNTMzMX0.QpCynyBZdrNzj8E3kRtWdf9Ta-D3wPEZZv90cfrEnXw"
out=Path("images/instagram/dental-care-original.jpg")
out.parent.mkdir(parents=True,exist_ok=True)
with urlopen(URL,timeout=40) as r:
    data=r.read()
im=Image.open(BytesIO(data)).convert("RGB")
im.save(out,"JPEG",quality=94,optimize=True)
print(f"Saved original supplied dental design: {out}, {im.size}")
