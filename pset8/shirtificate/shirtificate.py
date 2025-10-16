
# want to make a pdf in portrait a4 format with a white background
from fpdf import FPDF

# get name
name = input("Name: ").strip()

# make the base of the pdf, specify portrait and a4
pdf = FPDF(orientation="portrait", unit="mm", format="a4")
pdf.add_page()
WIDTH = 190

# title
pdf.set_font('helvetica', size=50)
pdf.cell(w=WIDTH, text="CS50 Shirtficate", align="C")

# image and label
pdf.image("shirtificate.png", x=10, y=50, w=WIDTH)

# text
pdf.set_font('times', size=25)
pdf.set_text_color(r=255,g=255,b=255)
# y
pdf.set_y(120)
# putting name on shirt
pdf.cell(text=f"{name} took CS50", align="C", w=WIDTH)
# output the shirt
pdf.output("shirtificate.pdf")
