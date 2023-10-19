"""19/12/2023

Dasturlash asoslari

lesson: Nesting

Author: Sirotulla Umrzogaliyev
"""

davlatlar={
    "o'zbekiston":{"poytaxt":"toshkent",
                   "hudud":448978,
                   "aholi":33000000,
                   "pul":"so'm"},
    "rossiya":{"poytaxt":"moskva",
                "hudud":17098246,
                "aholi":144000000,
                "pul":"rubl"},
    "aqsh":{"poytaxt":"vashington",
                   "hudud":9631418,
                   "aholi":327000000,
                   "pul":"dollar"},
    "malayziya":{"poytaxt":"kuala-lumpur",
                   "hudud":329750,
                   "aholi":25000000,
                   "pul":"rinngit"}}

davlat=input("Davlat nomini kiriting: ").lower()
if davlat in davlatlar:
    info=davlatlar[davlat]

    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi:  {info['hudud']} kv.km"
          f"\nAholisi: {info['aholi']}"
          f"\nPul birligi: {info['pul']}")
else:
    print("Bizda bu davlat haqida ma'limot mavjud emas")
        

