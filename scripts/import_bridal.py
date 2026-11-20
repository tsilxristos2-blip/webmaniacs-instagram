from urllib.request import urlopen
from pathlib import Path
url="https://d2jqrm6oza8nb6.cloudfront.net/datasets/c940dcd1-1457-47d3-b7de-9310fd171cc7.jpg?_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXlIYXNoIjoiNjhkNjc2ZjM2ZTRiMzNhMyIsImJ1Y2tldCI6InJ1bndheS1kYXRhc2V0cyIsInN0YWdlIjoicHJvZCIsImV4cCI6MTc5NTM0NjQxOX0.sQ2nFwyLPDGe8iKyfK_LGGi0A7nf4w1lkkEKyZtM_JA"
out=Path("images/instagram/bridal-atelier-premium.jpg")
out.parent.mkdir(parents=True,exist_ok=True)
with urlopen(url,timeout=45) as r: out.write_bytes(r.read())
print(out,out.stat().st_size)
