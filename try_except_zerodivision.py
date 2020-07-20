try:
    a,b = input('두수를 넣으세요').split()
    result = (int(a)/int(b))
    print(result)
except ZeroDivisionError:
    print('0으로는 나눌 수 없습니다')
except TypeError:
    print("지원되지 않는 연산자를 사용한 오류입니다.")

except Exception as a:
    print("오류 종류",a)

print('test')