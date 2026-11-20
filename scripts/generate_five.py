from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT=Path("images/instagram")
ROOT.mkdir(parents=True,exist_ok=True)
FONT="/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
def f(n,b=False): return ImageFont.truetype(BOLD if b else FONT,n)
def rgb(h): return tuple(bytes.fromhex(h.lstrip("#")))
def mix(a,b,t): return tuple(round(x*(1-t)+y*t) for x,y in zip(a,b))
def txt(d,xy,s,n,col,b=False): d.text(xy,s,font=f(n,b),fill=col)
def pill(d,box,fill,text,ink="#ffffff",size=19):
    d.rounded_rectangle(box,radius=(box[3]-box[1])//2,fill=fill)
    bb=d.textbbox((0,0),text,font=f(size,True))
    txt(d,(box[0]+(box[2]-box[0]-(bb[2]-bb[0]))//2,box[1]+(box[3]-box[1]-(bb[3]-bb[1]))//2-3),text,size,ink,True)

concepts=[
 dict(slug="real-estate",category="REAL ESTATE",brand="NOVA ESTATES",hero="Find your next",hero2="place to belong.",subtitle="Premium property experience",feature="Property listings  /  Virtual tours",bg="#0d2031",bg2="#19465a",accent="#c6a876",soft="#f4eee5",dark="#253944",badge="EXPLORE HOMES",scene="house"),
 dict(slug="car-detailing",category="AUTO DETAILING",brand="GLOSS LAB",hero="Precision in",hero2="every detail.",subtitle="The ultimate car care studio",feature="Services  /  Online booking",bg="#10141d",bg2="#303d4e",accent="#e6b75d",soft="#f0f1f3",dark="#252d38",badge="BOOK A SERVICE",scene="car"),
 dict(slug="fitness-studio",category="FITNESS STUDIO",brand="PULSE STUDIO",hero="Stronger starts",hero2="right here.",subtitle="Train with purpose",feature="Class schedule  /  Memberships",bg="#19151d",bg2="#433044",accent="#f16c91",soft="#f8eff3",dark="#332533",badge="JOIN THE MOVEMENT",scene="fitness"),
 dict(slug="restaurant",category="RESTAURANT",brand="TERRA TABLE",hero="A taste worth",hero2="remembering.",subtitle="Fresh flavors. Warm moments.",feature="Digital menu  /  Reservations",bg="#17241c",bg2="#405542",accent="#e6b780",soft="#faf4e9",dark="#344437",badge="RESERVE A TABLE",scene="plate"),
 dict(slug="beauty-salon",category="BEAUTY SALON",brand="MAISON BEAUTY",hero="Your beauty,",hero2="reimagined.",subtitle="A little time, just for you",feature="Treatments  /  Appointments",bg="#33232b",bg2="#78575f",accent="#f0c6b8",soft="#fcf4f0",dark="#604550",badge="BOOK AN APPOINTMENT",scene="beauty")
]
def scene(d,kind,cx,cy,accent):
    if kind=="house":
        d.polygon([(cx-120,cy),(cx,cy-105),(cx+120,cy),(cx+120,cy+140),(cx-120,cy+140)],fill="#d5e1dc")
        d.polygon([(cx-155,cy+5),(cx,cy-125),(cx+155,cy+5)],fill=accent)
        d.rectangle((cx-40,cy+55,cx+45,cy+140),fill="#537383")
        d.rectangle((cx-100,cy+35,cx-60,cy+80),fill="#9ac4c6")
    elif kind=="car":
        d.rounded_rectangle((cx-165,cy+12,cx+165,cy+95),radius=28,fill="#cad5de")
        d.polygon([(cx-100,cy+12),(cx-52,cy-57),(cx+80,cy-57),(cx+130,cy+12)],fill="#a8c3d3")
        d.ellipse((cx-125,cy+73,cx-65,cy+132),fill="#252a34")
        d.ellipse((cx+75,cy+73,cx+135,cy+132),fill="#252a34")
        d.line((cx-150,cy+30,cx+150,cy+30),fill=accent,width=8)
    elif kind=="fitness":
        d.rounded_rectangle((cx-145,cy-10,cx+145,cy+25),radius=15,fill="#3e3740")
        for x in [cx-145,cx-115,cx+95,cx+125]:
            d.rounded_rectangle((x,cy-55,x+20,cy+70),radius=8,fill=accent)
    elif kind=="plate":
        d.ellipse((cx-160,cy-130,cx+160,cy+190),fill="#e6e1d5")
        d.ellipse((cx-125,cy-95,cx+125,cy+155),fill="#f7f6f0")
        for i in range(8):
            ang=i*math.pi/4
            x=cx+70*math.cos(ang); y=cy+30+70*math.sin(ang)
            d.ellipse((x-20,y-20,x+20,y+20),fill=["#7a9966","#d9a36c","#bf7560"][i%3])
    elif kind=="beauty":
        d.ellipse((cx-110,cy-125,cx+110,cy+125),fill="#e8c6b8")
        d.arc((cx-118,cy-145,cx+118,cy+145),180,360,fill="#805b66",width=26)
        d.ellipse((cx-62,cy-12,cx-45,cy+1),fill="#71505a")
        d.ellipse((cx+45,cy-12,cx+62,cy+1),fill="#71505a")
        d.arc((cx-40,cy+25,cx+40,cy+75),0,180,fill="#a46473",width=4)

def render(c):
    im=Image.new("RGB",(1080,1080))
    d=ImageDraw.Draw(im)
    a=rgb(c["bg"]); b=rgb(c["bg2"])
    for y in range(1080):
        d.line((0,y,1080,y),fill=mix(a,b,y/1080))
    accent=c["accent"]; soft=c["soft"]; dark=c["dark"]
    d.ellipse((680,-160,1300,460),outline=accent,width=2)
    d.ellipse((770,-75,1200,350),outline=accent,width=2)
    d.rounded_rectangle((46,45,1034,1033),radius=37,outline="#68717b",width=2)
    txt(d,(88,78),"WEBMANIACS",40,"#ffffff",True)
    pill(d,(815,84,985,125),accent,"PORTFOLIO",dark,17)
    d.rounded_rectangle((88,171,430,177),radius=3,fill=accent)
    txt(d,(88,215),c["category"],30,accent,True)
    txt(d,(86,274),c["hero"],63,"#ffffff",True)
    txt(d,(86,350),c["hero2"],63,"#ffffff",True)
    txt(d,(90,446),c["subtitle"],26,"#d5dce1")
    # laptop screen
    d.rounded_rectangle((86,531,796,890),radius=22,fill="#101820",outline="#a1acb2",width=5)
    d.rounded_rectangle((103,547,779,862),radius=10,fill=soft)
    d.rounded_rectangle((103,547,779,606),radius=10,fill="#ffffff")
    txt(d,(127,562),c["brand"],24,dark,True)
    txt(d,(610,568),"ABOUT  CONTACT",12,dark,True)
    txt(d,(128,640),c["hero"],37,dark,True)
    txt(d,(128,685),c["hero2"],37,dark,True)
    pill(d,(130,766,350,815),accent,c["badge"],dark,14)
    d.rounded_rectangle((473,618,748,840),radius=20,fill="#d6dfd9")
    scene(d,c["scene"],610,690,accent)
    d.polygon([(340,890),(546,890),(578,919),(311,919)],fill="#8b9ba6")
    d.rounded_rectangle((260,916,622,928),radius=6,fill="#bcc7cb")
    # phone
    d.rounded_rectangle((770,600,992,962),radius=30,fill="#111a24",outline="#a4b3bd",width=5)
    d.rounded_rectangle((783,617,979,945),radius=22,fill=soft)
    txt(d,(800,652),c["brand"],15,dark,True)
    d.rounded_rectangle((797,690,965,829),radius=15,fill="#d6dfd9")
    scene(d,c["scene"],879,739,accent)
    txt(d,(797,850),c["category"],15,dark,True)
    pill(d,(798,885,962,923),accent,"EXPLORE",dark,15)
    txt(d,(88,968),c["feature"],22,"#f4f6f7",True)
    path=ROOT/(c["slug"]+"-website-concept.jpg")
    im.save(path,"JPEG",quality=89,optimize=True)
    print(str(path),path.stat().st_size)

for concept in concepts: render(concept)
