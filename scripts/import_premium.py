from urllib.request import urlopen
from PIL import Image
from io import BytesIO
from pathlib import Path
FILES=[["fitness-studio-premium.jpg","https://d2jqrm6oza8nb6.cloudfront.net/datasets/d93c6c42-23f7-43bf-bae3-a16ce2637180.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiZjI3ZmUwMGEwYjMwZmI5YyIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTM2OTA5OH0.RgKP6Ko6FmInnpfAiQIKux1eN4VF_s9k6Dz_bEIKSxg"],["real-estate-premium.jpg","https://d2jqrm6oza8nb6.cloudfront.net/datasets/7d7fee48-466c-43c6-ae44-b3fecd5220a7.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlYWI4Yzk3ZGJmNzg0MiIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTMzNjI2NX0.w3FSfwTcA2_gR087z8JW3NcrWHZ8h-GEhgqxiaRQDTY"],["restaurant-premium.jpg","https://d2jqrm6oza8nb6.cloudfront.net/datasets/3c35ab0d-b8af-4b15-8f35-6dccdd5e1089.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiOGQ3ZjQxODhhMGU2MzRkMiIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTMwNjUwNH0.SbOt1oElxr8GS3CqljIok6F8LXmtTKSyU-e2ygxjNrc"],["beauty-salon-premium.jpg","https://d2jqrm6oza8nb6.cloudfront.net/datasets/5cc8e222-bcb5-42b3-84e2-4e46b127965d.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNDE0MmUzNjkzNDM0NThlNSIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTM0NzQzM30.e7aeJI2fSuyiwp6rP73c3y9Cg_a88uFK54tMml0coHw"]]
for filename,url in FILES:
    out=Path("images/instagram")/filename
    out.parent.mkdir(parents=True,exist_ok=True)
    with urlopen(url,timeout=45) as response:
        im=Image.open(BytesIO(response.read())).convert("RGB")
    im.save(out,"JPEG",quality=92,optimize=True)
    print(filename,im.size,out.stat().st_size)
