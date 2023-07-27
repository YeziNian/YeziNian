from math import log
from functools import reduce
lie = []
namespace = ["年龄", "收入水平", "固定收入", "银行VIP", "提供贷款"]
with open("data.txt", "r") as fp:
    Data = fp.readline().rstrip()
    while Data:
        dic = dict.fromkeys(namespace)
        Data_spilt = Data.split()
        for m, n in zip(dic.keys(), Data_spilt):
            dic[m] = eval(n)
        lie.append(dic)
        Data = fp.readline().rstrip()
Yuzhi = 40
def get1(m, n):
    m[list(n.values())[1]] = m.get(list(n.values())[1], 0) + 1
    return m
def Shang(data):

    contrast = 6
    lenth = len(data)

    #信息熵
    Fi_room_len = len(list(filter(lambda c: True if c[namespace[4]] == 1 else False, data))) / lenth
    Fi_data = -(Fi_room_len*log(2, Fi_room_len) + (1-Fi_room_len)*log(2, 1-Fi_room_len))

    # age
    age_room = list(filter(lambda c: True if c[namespace[0]] <= Yuzhi else False, data))
    age_step = 0
    for k in age_room:
        if list(k.values())[4] == 1:
            age_step += 1
    age_Tlen = age_step / len(age_room)
    age_Flen = (contrast-age_step) / (lenth-len(age_room))
    age_T = -(age_Tlen*log(2, age_Tlen) + (1-age_Tlen)*log(2, 1-age_Tlen))
    age_F = -(age_Flen*log(2, age_Flen) + (1-age_Flen)*log(2, 1-age_Flen))
    G_age = Fi_data - (len(age_room) / lenth * age_T + (1 - len(age_room)) / lenth * age_F)

    # show
    Shou_room = reduce(get1, data, {})
    a, b, c= Shou_room.values()
    A, B, C = 0, 0, 0
    for m in data:
        if m[namespace[1]] == 1 and m[namespace[4]] == 1:
            A += 1
        elif m[namespace[1]] == 0 and m[namespace[4]] == 1:
            B += 1
        elif m[namespace[1]] == -1 and m[namespace[4]] == 1:
            C += 1
    A_data = -(A / a * log(2, A / a) + (1 - A / a) * log(2, (1 - A / a)))
    B_data = -(B / b * log(2, B / b) + (1 - B / b) * log(2, (1 - B / b)))
    C_data = -(C / c * log(2, C / c) + (1 - C / c) * log(2, (1 - C / c)))
    G_show = Fi_data - (a / lenth * A_data + b / lenth * B_data + c / lenth * C_data)

    #Gu
    Gu_room = list(filter(lambda c: True if c[namespace[2]] == 1 else False, data))
    Gu_step = 0
    for k in Gu_room:
        if list(k.values())[4] == 1:
            Gu_step += 1
    Gu_Tlen = Gu_step / len(Gu_room)
    Gu_Flen = (contrast - Gu_step) / (lenth - len(Gu_room))
    Gu_T = -(Gu_Tlen * log(2, Gu_Tlen) + (1 - Gu_Tlen) * log(2, 1 - Gu_Tlen))
    Gu_F = -(Gu_Flen * log(2, Gu_Flen) + (1 - Gu_Flen) * log(2, 1 - Gu_Flen))
    G_Gu = Fi_data - (len(Gu_room) / lenth * Gu_T + (1 - len(Gu_room)) / lenth * Gu_F)

    #Vip
    Vip_room = list(filter(lambda c: True if c[namespace[3]] == 1 else False, data))
    Vip_step = 0
    for k in Vip_room:
        if list(k.values())[4] == 1:
            Vip_step += 1
    Vip_Tlen = Vip_step / len(Vip_room)
    Vip_Flen = (contrast-Vip_step) / (lenth-len(Vip_room))
    Vip_T = -(Vip_Tlen*log(2, Vip_Tlen) + (1-Vip_Tlen)*log(2, 1-Vip_Tlen))
    Vip_F = -(Vip_Flen*log(2, Vip_Flen) + (1-Vip_Flen)*log(2, 1-Vip_Flen))
    G_Vip = Fi_data - (len(Vip_room) / lenth * Vip_T + (1 - len(Vip_room)) / lenth * Vip_F)

    return (Fi_data, G_age, G_show, G_Gu, G_Vip)

di = Shang(lie)
print("经验熵为:", di[0])
i = 0
for k in di[1:]:
    print(f"{namespace[i]}增益为:{k}")
    i += 1

