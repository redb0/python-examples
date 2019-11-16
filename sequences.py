_GR = (1 + 5**0.5) / 2  # golden ratio


def golomb_seq(n=1):  # первые n элементов через рекурсию
    if n == 1:
        return 1
    return 1 + golomb_seq(n - golomb_seq(golomb_seq(n - 1)))


def golomb_cl(n=1):  # первые n кластеров (по числам)
    g = [1, 2, 2]
    if 1 <= n <= 3:
        return g[:n]
    for i in range(3, n):
        g += [i] * g[i-1]
    return g

def golomb_lst(n=1):  # первые n элементов
    g = [1]
    for i in range(1, n):
        g.append(1 + g[i - g[g[i - 1] - 1]])
    return g


def silverman_seq(*args, **kwargs):
    return golomb_lst(*args, **kwargs)


def lucas_number(n, recf=False):  # числа Люка
    if not recf:  # как функция
        for i in range(n):
            yield int(_GR**i + (-_GR)**(-i))
    else:  # рекуррентная формула
        b = [2, 1]
        for i in range(n):
            if 0 <= i <= 1:
                yield b[i]
            else:
                b = [b[-1], b[-1] + b[-2]]
                yield b[-1]


def fibonacci(n, recf=False):
    if recf:  # рекуррентная формула
        b = [0, 1]
        for i in range(n):
            b = [b[-1], sum(b)]
            yield b[-1]
    else:  # через формулу Бине
        for i in range(n):
            yield int((_GR**i - (-_GR)**(-i)) / (2*_GR - 1)) 



def main():
    lst_1 = golomb_cl(20)
    lst_2 = golomb_lst(20)
    print(len(lst_1), len(lst_2))
    #for i, item in enumerate(lst_2):
        # assert item == golomb_seq(i + 1)
        # print(i + 1, '-', item, '-', lst_1[i])
    for i in fibonacci(10, recf=True):
        print(i)
    print('-' * 20)

    

if __name__ == '__main__':
    main()
