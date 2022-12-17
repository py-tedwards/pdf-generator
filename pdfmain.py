from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format='A4')


df = pandas.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1, border="B")
    num_pages = int(row['Pages']) - 1
    while num_pages > 0:
        pdf.add_page()
        num_pages = num_pages-1

pdf.output("output.pdf")