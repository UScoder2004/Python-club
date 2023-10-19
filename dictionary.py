"""
19.10.2023
Author:Sirotullla Umrzogaliyev
"""


shoir1={'ism':'abu abdulloh muhammad ibn ismoil',
        'tyil':810,
        'shahar':'buxoro',
        'yashagan':60}
shoir2={'ism':'abdulla qodoriy',
        'tyil':1894,
        'shahar':'toshkent',
        'yashagan':44}
shoir3={'ism':'erkin vohidov',
        'tyil':1936,
        'shahar':'farg\'ona',
        'yashagan':80}
shoir4={'ism':'alisher navoiy',
        'tyil':1441,
        'shahar':'xirot',
        'yashagan':60}

shoirs=[shoir1,shoir2,shoir3,shoir4]
for shoir in shoirs:
    print(f"\n{shoir['ism'].title()} {shoir['tyil']}-yilda "
          f"{shoir['shahar'].title()}da tavallud topgan."
          f"{shoir['yashagan']} yil umir ko'rgan.")
    
