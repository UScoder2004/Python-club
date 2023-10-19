"""19/12/2023

Dasturlash asoslari

lesson: Nesting

Author: Sirotulla Umrzogaliyev
"""

shoir1={'ism':'abu abdulloh muhammad ibn ismoil',
        'tyil':810,
        'shahar':'buxoro',
        'yashagan':60,
        'asarlar':["Al-jome' as -sahih","Al-adab al-mufrad",
                   "At-tarix al-kabir","At-tarix as-sag'ir"]}
shoir2={'ism':'abdulla qodoriy',
        'tyil':1894,
        'shahar':'toshkent',
        'yashagan':44,
        'asarlar':["O'tkan kunlar","Mehrobdan chayon","Obid ketmon"]}
shoir3={'ism':'erkin vohidov',
        'tyil':1936,
        'shahar':'farg\'ona',
        'yashagan':80,
        'asarlar':["Tong nafasi","Qo'shiqlarim sizga",
                   "O'zbegim","Qiziquvchan Matmusa"]}
shoir4={'ism':'alisher navoiy',
        'tyil':1441,
        'shahar':'xirot',
        'yashagan':60,
        'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub","Munojot"]}
shoirs=[shoir1,shoir2,shoir3,shoir4]
for shoir in shoirs:
    ism=shoir['ism']
    asarlar=shoir['asarlar']
    print(f"{ism} ning mashhur asarlari:")
    for asar in asarlar:
        print(f"{asar}")

