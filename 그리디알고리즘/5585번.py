'''타로는 자주 JOI잡화점에서 물건을 산다. JOI잡화점에는 잔돈으로 500엔, 100엔, 50엔, 10엔, 5엔, 1엔이 충분히 있고, 
언제나 거스름돈 개수가 가장 적게 잔돈을 준다. 타로가 JOI잡화점에서 물건을 사고 카운터에서 1000엔 지폐를 한장 냈을 때, 
받을 잔돈에 포함된 잔돈의 개수를 구하는 프로그램을 작성하시오.'''

def Calculator(n, num, result) :
    if n - num >= 0 :
        result += n // num
        n = n - (n // num * num)
        return n, result

    else:
        return n, result

n = 1000 - int(input())
result = 0

if n % 500 == 0 :
    print(n // 500)
    n == 0

else:

    n, result = Calculator(n, 500, result)

    n, result = Calculator(n, 100, result)

    n, result = Calculator(n, 50, result)

    n, result = Calculator(n, 10, result)

    n, result = Calculator(n, 5, result)

    n, result = Calculator(n, 1, result)

    print(result)












