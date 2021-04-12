import collections

a = collections.defaultdict(int)

print(8>>5)
print(9<<2)
print(~-9)

# 비트 변환 출력
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)

# 예제 1
for i in range(-5, 6):
    print("%3d = " % i, end='')
    Bbit_print(i)

print("--------------------")
# 예제 2
a = 0x10
x = 0x01020304  # 숫자하나당 4자리 차지하므로, 01 8칸 02 8칸 03 8칸 04 8칸
print("%d = " % a, end='')
Bbit_print(a)
print()
print("0%X = " % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i * 8) & 0xff)

print("--------------------")
# 예제 3
n = 0x00111111

if n & 0xff:  # 0xff 255
    print("little endian")
else:
    print("big endian")

print("--------------------")
# 예제 4
def ce(n):  # change endian
    p = []
    for i in range(0, 4):
        p.append((n >> (24 - i * 8)) & 0xff)
    return p


def ce1(n):
    return ((n << 24) & 0xff000000) | ((n << 8) & 0xff0000) | ((n >> 8) & 0xff00) | ((n >> 24) & 0xff)


x = 0x01020304
p = []
for i in range(0, 4):
    p.append((x >> (i * 8)) & 0xff)

print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
p = ce(x)
print("x = %d%d%d%d" % (p[0], p[1], p[2], p[3]))
p = ce1(x)
print(hex(p))
# %02x : 뒤에부터2칸 모자라면 0채우고 16진수로

print("----------------")
# 예제 5
def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)


a = 0x86
key = 0xAA

print("a      ==> ", end='')
Bbit_print(a)

print("a^=key ==> ", end='');
a ^= key;
Bbit_print(a)

print("a^=key ==> ", end='');
a ^= key;
Bbit_print(a)