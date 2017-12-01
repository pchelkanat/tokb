import random

"""
Тест Миллера-Рабина
Пусть число n > 2–нечетно и n−1 = 2^s·d, где d–нечетно.
Для каждого числа a от 2 до r + 1, где r – число проверок в тесте, выполним следующие действия:
1. Вычислим x[0] = a^d(mod n).
2. Проверим условие x[0] ∈ {1, n − 1}. Если оно выполнится, тогда a–свидетель простоты. 
Перейдем к следующему a.
3. Иначе проверим, содержится ли число n − 1 в последовательности
{x[1], x[2], ..., x[s−1]}, где каждый последующий x вычисляется по формуле x[i+1] = x[i]^2(mod n).
Если ответ положительный, то a–свидетель простоты. Перейдем к следующему a ≤ r + 1.
Иначе, найден свидетель непростоты n.
Завершаем тест с сообщением «число n–составное».
Если после r проверок окажется r свидетелей простоты, то заканчиваем тест с сообщением «n–вероятно простое».
"""


def find_sd(n):
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d /= 2
    return s, int(d)


def MillerRabin(n, r=5):
    #число свидетелей простоты
    countOfWitnesses = 0
    # порядковое присваивание s и d
    s, d = find_sd(n)
    #print(s, d)

    #
    for a in range(2, r + 2):
        # x = pow(a, d, n)  # x=a^d mod n
        x = (a ** d) % n
        #print(a, pow(a, d), x)

        if x == 1 or x == (n - 1):
            countOfWitnesses += 1
            continue
        for i in range(s - 1):
            x = pow(x, 2, n)
            # x = (x * x) % n
            #print(".", a, pow(x, 2), x)
            if x == 1:
                return False  # Составное
            elif x == (n - 1):
                a = 0
                break
        if a:
            return False  # Составное
    #print(countOfWitnesses)
    return True  # Простое


print(MillerRabin(1567451))