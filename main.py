import math
from collections import Counter

if __name__ == '__main__':

    n = 300
    k = 3
    y0 = 0.514
    g = 12345678

    sequence = [y0, ]

    for i in range(n):
        sequence.append(round(pow(10, -k) * math.modf(pow(10, k) * math.modf(g * sequence[i])[0])[1], k))

        sequence[0] = round(sequence[0], k)

    for i in range(n + 1):
        print(str(i) + " " + str(sequence[i]))

    counter = Counter(sequence)
    print(counter)

    r = math.floor(1 + 3.3 * math.log10(n + 1))
    pi = round(1/r, 3)
    print("r" + " = " + str(r))
    print("pi" + " = " + str(pi))

    not_sorted_sequence = sequence.copy()
    sequence.sort()

    print(sequence)

    frequencies = []
    low = 0
    high = pi
    for i in range(r):
        frequency = 0
        for j in range(1, n + 1):
            if low <= sequence[j] <= high:
                frequency += 1

        frequencies.append(frequency)
        low += pi
        high += pi

    print(frequencies)

    chisquare = 0
    for i in range(r):
        chisquare += pow(frequencies[i] - n * pi, 2) / (n * pi)

    print(chisquare)

    theoretical_chisquares = [0.004, 0.103, 0.352, 0.711, 1.145, 1.635, 2.167, 2.733, 3.325, 3.940, 4.575, 5.226]  # до 12 степени свободы

    s = r - 1

    theoretical_chisquare = theoretical_chisquares[s - 1]

    print(theoretical_chisquare)

    if chisquare > theoretical_chisquare:
        print("Результаты противоречат!")
    else:
        print("Результаты подтверждают!")

    l = not_sorted_sequence.index(counter.most_common(1)[0][0])
    print(l)
    L = not_sorted_sequence.index(counter.most_common(1)[0][0], l+1)
    print(L)

    P = L - l
    print(P)














