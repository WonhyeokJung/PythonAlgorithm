# Python For Beginners.
## sys
```python
# input으로 받을 때, python 입력 버퍼 크기 문제로 메모리 초과 발생 가능
import sys
# Read and Load all contents
sys.stdin = open("input.txt", "r")
variable = input()  # Input from sys.stdin
		 = sys.stdin.readline() # read one line as same way with 'input()'

```

## Bitwise Operators
```python
8 & 3  # And / if both are 1, return 1
1000
0011
----
0000 return 0

8 | 3 # Pipe / Either of those are 1, return 1
1000
0011
----
1011 return 11

7 ^ 3  # XOR(exclusive or) if 1 and 0 or 0 and 1, return 1
0111
0011
----
0100 return 4

9(x) >> 1(n)  # Move x, n times to the right
# == x//(2**n)
1001
----
0100 return 4

9(x) << 1(n)  # Move x, n times to the left
# == x*(2**n)
1001
----
10010 return 18

# One's complement
~9  # change 1 to 0, 0 to 1
== -(x+1)
1001
----
0110 return -10 

# Two's complement
# + 1 on (2**0)bit of number
# **Two's complement + number = 0**
 9 =               1001
-9 = 0110 + 0001 = 0111
-----------------------
                 1 0000  # if Most significant bit is 1, it means negative.
```

## Formatting 

```python
# 9.100000 소숫점 일곱번째 자리에서 여섯번 째로 반올림.
print(f'#{tc} {"%.6f" % maxs}')
# ---------------------------------- #
print(f'#{tc}', end = ' ')
print(format(maxs, '.6f'))
# ---------------------------------- #
print("#{} {}".format(tc, "%.6f" % maxs))
# ---------------------------------- #
print(f'#{tc} {maxs:0.6f}')
```

