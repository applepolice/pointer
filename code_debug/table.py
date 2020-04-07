import table_work
from fpdf import FPDF

pdf = FPDF(format='letter', unit='in')


def table_draw(x, y):

    epw = pdf.w - 2 * pdf.l_margin

    data_default = table_work.table_work()

    pdf.set_xy(x, y)

    pdf.add_font('Exo 2 Bold', '', r"C:\Users\yacub\PycharmProjects\pointer\Exo 2 Bold.ttf", uni=True)
    pdf.add_font('Exo 2', '', r"C:\Users\yacub\PycharmProjects\pointer\Exo 2.ttf", uni=True)
    pdf.set_font('Exo 2', '', 20)
    pdf.cell(epw, 20.0, 'With more padding', align='C')
    pdf.set_font('Exo 2', '', 12.5)
    pdf.ln(0.5)
    th = pdf.font_size



    for row in data_default:
        i = 0
        if row == data_default[0]:
            pdf.set_font('Exo 2 Bold', '', 12.5)
        else:
            pdf.set_font('Exo 2', '', 12.5)
        for datum in row:
            col_width = epw / 4
            if i == 0:
                col_width += 0.6
                pdf.cell(col_width, 2 * th, str(datum), border=0, ln=0)
            elif i == 2:
                col_width += 0.3
                pdf.cell(col_width, 2 * th, str(datum), border=0, ln=0)
            elif (i == 1) or (i == 3):
                col_width -= 0.5
                pdf.cell(col_width, 2 * th, str(datum), border=0, ln=0, align='C')
            i += 1
        pdf.ln(2 * th)
        #pdf.ln(th)
        #pdf.set_draw_color(209, 212, 221)
        #pdf.line(x, y + 2 * th, 210-x, y + 2 * th)
        #pdf.ln(th)
    print(data_default)


#pdf.add_page()
table_draw(20, 20)
pdf.output('table-using-cell-borders.pdf', 'F')