# Rotate vector of n elements left by i
def rotate_cool(x, i):
    v = x[:]
    temp = v[0]
    j = 0
    incr = 1
    k = i % len(v)
    while k != 0:
        v[j] = v[k]
        j = k
        incr += 1
        k = (incr * i) % len(v)
    v[j] = temp
    return v

def rotate_clean(x, i):
    left = x[:i][::-1]
    right = x[i:][::-1]
    return (left + right)[::-1]

if __name__ == '__main__':
    v = [1, 2, 3, 4, 5]
    print(v)
    print(rotate_cool(v, 3))
    print(rotate_cool(v, 2))
    print(rotate_clean(v, 3))
