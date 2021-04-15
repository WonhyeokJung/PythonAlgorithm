# lambda
def functionName(parameter):
    return result

== lambda parameter:result

# example
(lambda x : x + 1)(3)
func = lambda x: x + 1
func(4)
# 5

#######################################################

# sorted example
s = ['2 A', '1 B', '4 C', '1 A']

print(sorted(s))
# 문자를 기준으로 정렬하고 싶다면
def func(x):
    return x.split()[1], x.split()[0]

s.sort(key=func)  # key = sort 기준 값을 지정(sort key)
print(s)

# Using Lambda !
s.sort(key = lambda x: (x.split()[1], x.split()[0]))
print(s)