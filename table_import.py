import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('exactpointer-74a7f1e4a7e2.json', scope)
client = gspread.authorize(creds)

sheet = client.open("pointer_data")

############################################################ берем режим отчета
sh2 = sheet.worksheet("Main")
main_things = sh2.get_all_records()
mode = int(main_things[0]['mode'])

########################################################## берем первый лист для сбора всей инфы и зачищаем по режиму
sh1 = sheet.worksheet("Raw")
list_of_hashes = sh1.get_all_records()

i = 0
while i < len(list_of_hashes):
    if (mode == 1 and list_of_hashes[i]['short'] == 0) or (mode == 0 and list_of_hashes[i]['free'] == 0):
        del list_of_hashes[i]
        continue
    i += 1
########################################################## набираем список категорий
headers_list = []
headers_max_points_list = []
headers_min_points_list = []
headers_points_list = []

for i in range(len(list_of_hashes)):
    headers_list.append(list_of_hashes[i]['category'])
i = 0
while i < len(headers_list) - 1:
    if headers_list[i] == headers_list[i + 1]:
        del headers_list[i + 1]
    else:
        i += 1
############################################################ набираем список параметров, блок на что влияет
parameters_list = [[] for i in range(len(headers_list))]
parameters_influence_list = [[] for i in range(len(headers_list))]
parameters_description_list = [[] for i in range(len(headers_list))]
parameters_addinfo_list = [[] for i in range(len(headers_list))]
parameters_max_points_list = [[] for i in range(len(headers_list))]
parameters_min_points_list = [[] for i in range(len(headers_list))]
parameters_points_list = [[] for i in range(len(headers_list))]


def delete_repeats_1(inlist):
    for i in range(len(inlist)):
        j = 0
        while j < len(inlist[i]) - 1:
            if inlist[i][j] == inlist[i][j + 1]:
                del inlist[i][j + 1]
            else:
                j += 1


z = 0
for i in range(len(headers_list)):
    t = 0
    for j in range(len(list_of_hashes)):
        if list_of_hashes[j]['category'] == headers_list[i]:
            parameters_list[z].insert(t, list_of_hashes[j]['parameter'])
            parameters_influence_list[z].insert(t, list_of_hashes[j]['influence'])
            parameters_description_list[z].insert(t, list_of_hashes[j]['description'])
            parameters_addinfo_list[z].insert(t, list_of_hashes[j]['add_info'])
            t += 1
    z += 1


delete_repeats_1(parameters_list)
delete_repeats_1(parameters_influence_list)
delete_repeats_1(parameters_description_list)
delete_repeats_1(parameters_addinfo_list)

############################################################ набираем список подпараметров
subparameters_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_points_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_max_points_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_min_points_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_time_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_good_result_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_good_advice_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_bad_result_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_bad_task_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_extra_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]

subparameters_standart_mode_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_short_mode_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]
subparameters_free_mode_list = [[[] for j in range(len(parameters_list[i]))] for i in range(len(headers_list))]


z = 0
for i in range(len(headers_list)):
    t = 0
    for g in range(len(parameters_list[i])):
        f = 0
        for j in range(len(list_of_hashes)):
            if list_of_hashes[j]['category'] == headers_list[i] and list_of_hashes[j]['parameter'] == parameters_list[i][g]:
                subparameters_list[z][t].insert(f, list_of_hashes[j]['subparameter'])
                subparameters_points_list[z][t].insert(f, list_of_hashes[j]['points'])
                subparameters_max_points_list[z][t].insert(f, list_of_hashes[j]['max_points'])

                subparameters_min_points_list[z][t].insert(f, 0)

                subparameters_time_list[z][t].insert(f, list_of_hashes[j]['time'])
                subparameters_good_result_list[z][t].insert(f, list_of_hashes[j]['good_result'])
                subparameters_good_advice_list[z][t].insert(f, list_of_hashes[j]['good_advice'])
                subparameters_bad_result_list[z][t].insert(f, list_of_hashes[j]['bad_result'])
                subparameters_bad_task_list[z][t].insert(f, list_of_hashes[j]['bad_task'])
                subparameters_extra_list[z][t].insert(f, list_of_hashes[j]['extra'])

                subparameters_standart_mode_list[z][t].insert(f, list_of_hashes[j]['standart'])
                subparameters_short_mode_list[z][t].insert(f, list_of_hashes[j]['short'])
                subparameters_free_mode_list[z][t].insert(f, list_of_hashes[j]['free'])

                f += 1
        t += 1
    z += 1
############################################################ считаем пойнты параметров и хэдеров
def sum_point_2(inlist1, inlist2):
    for i in range(len(inlist1)):
        for j in range(len(inlist1[i])):
            temp_sum = 0
            for z in range(len(inlist1[i][j])):
                temp_sum += inlist1[i][j][z]
            inlist2[i].insert(z, temp_sum)


sum_point_2(subparameters_max_points_list, parameters_max_points_list)
sum_point_2(subparameters_min_points_list, parameters_min_points_list)
sum_point_2(subparameters_points_list, parameters_points_list)

def sum_point_1(inlist1, inlist2):
    for i in range(len(inlist1)):
        temp_sum = 0
        for j in range(len(inlist1[i])):
            temp_sum += inlist1[i][j]
        inlist2.insert(i, temp_sum)


sum_point_1(parameters_max_points_list, headers_max_points_list)
sum_point_1(parameters_min_points_list, headers_min_points_list)
sum_point_1(parameters_points_list, headers_points_list)

total_max = sum(i for i in headers_max_points_list)
total_min = sum(i for i in headers_min_points_list)
total = sum(i for i in headers_points_list)
total_percent = str(round((total / total_max)*100, 2)) + ' / 100'


def time_check(t):
    if t < 60:
        if t % 10 == 1:
            tmp_time = str(t) + ' минута'
        elif t % 10 in [2, 3, 4]:
            tmp_time = str(t) + ' минуты'
        elif t % 10 in [5, 6, 7, 8, 9, 0]:
            tmp_time = str(t) + ' минут'
        else:
            tmp_time = 'сложно сказать'
    elif (t >= 60) and (t < 1440):
        if t // 60 % 10 == 1:
            tmp_time = str(t // 60) + ' час'
        elif t // 60 % 10 in [2, 3, 4]:
            tmp_time = str(t // 60) + ' часа'
        elif t // 60 % 10 in [5, 6, 7, 8, 9, 0]:
            tmp_time = str(t // 60) + ' часов'
        else:
            tmp_time = 'сложно сказать'
    elif (t >= 1440) and (t < 10080):
        if t // 1440 % 10 == 1:
            tmp_time = str(t // 1440) + ' день'
        elif t // 1440 % 10 in [2, 3, 4]:
            tmp_time = str(t // 1440) + ' дня'
        elif t // 1440 % 10 in [5, 6, 7, 8, 9, 0]:
            tmp_time = str(t // 1440) + ' дней'
        else:
            tmp_time = 'сложно сказать'
    elif (t >= 10080) and (t < 43800):
        if t // 10080 % 10 == 1:
            tmp_time = str(t // 10080) + ' неделя'
        elif t // 10080 % 10 in [2, 3, 4]:
            tmp_time = str(t // 10080) + ' недели'
        elif t // 10080 % 10 in [5, 6, 7, 8, 9, 0]:
            tmp_time = str(t // 10080) + ' недель'
        else:
            tmp_time = 'сложно сказать'
    elif t >= 43800:
        if t // 43800 % 10 == 1:
            tmp_time = str(t // 43800) + ' месяц'
        elif t // 43800 % 10 in [2, 3, 4]:
            tmp_time = str(t // 43800) + ' месяца'
        elif t // 43800 % 10 in [5, 6, 7, 8, 9, 0]:
            tmp_time = str(t // 43800) + ' месяцев'
        else:
            tmp_time = 'сложно сказать'
    else:
        tmp_time = 'сложно сказать'
    return(tmp_time)


total_time = 0
for i in range(len(subparameters_time_list)):
    for j in range(len(subparameters_time_list[i])):
        for z in range(len(subparameters_time_list[i][j])):
            total_time += subparameters_time_list[i][j][z]

final_time = time_check(total_time)

############################################################ меняем лист, берем общую инфу
sh2 = sheet.worksheet("Main")
main_things = sh2.get_all_records()

changes_count = 0
for i in range(len(subparameters_points_list)):
    for j in range(len(subparameters_points_list[i])):
        for z in range(len(subparameters_points_list[i][j])):
            if subparameters_max_points_list[i][j][z] == 0:
                temp_border = abs(subparameters_min_points_list[i][j][z])
                if subparameters_points_list[i][j][z] / temp_border <= 0.2:
                    changes_count += 1
            else:
                temp_border = subparameters_max_points_list[i][j][z]
                if subparameters_points_list[i][j][z] / temp_border <= 0.8:
                    changes_count += 1
main_things[0]['changes_count'] = changes_count
main_things[0]['final_time'] = final_time
main_things[0]['total_percent'] = total_percent
common = []
for key, value in main_things[0].items():
    common.append(str(value))
#print(common)
############################################################ методы вывода хэдеров


def main_things(i):
    return common[i]


def headers_length():
    return len(headers_list)


def headers(i):
    return headers_list[i]


def headers_points(i):
    return headers_points_list[i]


def headers_maxpoints(i):
    return headers_max_points_list[i]


def headers_minpoints(i):
    return headers_min_points_list[i]


############################################################ методы вывода параметров


def parameters(i):
    return parameters_list[i]


def parameters_points(i):
    return parameters_points_list[i]


def parameters_maxpoints(i):
    return parameters_max_points_list[i]


def parameters_minpoints(i):
    return parameters_min_points_list[i]


def parameters_influence(i):
    return parameters_influence_list[i]


def parameters_description(i):
    return parameters_description_list[i]


def parameters_addinfo(i):
    return parameters_addinfo_list[i]


############################################################ методы вывода субпараметров

def subparameters(i, j):
    return subparameters_list[i][j]


def subparameters_points(i, j):
    return subparameters_points_list[i][j]


def subparameters_maxpoints(i, j):
    return subparameters_max_points_list[i][j]


def subparameters_minpoints(i, j):
    return subparameters_min_points_list[i][j]


def subparameters_time(i, j):
    return subparameters_time_list[i][j]

def subparameters_goodresult(i, j):
    return subparameters_good_result_list[i][j]


def subparameters_goodadvice(i, j):
    return subparameters_good_advice_list[i][j]


def subparameters_badresult(i, j):
    return subparameters_bad_result_list[i][j]


def subparameters_badtask(i, j):
    return subparameters_bad_task_list[i][j]


def subparameters_extra(i, j):
    return subparameters_extra_list[i][j]


def subparameters_standart_mode(i, j):
    return subparameters_standart_mode_list[i][j]


def subparameters_short_mode(i, j):
    return subparameters_short_mode_list[i][j]


def subparameters_free_mode(i, j):
    return subparameters_free_mode_list[i][j]
