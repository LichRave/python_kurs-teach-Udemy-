# Zadanie 1.
def factorial(n: int) -> int | str:
    if isinstance(n, str):
        return "Input as string not allowed. Input must be a positive integer or zero."

    if not isinstance(n, int) and not isinstance(n, float):
        return "Input allowed only in the form of a positive integer or zero."

    if not int(n) == n or n < 0:
        return "Only natural numbers allowed"

    result = 1

    for i in range(1, int(n) + 1):
        result *= i  # odpowiednik result = result * i

    return result


# Testy do funkcji factorial

assert factorial(n=0) == 1  # corner case: 0 obliczamy z definicji
assert (
    factorial(n=1) == 1
)  # corner case: 1 to pierwszy n, dla którego wykorzystujemy wzór
assert (
    factorial(n=1.0) == 1
)  # jeśli liczba nie ma części ułamkowej, to traktujemy ją jako całkowitą
assert factorial(n=8) == 40320  # middle case: standardowe obliczenia dla jakiegoś n

assert factorial(n=0.5) == "Only natural numbers allowed"  # nie obsługujemy ułamków
assert (
    factorial(n=-10) == "Only natural numbers allowed"
)  # nie obsługujemy liczb ujemnych

assert (
    factorial(n="string")
    == "Input as string not allowed. Input must be a positive integer or zero."
)  # nie obsługujemy stringów
assert (
    factorial(n=None) == "Input allowed only in the form of a positive integer or zero."
)  # nie obsługujemy None'ów (i innych typów)
