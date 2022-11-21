user_id = input('id ? ')
user_pwd = input('password ? ')

'''
if user_pwd == '111111':
    print('Hello Master')
else:
    print('Who are you?')
'''
#같은 블럭에 속하는 명령어는 같은 방법으로 들여쓰기를 해야한다
#주석처리를 하기 위해서는 명령문 앞에 #을 붙여도 되지만, 앞뒤로 '''을 사용할 수도 있다.


#조건문과 조건문의 중첩
'''
if user_id == 'taxpace':
    if user_pwd == '111111':
        print('Hello Master')
    else:
        print('Who are you?')
else:
    print('Who are you?')
'''


#조건문과 논리연산자 (Logical Operator)
if user_id == 'taxpace' and user_pwd == '111111':
        print('Hello Master')
elif user_id =='baton' and user_pwd =='222222':
        print('Hello Master')
else:
        print('Who are you?')

print(not True) #Case sensitive
print(not False) #Case sensitive
