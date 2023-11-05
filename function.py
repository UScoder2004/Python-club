"""31/10/2023

Dasturlash asoslari

lesson: Nesting

Author: Sirotulla Umrzogaliyev
"""
def info(ism,familiya,t_yil,t_joy,email="",tel=None):
    info_d={
            "ism": ism,
            "familiya": familiya,
            "yil": 2023 - t_yil,
            "joy": t_joy,
            "email": email,
            "tel": tel
            }
    return info_d
 
print("mijozlar ro'yhati")
mijozlar = []
while True:
    ism = input("Ismi:")
    familiya = input("Familiyasi:")
    yil = int(input("Tug'ilgan yili':"))
    joy = input("tug'ilgan joyi':")
    email = input("Email:")
    tel = input("Telefon raqami:")
    mijozlar.append(info(ism,familiya,yil,joy,email,tel))
    javob = input("Do you want to add another names? (yes,no)")
    if javob != 'yes':
        break
print("mijozlar:")

for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['yil']} yoshda,telefoni: {mijoz['tel']}"
        )




