# 7. Sa se verifice, folosind o expresie regulata, daca un sir de caractere reprezinta un CNP valid.
#
# [S][AA][LL][ZZ][CJ][XXX][C]
#
# [S] - Cod sex, masculin/feminin, se aloca astfel:
# 1/2 - nascuti intre 1 ian 1900 si 31 dec 1999;
# 3/4 - nascuti intre 1 ian 1800 si 31 dec 1899;
# 5/6 - nascuti intre 1 ian 2000 si 31 dec 2099;
# 7/8 - pentru rezidenti;
# 9/9 - pentru persoanele cu cetatenie straina.
# [AA] - An nastere
# [LL] - Luna nastere
# [ZZ] - Zi nastere
# [CJ] - Cod judet
# [XXX] - Numar de ordine
# [C] - Cifra de control

import  re

def validate_cnp(cnp_string):
    # \d{3}(0[1-9]|1[0-2])([0-2][0-9]|3[0-1])([0-3][0-9]|4[0-1])\d{4})
    r = re.compile('[1-9](\d\d)(0[1-9]|1[0-2])([0-2][0-9]|3[0-1])([0-3][0-9]|4[0-1])(\d{3}\d)')

    if r.match(cnp_string):
        return True
    return False

if __name__=="__main__":
    print(validate_cnp('7950404220027'))