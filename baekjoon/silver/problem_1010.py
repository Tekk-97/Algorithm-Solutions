#import math

def combination(n, r):
    if r == 0 or n == r:
        return 1
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

# 테스트 케이스 수 입력
T = int(input())



for _ in range(T):
    N, M = map(int, input().split())
    # M개 중에서 N개를 선택하는 조합 계산
#    result = math.comb(M, N)
    result=combination(M,N)

    print(result)
