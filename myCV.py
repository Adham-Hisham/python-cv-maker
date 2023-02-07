from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF


width, height = A4

myCV = Drawing(width, height)

myCV.add(Rect(140, 530, 285, 260, strokeColor=colors.HexColor('#a5e4f3'),
 fillColor=colors.HexColor('#a5e4f3'))) 

myCV.add(Circle(140, 660, 130, strokeColor=colors.HexColor('#a5e4f3'),
 fillColor=colors.HexColor('#a5e4f3')))

myCV.add(Image(80, 560, 200, 200, 'p.jpg'))

myCV.add(Rect(80, 560, 200, 200, strokeColor=colors.HexColor('#FFFFFF'),
 fillColor=None, strokeWidth= 6)) 

myCV.add(Rect(300, 300, 280, 520,strokeColor=colors.HexColor('#66b2c0'),
 fillColor=colors.HexColor('#66b2c0'))) 

h = 800
h = h - 30

myCV.add(String(310, h, "Skills", fontSize = 18, fillColor=colors.HexColor('#FFFFFF'),
 fontName= 'Helvetica-Bold'))

skills = ['Python','Video Editing', 'Graphic Design', 'Linux','Office']

for skill in skills:
    h = h - 20
    myCV.add(String(320, h, f"\u2022 {skill}", fontSize = 15, fillColor=colors.HexColor('#FFFFFF'),
    fontName= 'Helvetica'))

h = h - 40

myCV.add(String(310, h, "Experience", fontSize = 18, fillColor=colors.HexColor('#FFFFFF'),
 fontName= 'Helvetica-Bold'))


jobs = ["Freelance Logo Designer"]

for job in jobs:
    h = h - 20
    myCV.add(String(320, h, f"\u2022 {job}", fontSize = 15, fillColor=colors.HexColor('#FFFFFF'),
    fontName= 'Helvetica'))

h = h - 40

myCV.add(String(310, h, "Projects", fontSize = 18, fillColor=colors.HexColor('#FFFFFF'),
 fontName= 'Helvetica-Bold'))

project1 = ["Personal Protofolio/Blog website"]
project1d = ["you can check out my website, via ","this link: cs-is-fun.tk"]

for project1 in project1:
    h = h - 20
    myCV.add(String(320, h, f"\u2022 {project1}", fontSize = 15, fillColor=colors.HexColor('#FFFFFF'),
    fontName= 'Helvetica-Bold'))

for d in project1d:
    h = h - 20
    myCV.add(String(335, h, d, fontSize = 15, fillColor=colors.HexColor('#FFFFFF'),
    fontName= 'Helvetica'))

project2 = ["Generating my CV using Python"]
project2d = ["Made a Python script that ","automated the process of making","a CV like this."]


for project2 in project2:
    h = h - 20
    myCV.add(String(320, h, f"\u2022 {project1}", fontSize = 15, fillColor=colors.HexColor('#FFFFFF'),
    fontName= 'Helvetica-Bold'))

for d in project2d:
    h = h - 20
    myCV.add(String(335, h, d, fontSize = 15, fillColor=colors.HexColor('#FFFFFF'),
    fontName= 'Helvetica'))

h = h - 40

myCV.add(String(310, h, "Eductation", fontSize = 18, fillColor=colors.HexColor('#FFFFFF'),
 fontName= 'Helvetica-Bold'))


education = ["FOC student at Cairo University","CS50 programming course"]

for course in education:
    h = h - 20
    myCV.add(String(320, h, f"\u2022 {course}", fontSize = 15, fillColor=colors.HexColor('#FFFFFF'),
    fontName= 'Helvetica'))

h2 = 450

myCV.add(String(50, h2, "Adham Hisham", fontSize = 30, fillColor=colors.HexColor('#000000'),
 fontName= 'Helvetica-Bold'))

h2 = h2 - 60

myCV.add(String(30, h2, "Contacts", fontSize = 18, fillColor=colors.HexColor('#000000'),
 fontName= 'Helvetica-Bold'))



contacts = ["01153855959", "adhamhisham204@gmail.com", "cs-is-fun.tk"]

for contact in contacts:
    h2 = h2 - 20
    myCV.add(String(20, h2, f"\u2022 {contact}", fontSize = 15, fillColor=colors.HexColor('#000000'),
    fontName= 'Helvetica'))

h2 = h2 - 150
myCV.add(String(20, h2, "About me", fontSize = 25, fillColor=colors.HexColor('#000000'),
 fontName= 'Helvetica-Bold'))

h2 = h2 - 20

about = ["I am Adham Hisham, I am 19, and this CV was made ",
 "using my own python script instead of using MS word,",
 "I am self tought programmer, looking for a relevant Job",
 "and I am looking forward to expand my knowledge"]

for content in about:
    h2 = h2 - 20
    myCV.add(String(20, h2, content, fontSize = 18, fillColor=colors.HexColor('#000000'),
    fontName= 'Helvetica'))


renderPDF.drawToFile(myCV, 'myCV.pdf')
