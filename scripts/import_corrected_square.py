from urllib.request import urlopen
from io import BytesIO
from PIL import Image
from pathlib import Path
FILES=[["dietitian","https://d2jqrm6oza8nb6.cloudfront.net/datasets/5b48a906-b561-40c2-b527-a34ea804bbd0.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNmNkOTgzZjE3YmMyMDkyMiIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTM0OTYxN30.HFa_dkuEqSq9wPpMdl1_zovRLeYhM3CtxcQFWNNB8LM"],["doctor","https://d2jqrm6oza8nb6.cloudfront.net/datasets/7f736847-524e-4bfe-8007-1406af926e69.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiZmM1M2NkOTE4YzkxZDVlYiIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTMxNTM0NX0._YNex87KraRIJ-SWktuRusIKDR44Ehyz-1Bwe6u0EO8"],["lawyer","https://d2jqrm6oza8nb6.cloudfront.net/datasets/c7201f6e-c4b4-4956-9e46-625dfd982472.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMTcyMTg4NmUxM2U0YWZjMiIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTM1Njc4Mn0.qnwgox7QLS59ki2MGwE5TZGlmB1FIGGr41wql8ozJSk"],["tutoring","https://d2jqrm6oza8nb6.cloudfront.net/datasets/1b55eadc-ad16-4d76-993f-b9091575e955.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMzlhNWRlYWNkZWQ2YmI5YyIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsImV4cCI6MTc5NTMxNTc1Nn0.optr4Ewdi7AMYWa3kVeGnBK4KI6RJgTyCdMuaKaAO-g"],["physiotherapy","https://d2jqrm6oza8nb6.cloudfront.net/datasets/6e23adcf-14ad-40d9-aae4-57d190e3f56f.png?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiMzZmYWEzOGQxMTRhNGJhYSIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsImV4cCI6MTc5NTI5NDczM30.iArBO4o5qEOsDJgDbkeXyTkkrb8jjVyRbU_H7PGrxyk"]]
for name,url in FILES:
    with urlopen(url,timeout=50) as response:
        img=Image.open(BytesIO(response.read())).convert("RGB")
    assert img.width==img.height, f"Image {name} must be square: {img.size}"
    img=img.resize((1080,1080),Image.Resampling.LANCZOS)
    path=Path("images/instagram")/f"{name}-corrected-square.jpg"
    path.parent.mkdir(parents=True,exist_ok=True)
    img.save(path,"JPEG",quality=94,optimize=True)
    assert Image.open(path).size==(1080,1080)
    print(name,img.size,path.stat().st_size)
