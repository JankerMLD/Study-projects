n, m, k, x, y, z, t, a = int(input()),  int(input()),  int(input()),  int(input()),  int(input()),  int(input()),  int(input()), int(input())
o = n + m - x
u = m + k - y
e = k + n - z
result1 = (n - o - e + t) + (m - u - o + t) + (k - u - e + t)
result2 = o + u + e - 3 * t
result3 = a - (x + k - u - e + t)
print(result1)
print(result2)
print(result3)