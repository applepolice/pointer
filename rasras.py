from fpdf import FPDF
import datetime
import table_work
import globals
import table_import

now = datetime.datetime.now()

headers_links_list = []
contentpages = []
contentoffset = []
parameters_links_list = [[] for i in range(table_import.headers_length())]
detailedpages = [[] for i in range(table_import.headers_length())]


class PDF(FPDF):
    def header(self):
        self.set_fill_color(27, 38, 83)
        self.rect(0, 0, 210, 40, 'F')

        tmp_link = self.add_link()
        self.image(globals.logo, x=10, y=8, w=80, link=tmp_link)
        self.set_link(tmp_link, 0, 1)

        self.add_font('Exo 2', '', globals.exo2regular_path, uni=True)
        self.set_font('Exo 2', '', 12.5)

        self.set_text_color(255, 255, 255)
        self.set_xy(100, 14)
        self.cell(100, 10, txt="Маркетинговый искуственный интеллект", ln=1, align="C")
        self.ln(30)
        self.image(globals.watermark, x=(self.w-160)/2, y=100, w=160)

    def footer(self):
        self.set_y(-15)
        self.add_font('Exo 2', '', globals.exo2regular_path, uni=True)
        self.set_font('Exo 2', '', 10)
        self.cell(0, 10, str(self.page_no()) + '/{nb}', 0, 0, 'R')


def start_x(m):
    string_length = 0
    for i in range(len(m)):
        string_length += pdf.get_string_width(m[i])
    start_x_pos = (pdf.w - string_length) / 2
    return(start_x_pos)


def title_page(y):
    pdf.add_font('Exo 2', '', globals.exo2regular_path, uni=True)
    pdf.add_font('Exo 2 Bold', '', globals.exo2bold_path, uni=True)

    pdf.set_font('Exo 2', '', 20)
    temp1 = "План работ по сайту "
    tempx = start_x([temp1, table_import.main_things(0)])
    str_lng = pdf.get_string_width(temp1) + pdf.get_string_width(table_import.main_things(0))
    pdf.set_xy(tempx, y)
    pdf.cell(str_lng, 10, txt="План работ по сайту " + table_import.main_things(0), ln=1, align="L")       # сюда подставить адрес сайта

    pdf.set_font('Exo 2', '', 10)
    temp1 = "Дата составления: {}.{}.{}".format(now.day, now.month, now.year)
    tempx = start_x([temp1])
    str_lng = pdf.get_string_width(temp1)
    pdf.set_x(tempx)
    pdf.cell(str_lng, 10, txt=temp1, ln=1, align="L")

    pdf.ln(pdf.font_size*2)

    pdf.set_font('Exo 2', '', 15)
    temp1 = "Текущее состояние сайта -"
    temp2 = table_import.main_things(7)
    tempx = start_x([temp1, temp2])
    pdf.set_x(tempx)
    pdf.cell(pdf.get_string_width(temp1), 10, txt=temp1, ln=0, align="L")
    pdf.set_font('Exo 2 Bold', '', 15)
    pdf.set_x(tempx + pdf.get_string_width(temp1))
    pdf.cell(pdf.get_string_width(temp2), 10, txt=temp2, ln=1, align="L")                                       # сюда подставить оценку сайта

    pdf.set_font('Exo 2', '', 15)
    temp1 = "Текущая посещаемость - "
    temp2 = table_import.main_things(1)
    temp3 = "  посещений в месяц"
    tempx = start_x([temp1, temp2, temp3])
    pdf.set_x(tempx)
    pdf.cell(pdf.get_string_width(temp1), pdf.font_size, txt=temp1, ln=0, align="L")
    pdf.set_x(tempx + pdf.get_string_width(temp1))
    pdf.set_font('Exo 2 Bold', '', 15)
    pdf.cell(pdf.get_string_width(temp2), pdf.font_size, txt=temp2, ln=0, align="L")                                    # сюда подставить посещаемость сайта
    pdf.set_font('Exo 2', '', 15)
    pdf.set_x(tempx + pdf.get_string_width(temp1) + pdf.get_string_width(temp2))
    pdf.cell(pdf.get_string_width(temp3), pdf.font_size, txt=temp3, ln=1, align="L")

    pdf.set_draw_color(209, 212, 221)
    pdf.line(5, pdf.get_y()+pdf.font_size*2, 205, pdf.get_y()+pdf.font_size*2)

    temp1 = "Мы считаем, что необходимо внести "
    temp2 = table_import.main_things(5)
    if int(temp2) % 10 == 1:
        temp3 = '  изменение'
    elif int(temp2) % 10 in (2, 3, 4):
        temp3 = '  изменения'
    elif int(temp2) % 10 in (6, 7, 8, 9, 0):
        temp3 = '  изменений'
    tempx = start_x([temp1, temp2, temp3])
    pdf.set_xy(tempx, y + 60)
    pdf.set_font('Exo 2', '', 15)
    pdf.cell(pdf.get_string_width(temp1), 10, txt=temp1, ln=0, align="L")
    pdf.set_x(tempx + pdf.get_string_width(temp1))
    pdf.set_font('Exo 2 Bold', '', 15)
    pdf.cell(pdf.get_string_width(temp2), 10, txt=temp2, ln=0, align="L")                                   # сюда подставить количество изменений
    pdf.set_font('Exo 2', '', 15)
    pdf.set_x(tempx + pdf.get_string_width(temp1) + pdf.get_string_width(temp2))
    pdf.cell(pdf.get_string_width(temp3), 10, txt=temp3, ln=1, align="L")

    temp1 = "Примерное время работ: "
    temp2 = table_import.main_things(6)
    temp3 = '  рабочего времени'
    tempx = start_x([temp1, temp2, temp3])
    pdf.set_xy(tempx, 115)
    pdf.set_font('Exo 2', '', 15)
    pdf.cell(30, 10, txt=temp1, ln=0, align="L")
    pdf.set_x(tempx + pdf.get_string_width(temp1))
    pdf.set_font('Exo 2 Bold', '', 15)
    pdf.cell(10, 10, txt=temp2, ln=0, align="L")
    pdf.set_font('Exo 2', '', 15)
    pdf.set_x(tempx + pdf.get_string_width(temp1) + pdf.get_string_width(temp2))
    pdf.cell(30, 10, txt=temp3, ln=1, align="L")

    temp1 = "Прогнозируемый результат - повышение посещаемости на "
    temp2 = table_import.main_things(2)+'%'
    temp3 = ' за '
    temp4 = table_import.time_check(int(table_import.main_things(3)))
    tempx = start_x([temp1, temp2, temp3, temp4])
    pdf.set_xy(tempx, 125)
    pdf.set_font('Exo 2', '', 15)
    pdf.cell(pdf.get_string_width(temp1), 10, txt=temp1, ln=0, align="L")
    pdf.set_x(tempx + pdf.get_string_width(temp1))
    pdf.set_font('Exo 2 Bold', '', 15)
    pdf.cell(pdf.get_string_width(temp2), 10, txt=temp2, ln=0, align="L")
    pdf.set_font('Exo 2', '', 15)
    pdf.set_x(tempx + pdf.get_string_width(temp1) + pdf.get_string_width(temp2))
    pdf.cell(pdf.get_string_width(temp3), 10, txt=temp3, ln=0, align="L")
    pdf.set_x(tempx + pdf.get_string_width(temp1) + pdf.get_string_width(temp2) + pdf.get_string_width(temp3))
    pdf.set_font('Exo 2 Bold', '', 15)
    pdf.cell(pdf.get_string_width(temp4), 10, txt=temp4, ln=0, align="L")                        # сюда подставить срок


def title_table_draw(x, y):

    epw = pdf.w - 2 * pdf.l_margin

    data_default = table_work.table_work()

    pdf.set_xy(x, y)

    pdf.add_font('Exo 2 Bold', '', globals.exo2bold_path, uni=True)
    pdf.add_font('Exo 2', '', globals.exo2regular_path, uni=True)
    pdf.set_font('Exo 2', '', 12.5)
    pdf.ln(0.5)
    th = pdf.font_size

    j = 1
    for row in data_default:
        i = 0
        if row == data_default[0]:
            pdf.set_font('Exo 2 Bold', '', 12.5)
        else:
            pdf.set_font('Exo 2', '', 12.5)
        for datum in row:
            col_width = epw / 4
            if i == 0:
                col_width += 20
                pdf.cell(col_width, 2 * th, str(datum), border=0, ln=0)
            elif i == 1:
                col_width -= 23
                pdf.cell(col_width, 2 * th, str(datum), border=0, ln=0)
            elif i == 2:
                col_width += 15
                pdf.cell(col_width, 2 * th, str(datum), border=0, ln=0)
            elif i == 3:
                col_width -= 15
                pdf.cell(col_width, 2 * th, str(datum), border=0, ln=0)
            i += 1
        pdf.ln(th)
        pdf.set_draw_color(209, 212, 221)
        pdf.line(x-10, y + 2 * th * j, 210-x+10, y + 2 * th * j)
        pdf.ln(th)
        j += 1


def chart(x, y):
    pdf.set_font('Exo 2', '', 12)
    pdf.set_draw_color(209, 212, 221)
    pdf.line(x-10, y, 210-x+10, y)
    pdf.line(x - 10, y, x - 10, y - 10 * pdf.font_size)

    pdf.line(x-12, y - 10 * pdf.font_size, x-10, y - 10 * pdf.font_size)
    pdf.line(x - 12, y - 5 * pdf.font_size, x - 10, y - 5 * pdf.font_size)

    pdf.set_xy(x-18, y - 11 * pdf.font_size)
    pdf.cell(3, pdf.font_size, '100')
    pdf.set_xy(x - 16, y - 6 * pdf.font_size)
    pdf.cell(3, pdf.font_size, '50')

    pdf.set_xy(x-10, y + pdf.font_size)
    legend_width = (pdf.w - x) / 6 + 2
    tempx = pdf.get_x() + 3
    for i in range(table_import.headers_length()):
        temp = table_import.headers(i)

        if temp.find(' ') != -1:
            temp = temp[:temp.find(' ')] + '\n' + temp[temp.find(' ')+1:]

        if pdf.get_string_width(temp) < legend_width:
            tempx -= 5
            str_lng = pdf.get_string_width(temp) + 5
            offset = (legend_width - str_lng)/2
        else:
            str_lng = legend_width
            offset = 0
        pdf.set_xy(tempx, y + pdf.font_size)
        pdf.multi_cell(str_lng, pdf.font_size, temp)

        temp_points = table_import.headers_points(i) / table_import.headers_maxpoints(i)
        if temp_points <= 0.2:
            pdf.set_fill_color(235, 87, 87)
        elif (temp_points > 0.2) and (temp_points <= 0.5):
            pdf.set_fill_color(242, 153, 74)
        elif (temp_points > 0.5) and (temp_points <= 0.8):
            pdf.set_fill_color(242, 201, 76)
        elif temp_points > 0.8:
            pdf.set_fill_color(39, 174, 96)

        pdf.rect(tempx + 1, y - temp_points * 10 * pdf.font_size, 15, temp_points * 10 * pdf.font_size, 'F')

        tempx = tempx + str_lng + offset


def content_list():
    pdf.add_font('Exo 2', '', globals.exo2regular_path, uni=True)
    pdf.add_font('Exo 2 Bold', '', globals.exo2bold_path, uni=True)

    pdf.set_y(45)


    for i in range(table_import.headers_length()):
        pdf.set_font('Exo 2', '', 20)
        pdf.set_x(10)

        if pdf.get_y() + 0.1 + globals.h2_icon_size * 2 + pdf.font_size * 4 > pdf.h - pdf.t_margin:
            pdf.cell(90, pdf.font_size * 4, ln=1)
            pdf.set_y(45)
        else:
            if i != 0:
                pdf.ln(pdf.font_size / 2)

        contentpages.append(pdf.page_no())
        contentoffset.append(pdf.get_y())
        pdf.cell(90, pdf.font_size, table_import.headers(i), ln=0, align="L")

        pdf.cell(80, pdf.font_size, str(table_import.headers_points(i)) + '/' + str(table_import.headers_maxpoints(i)), ln=1, align="R")
        pdf.ln(pdf.font_size/2)
        for j in range(len(table_import.parameters(i))):

            pdf.set_font('Exo 2', '', 15)
            if j != 0:
                pdf.ln(pdf.font_size / 2)
            pdf.set_x(13)
            if table_import.parameters_maxpoints(i)[j] == 0:
                temp_point = table_import.parameters_points(i)[j] / abs(table_import.parameters_minpoints(i)[j])
            else:
                temp_point = table_import.parameters_points(i)[j] / table_import.parameters_maxpoints(i)[j]
            if temp_point >= 0.8:
                pdf.image(globals.icon_good, pdf.get_x(), pdf.get_y() + 0.1, w=globals.h2_icon_size)
            elif (temp_point >= 0.4) and (temp_point < 0.8):
                pdf.image(globals.icon_avg, pdf.get_x(), pdf.get_y() + 0.1, w=globals.h2_icon_size)
            elif temp_point < 0.4:
                pdf.image(globals.icon_bad, pdf.get_x(), pdf.get_y() + 0.1, w=globals.h2_icon_size)
            parameters_links_list[i].insert(j, pdf.add_link())
            pdf.set_x(20)
            pdf.cell(90, pdf.font_size, table_import.parameters(i)[j], ln=0, align="L", link=parameters_links_list[i][j])
            if table_import.parameters_maxpoints(i)[j] == 0:
                pdf.cell(90, pdf.font_size,
                         str(table_import.parameters_points(i)[j]) + '/' + str(table_import.parameters_minpoints(i)[j]),
                         ln=1, align="R")
            else:
                pdf.cell(90, pdf.font_size, str(table_import.parameters_points(i)[j]) + '/' + str(table_import.parameters_maxpoints(i)[j]), ln=1, align="R")
            

            if pdf.get_y() + 0.1 + globals.h2_icon_size * 2 + pdf.font_size * 1.5 > pdf.h - pdf.t_margin:
                pdf.cell(90, pdf.font_size * 4, ln=1)
                pdf.set_y(45)
            else:
                pdf.ln(pdf.font_size / 2)



def detailed_view ():
    pdf.add_font('Exo 2', '', globals.exo2regular_path, uni=True)
    pdf.add_font('Exo 2 Bold', '', globals.exo2bold_path, uni=True)
    pdf.add_font('Exo 2 Medium', '', globals.exo2medium_path, uni=True)
    pdf.add_font('Exo 2 Thin', '', globals.exo2thin_path, uni=True)
    pdf.add_font('Exo 2 Light', '', globals.exo2thin_path, uni=True)
    multicell_width = pdf.w - 4 * pdf.l_margin - pdf.get_x()

    for i in range(table_import.headers_length()):
        headers_links_list.append(pdf.add_link())
        for j in range(len(table_import.parameters(i))):
            detailedpages[i].insert(j, pdf.page_no())
            pdf.set_y(45)
            pdf.set_font('Exo 2', '', 20)
            pdf.set_x(10)

            pdf.cell(90, pdf.font_size, str(i+1) + '. ' + table_import.headers(i), ln=1, align="L", link=headers_links_list[i])

            pdf.ln(pdf.font_size)

            pdf.set_font('Exo 2', '', 15)
            pdf.set_x(17)
            pdf.cell(90, pdf.font_size, str(i+1) + '.' + str(j+1) + '. ' + table_import.parameters(i)[j], ln=0, align="L")
            if table_import.parameters_maxpoints(i)[j] == 0:
                pdf.cell(95, pdf.font_size,
                         str(table_import.parameters_points(i)[j]) + '/' + str(table_import.parameters_minpoints(i)[j]),
                         ln=1, align="R")
            else:
                pdf.cell(95, pdf.font_size,
                         str(table_import.parameters_points(i)[j]) + '/' + str(table_import.parameters_maxpoints(i)[j]),
                         ln=1, align="R")

            pdf.ln(pdf.font_size*1.5)

            pdf.set_x(25)
            pdf.set_font('Exo 2 Light', '', 12.5)
            pdf.cell(90, pdf.font_size, 'На что влияет этот параметр', ln=1, align="L")
            pdf.ln(pdf.font_size / 2)
            pdf.set_x(25)
            pdf.multi_cell(multicell_width, pdf.font_size*1.2, table_import.parameters_influence(i)[j])

            pdf.ln(pdf.font_size*1.5)

            for z in range(len(table_import.subparameters(i, j))):

                pdf.set_font('Exo 2 Medium', '', 12.5)
                if pdf.get_y() + globals.h3_icon_size * 2 + pdf.font_size * 4 > pdf.h - pdf.t_margin:
                    pdf.cell(90, pdf.font_size * 8, ln=1)
                    pdf.set_y(45)
                else:
                    pdf.ln(pdf.font_size / 2)

                if table_import.subparameters_maxpoints(i, j)[z] == 0:
                    temp_subpoints = table_import.subparameters_points(i, j)[z] / abs(table_import.subparameters_minpoints(i, j)[z])
                else:
                    temp_subpoints = table_import.subparameters_points(i, j)[z] / table_import.subparameters_maxpoints(i, j)[z]

                pdf.set_x(10)
                if table_import.subparameters_extra(i, j)[z] == 1:
                    pdf.image(globals.icon_extra, pdf.get_x(), pdf.get_y() - 0.3, w=globals.h2_icon_size)

                pdf.set_font('Exo 2 Medium', '', 12.5)
                pdf.set_x(17)
                if temp_subpoints >= 0.8:
                    pdf.image(globals.icon_good, pdf.get_x(), pdf.get_y()-0.3,  w=globals.h2_icon_size)
                elif (temp_subpoints >= 0.4) and (temp_subpoints < 0.8):
                    pdf.image(globals.icon_avg, pdf.get_x(), pdf.get_y()-0.3, w=globals.h2_icon_size)
                elif temp_subpoints < 0.4:
                    pdf.image(globals.icon_bad, pdf.get_x(), pdf.get_y()-0.3, w=globals.h2_icon_size)
                pdf.set_x(25)
                pdf.cell(90, pdf.font_size, table_import.subparameters(i, j)[z], ln=0, align="L")

                pdf.set_x(145)
                pdf.image(globals.icon_points, pdf.get_x(), pdf.get_y() +0.3, w=globals.h3_icon_size)
                pdf.set_x(150)
                if table_import.subparameters_maxpoints(i, j)[z] == 0:
                    pdf.cell(20, pdf.font_size, str(table_import.subparameters_points(i, j)[z]) + '/' + str(table_import.subparameters_minpoints(i, j)[z]),
                             ln=0)
                else:
                    pdf.cell(20, pdf.font_size, str(table_import.subparameters_points(i, j)[z]) + '/' + str(table_import.subparameters_maxpoints(i, j)[z]),
                             ln=0)
                
                # pdf.set_x(162)
                # pdf.image(globals.icon_importance, pdf.get_x(), pdf.get_y() +0.3, w=globals.h3_icon_size)
                # pdf.set_x(167)
                # pdf.cell(5, pdf.font_size, str(table_import.params_importance_back(i, j)[z]), ln=0)
                pdf.set_x(178)
                pdf.image(globals.icon_time, pdf.get_x(), pdf.get_y() +0.3, w=globals.h3_icon_size)
                pdf.set_x(183)

                pdf.cell(60, pdf.font_size, table_import.time_check(table_import.subparameters_time(i, j)[z]), ln=1)
                pdf.ln(pdf.font_size/2)

                if temp_subpoints >= 0.8:
                    tmp_text_top = table_import.subparameters_goodresult(i, j)[z]
                    tmp_text_bot = table_import.subparameters_goodadvice(i, j)[z]
                elif temp_subpoints < 0.8:
                    tmp_text_top = table_import.subparameters_badresult(i, j)[z]
                    tmp_text_bot = table_import.subparameters_badtask(i, j)[z]
                else:
                    tmp_text_top = 'Твоя любимая свинка'
                    tmp_text_bot = 'Матвей Петрович'
                pdf.set_x(25)
                pdf.set_font('Exo 2', '', 12)
                pdf.multi_cell(multicell_width, pdf.font_size*1.2, tmp_text_top)
                #pdf.ln(pdf.font_size * 1.2)
                pdf.set_x(25)
                pdf.multi_cell(multicell_width, pdf.font_size * 1.2, tmp_text_bot)
                pdf.ln(pdf.font_size*2)
            pdf.set_x(25)
            pdf.set_font('Exo 2 Medium', '', 12.5)
            pdf.cell(90, pdf.font_size, 'Описание параметра', ln=1, align="L")
            pdf.ln(pdf.font_size / 2)
            pdf.set_x(25)
            pdf.set_font('Exo 2', '', 12.5)
            pdf.multi_cell(multicell_width, pdf.font_size * 1.2, table_import.parameters_description(i)[j])
            pdf.ln(pdf.font_size * 2)
            pdf.add_page()


def define_links():
    for i in range(table_import.headers_length()):
        for j in range(len(table_import.parameters(i))):
            pdf.set_link(parameters_links_list[i][j], 0, detailedpages[i][j])
        pdf.set_link(headers_links_list[i], contentoffset[i], contentpages[i])




pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
title_page(45)
title_table_draw(20, 140)
chart(20, 255)
pdf.add_page()
content_list()
pdf.add_page()
detailed_view()
define_links()

pdf.output('simple_demo.pdf')

