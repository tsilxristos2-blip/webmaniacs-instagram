from urllib.request import urlopen
from PIL import Image, ImageFilter
from io import BytesIO
from pathlib import Path
URL="https://d2jqrm6oza8nb6.cloudfront.net/datasets/4bb14371-cf48-4680-8539-111359ec0e56.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMTFjMTVlZjBhZTEyMTBkNiIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTM3MDIyNH0.AfEn8U5bSPyPqr6m6j02EfBwT09sprh_0uFrgGHM4bI"
with urlopen(URL,timeout=50) as r: image=Image.open(BytesIO(r.read())).convert("RGB")
w,h=image.size
print("Original collage",image.size)
# Extract five independent complete panels, with margins avoiding white dividers.
panels=[
("dietitian", (0,0,0.499,0.495)),
("doctor", (0.501,0,1,0.495)),
("lawyer", (0,0.505,0.333,1)),
("tutoring", (0.335,0.505,0.665,1)),
("physiotherapy", (0.667,0.505,1,1)),
]
outdir=Path("images/instagram");outdir.mkdir(parents=True,exist_ok=True)
for name,(x0,y0,x1,y1) in panels:
    crop=image.crop((round(x0*w),round(y0*h),round(x1*w),round(y1*h)))
    # Preserve the entire layout and lettering. Pad the narrow bottom panels to square.
    bg=Image.new("RGB",(1080,1080),(9,25,41))
    scale=min(1080/crop.width,1080/crop.height)
    new=crop.resize((round(crop.width*scale),round(crop.height*scale)),Image.Resampling.LANCZOS)
    bg.paste(new,((1080-new.width)//2,(1080-new.height)//2))
    out=outdir/f"{name}-professional-premium.jpg"
    bg.save(out,"JPEG",quality=94,optimize=True)
    print(out,out.stat().st_size)

# Refresh professional image export.
