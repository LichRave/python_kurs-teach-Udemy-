# %%
class MyValueError(Exception):
    pass


class TriangleError(Exception):
    pass


class ZeroDivisionError(Exception):
    pass


# Sprawdzanie wartosci
def triangle(a, b, c):
    try:
        int_a = int(a)
        int_b = int(b)
        int_c = int(c)
    except:
        raise MyValueError("WARTOSC A, B, LUB C JEST NIEPOPRAWNA!")

    # Sprawdznie na wlasciwosc:
    if not (int_a + int_b > int_c and int_b + int_c > int_a and int_a + int_c > int_b):
        raise TriangleError("TO NIE JEST TROJKAT!")

    # Sprawdzenie na zera:
    if int_a <= 0 or int_b <= 0 or int_c <= 0:
        raise ZeroDivisionError("PODALES ZERO!")

    # Dzialanie
    return int_a + int_b + int_c

# Program
if __name__ == "__main__":
    a = input("Podaj a: ")
    b = input("Podaj b: ")
    c = input("Podaj c: ")

    print(f"Obwod trojkata to: {triangle(a, b, c)}")
