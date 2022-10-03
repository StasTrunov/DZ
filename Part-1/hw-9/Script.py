from Module import square
from Module import curcle

f1 = square(3)
f2 = curcle(5)

if f1 < f2:
    print(f1, '<', f2)
elif f1 > f2:
    print(f1, '>', f2)
else:
    print(f1, '=' ,f2)
