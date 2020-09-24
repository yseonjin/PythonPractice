# PythonPractice
PythonPractice/ Practice ,  basic
<br><br>Python을 처음 시작하면서, 문법예제 연습을 위해 만들었습니다.
<br><br>
~~~
print('Hello World!')
print('안녕하세요')
~~~
<br><br>
~~~
number1 = 1
pi = 3.14
flag = True
char = 'X'
chars = 'I Love Python'

print(number1,pi,flag,char,chars)
print('-------------')

s = number1+2
s2 = pi + number1

print(s,s2)
~~~
<br><br>
~~~~
x=1
y=2

if x>y:
    print('x가 y보다 큽니다.')
elif x<y:
    print('x가 y보다 작습니다.')
else:
    print('x와 y가 같습니다.') 
~~~
<br><br>
~~~
scope = [1,2,3,4,5]
for x in scope:
    print(x, end=" ")

print(' ')

stri = 'abcdef'
for y in stri:
    print(y, end=" ")

print(' ')

dicti = {'a':97,'b':98,'c':99}
for z in dicti:
    print(z, end=" ")

print(' ')

dicti = {'a':97,'b':98,'c':99}
for q in dicti:
    print(dicti[q], end=" ")

print(' ')

for c in range(2,10,3):
    print(c,end=" ")
~~~~
<br><br>
~~~
scope = [1,2,3,4,5]
for x in scope:
    print(x)
else:
    print('Perfect')

print('=========')

scope = [1,2,3,4,5]
for y in scope:
    print(y)
    break
else:
    print('Perfect')
~~~
<br><br>
~~~
x=0
while x<10:
    x+=1
    if x<3:
        continue
    print(x)
    if x>7:
        break 
~~~
