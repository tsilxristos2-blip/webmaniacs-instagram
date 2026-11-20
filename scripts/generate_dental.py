"""Generate a square WEBMANIACS dental-clinic Instagram concept."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W=1080
im=Image.new("RGB",(W,W),(8,20,37))
d=ImageDraw.Draw(im)
for y in range(W):
    t=y/W
    d.line((0,y,W,y),fill=(int(8+7*t),int(20+26*t),int(37+47*t)))
def font(size,bold=False):
    candidates=["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for p in candidates:
        if Path(p).exists(): return ImageFont.truetype(p,size)
    return ImageFont.load_default()
white="#f5faff"; cyan="#42d8f5"; muted="#b9cbdc"
d.rounded_rectangle((60,55,1020,1025),radius=40,outline="#24485f",width=3)
d.text((105,95),"WEBMANIACS",font=font(42,True),fill=white)
d.rounded_rectangle((105,170,420,176),radius=3,fill=cyan)
d.text((105,225),"DENTAL CARE",font=font(77,True),fill=white)
d.text((108,330),"Modern dental website concept",font=font(31),fill=muted)
# Desktop monitor mockup
d.rounded_rectangle((102,415,790,810),radius=24,fill="#111d2d",outline="#6c93a8",width=6)
d.rounded_rectangle((120,433,772,773),radius=12,fill="#eefaff")
d.rectangle((120,433,772,490),fill="#d9f2fa")
d.text((145,445),"dentalcare",font=font(25,True),fill="#163f5d")
d.text((570,452),"HOME   SERVICES",font=font(14,True),fill="#32637a")
d.text((150,535),"Your smile,",font=font(49,True),fill="#133b57")
d.text((150,590),"our priority.",font=font(49,True),fill="#133b57")
d.rounded_rectangle((150,677,355,725),radius=15,fill="#00a6ca")
d.text((168,690),"BOOK A VISIT",font=font(18,True),fill="white")
# Tooth symbol
d.ellipse((540,530,695,685),fill="#a8e6f2")
d.text((572,545),"+",font=font(100,True),fill="#137b9a")
d.polygon([(380,810),(515,810),(550,854),(345,854)],fill="#718c9f")
d.rounded_rectangle((305,852,590,870),radius=8,fill="#a4b8c8")
# Mobile
d.rounded_rectangle((735,525,955,893),radius=32,fill="#122438",outline="#7ba4b9",width=6)
d.rounded_rectangle((750,549,940,868),radius=22,fill="#f0fbff")
d.text((767,582),"dentalcare",font=font(20,True),fill="#145c77")
d.text((765,650),"Smile with",font=font(22,True),fill="#164c68")
d.text((765,683),"confidence",font=font(22,True),fill="#164c68")
d.rounded_rectangle((766,755,920,799),radius=12,fill="#06a9cc")
d.text((776,767),"BOOK NOW",font=font(17,True),fill="white")
d.text((105,940),"WEB DESIGN  /  MOBILE FIRST  /  ONLINE BOOKINGS",font=font(22,True),fill=cyan)
out=Path("images/instagram/dental-care-concept.jpg")
out.parent.mkdir(parents=True,exist_ok=True)
im.save(out,"JPEG",quality=92,optimize=True)
print(out)
