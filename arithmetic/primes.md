Алгоритм называется "Решето Эратосфена". 
*Представлена небольшая модификация с использованием только нечётных чисел.*
Мы проходим по всем числам от 3 до `$i^2 < n$` и проверяем все последующие `$j = i^2$` до `$n$` с шагом `$i$`.
Время работы алгоритма `$O(n \cdot log(log n))$`

```python
def isprime(a: int) -> bool:
    '''
    Return if number is a prime number.
    Eratosphen's sieve algorithm.
    '''

    assert a >= 0

    if a in [0, 1]:
        return False

    primes = [bool(_ % 2) for _ in range(a + 1)]
    primes[:3] = [False, False, True]

    # iterate over the odd number only
    for i in [i for i in range(3, a + 1) if i * i <= a and i % 2]:
        # start from the i^2 and check every next +i number
        for j in [j for j in range(i * i, a + 1, i)]:
            primes[j] = False

    return primes[a]
```
