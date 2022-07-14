'''
데이터가 정규성을 띄는지 확인하는 코드
'''

import math


def Anderson_pvalue(Value:float):
    AD = Value*(1 + (.75/50) + 2.25/(50**2))
#     print("Adjusted A^2 = ", AD)
    if AD >= .6:
        p = math.exp(1.2937 - 5.709*AD - .0186*(AD**2))
    elif AD >=.34:
        p = math.exp(.9177 - 4.279*AD - 1.38*(AD**2))
    elif AD >.2:
        p = 1 - math.exp(-8.318 + 42.796*AD - 59.938*(AD**2))
    else:
        p = 1 - math.exp(-13.436 + 101.14*AD - 223.73*(AD**2))
#     print("p = ", p) # 해당 통계치를 P-value로 환산 한 코드.
    return p