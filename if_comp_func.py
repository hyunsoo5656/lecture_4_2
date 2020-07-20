n_lists = list(range(1,101))

#짝수만 제곱하여 배열 만들기
squre_arr =[x**2 for x in n_lists if x%2==0]

#2와 3의 공배수만 제곱하여 배열 만들기
squre_arr_1 =[x**2 for x in n_lists if x%2==0 and x%3==0]
print(squre_arr_1)