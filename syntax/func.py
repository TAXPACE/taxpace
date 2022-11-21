# #!python
# a=1
# b=2
# c=3
# s=a+b+c
# r=s/3
# print(r)
# #code...

#함수의 input
#function and parameter
# def average():
#     a=1
#     b=2
#     c=3
#     s=a+b+c
#     r=s/3
#     print(r)
#
# #argument 인자
# average(10, 20, 30)


# def averageEmail(a,b,c):
#     s=a+b+c
#     r=s/3
#     print(r)



#return 뒤의 부분은 해당 함수에 대한 표현식
# def a():
    # return 'haha'
# print(a())

def average(a,b,c):
    s=a+b+c
    r=s/3
    return r

print ("평균값은", average(10,20,30))
