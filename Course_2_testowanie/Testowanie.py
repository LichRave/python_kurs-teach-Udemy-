# %% Czemu trzeba testować
"""
Testowanie w języku Python: wstęp
1) Każdy popełnia błędy, które niestety mogą być bardzo kosztowne. Jako deweloperzy mamy tylko jeden sposób na podjęcie próby unikania tych błędów -- jest to otestowany kod.
2) Trudno jest przewidzieć wszystkie przypadki wykorzystania danego oprogramowania (w zasadzie jest to niestety niemożliwe). Mimo tego próbować warto. 3) 3) Pisanie testów pomaga nam w byciu kreatywnymi (tzn. w rozważaniu przeróżnych przypadków). Dzięki temu mamy szansę na ,,tanie'' wyeliminowanie części potencjalnych błędów.
4) Naszym celem jest uniknięcie wychwycenia błędów przez klientów, czyli użytkowników oprogramowania, bo to jest po prostu droższe i powoduje utratę wiarygodności.
5) Duża ilość testów pozwala nam na bezpieczniejszy proces wdrażania poprawek lub przepisywania aplikacji; jesteśmy w stanie od razu stwierdzić czy powstały na nowo kawałek kodu działa zgodnie z oczekiwaniami.
6) Testy są istotnym elementem dokumentacji kodu. Pomagają w zrozumieniu działania danych fragmentów oprogramowania, są też nieocenione we wzdrażaniu nowych oosób w dany projekt.

"""

# %% Jak testować oprogramowanie?
"""
---- 
Wchodzi tester oprogramowania do baru. Patrzy na barmana i zamawia jedno piwo. Potem dwa piwa. Następnie zamawia milion piw, a zaraz potem zamawia brak piwa. Potem prosi o -1 piwo, a następnie o dokładnie 0 piw.
----

Przykład:

Zadanie 1. Napisz funkcję, która implementuje matematyczne działanie obliczania silni z liczby  n .

Definicja. Silnią z liczby  n  nazywamy liczbę  n!=1⋅2⋅…⋅n ,  n∈N . Ponadto  0!=1 .

Kryteria, które powinny być zastosowane do naszej funkcji:

1) Jeżeli liczba jest równa  0 , to zwracamy  1 .
2) Jeżeli liczba  n  jest naturalna i większa od  0 , to zwracamy  1⋅2⋅…⋅n .
3) Jeżeli użytkownik poda nam liczbę, która nie jest naturalna lub nie jest zerem, to wydrukujmy specjalny komunikat o treści Only natural numbers allowed.
4) Jeżeli użytkownik poda nam tekst (jakikolwiek, tj. odrzucamy też np. "2"), to wydrukujmy specjalny komunikat o treści Input as string not allowed. Input must be a positive integer or zero.
5) Jeżeli użytkowni poda nam obiekt niebędący tekstem ani liczbą (tj. poda nam funkcję, None, podam nam klasę, itp.), to wydrukujmy komunikat Input allowed only in the form of a positive integer or zero.
"""


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


# %% assert
"""
Sposób testowania z wykorzystaniem słowa kluczowego `assert`
Python udostępnia nam słowo kluczowe `assert`, które obudowuje operator porównania `==`. W przypadku, gdy porównywane strony są sobie równe, to `assert` niczego nie robi, po prostu omija tą linijkę. Natomiast jeśli porównywane strony są różne, to podnosi wyjątek `AssertionError` i wskazuje, która asercja ,,nie przeszła'', tzn. które wartości nie są sobie równe.

Na przykład linijka
```
assert 1 == 1
```
nie będzie miała żadnego wpływu na działanie kodu, natomiast linijka
```
assert 1 == 2
```
spowoduje podniesienie wyjątku `AssertionError` no i przerwanie wykonywania kodu.

**Uwaga.** Liczby, stringi, listy, słowniki, krotki (ang. *tuple*) i inne struktury danych porównujemy z użyciem operatora `==`, natomiast wartości logiczne <tt>True</tt>, <tt>False</tt> oraz singletony, tj. <tt>None</tt> porównujemy z wykorzystaniem operatora `is`. Na przykład
```
assert True is True
```
a nie
```
assert True == True
```
"""

# %% Różnica == a is

# Przykład do is vs ==
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

c = (1, 2, 3)
d = (1, 2, 3)

print(c == d)
print((1, 2, 3) is (1, 2, 3))

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)

# 2 Przykład do is vs ==
a = 1
b = 1

print(a == b)
print(a is b)
print(f"address of a: {id(a)} \t address of b: {id(b)} \t diff: {id(a) - id(b)}")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(f"address of a: {id(a)} \t address of b: {id(b)} \t diff: {id(a) - id(b)}")

# %%
# Testy do funkcji factorial

assert factorial(n=0) == 1  # corner case: 0 obliczamy z definicji
assert factorial(n=1) == 1  # corner case: 1 to pierwszy n, dla którego wykorzystujemy wzór
assert factorial(n=1.0) == 1  # jeśli liczba nie ma części ułamkowej, to traktujemy ją jako całkowitą
assert factorial(n=8) == 40320  # middle case: standardowe obliczenia dla jakiegoś n

assert factorial(n=0.5) == "Only natural numbers allowed"  # nie obsługujemy ułamków
assert factorial(n=-10) == "Only natural numbers allowed"  # nie obsługujemy liczb ujemnych

assert factorial(n="string") == "Input as string not allowed. Input must be a positive integer or zero."  # nie obsługujemy stringów
assert factorial(n=None) == "Input allowed only in the form of a positive integer or zero."  # nie obsługujemy None'ów (i innych typów)

# %%
"""
Podsumowanie
Napisaliśmy funkcję i wymyśliliśmy sporo scenariuszy, które mogą się pojawić podczas korzystania z niej. Dzięki naszej kreatywności byliśmy w stanie przewidzieć różne problemy, które mogą się pojawić, a co za tym idzie potrafiliśmy poprawnie na nie zareagować.

Co więcej, testując zachowanie naszej funkcji, wiemy czego można od niej oczekiwać w określonych warunkach. Teraz, jeśli będziemy chcieli przepisać naszą funkcję lub, w jakiś sposób, ją zmodyfikować, to mamy punkt startowy, czyli zbiór warunków, które nasza funkcja musi spełniać.
"""

#%%
#Zadanie 2
"""Zadanie 2. Przepiszmy funkcję z zadania 1 z użyciem funkcji reduce z pakietu functools, będziemy używać wymienionej już funkcji reduce oraz słówka kluczowego lambda czyli funkcji anonimowej w języku Python."""

# Funkcja lambda, czyli funkcja anonimowa w języku Python

# 1. Funkcję lambda możemy wykorzystywać jak wszystkie inne funkcje w języku Python, tj.
# możemy po prostu zdefiniować jakąś funkcją w inny sposób (korzystając z innej składni).
# Jest to rzadkie użycie funkcji lambda.

def x_squared_def(x: float) -> float:
  return x ** 2


assert x_squared_def(x=0) == 0
assert x_squared_def(x=2) == 4


x_squared_lambda = lambda x: x ** 2


assert x_squared_lambda(x=0) == 0
assert x_squared_lambda(x=2) == 4


# 2. Funkcje anonimowe najczęściej wykorzystujemy jako "narzędzia" w argumentach innych funkcji,
# dobrym przykładem może być tutaj sortowanie.

# Zadanie: posortuj tablicę stringów ["caCc", "cbBc", "ccAc"] po trzeciej literce, czyli oczekiwany
# rezultat to ["ccAc", "cbBc", "ccCc"].

ls = ["caCc", "cbBc", "ccAc"]
print(sorted(ls, key=lambda x: x[2]))

#%%

['ccAc', 'cbBc', 'caCc']

#%%
from functools import reduce

# Funkcja: reduce (pakiet functools)
# Metoda ta jest wykorzystywana do nakładania na siebie tych samych obliczeń,
# funkcja ta przyjmuje dwa argumentu, funkcję (która definiuje jakieś działanie)
# oraz kolekcję, czyli np. listę.

# Dzięki reduce możemy rozwiązać np. problem posumowania elementów w liście, zapiszemy to
# jako reduce(lambda x, y: x + y, [1, 2, 3, 4]). Ta funkcja będzie działała następująco:
# krok 1: weź 1 i 2, wykonaj działanie 1 + 2 i zwróć wynik tego działania czyli 3,
# krok 2: weź wynik z poprzedniego kroku (3) i weź kolejny element z listy (3), zwróć 3 + 3 = 6,
# krok 3: weź wynik z poprzedniego kroku (6) i weź kolejny element z listy (4), zwróć 6 + 4 = 10,
# krok ...: powtarzaj do momentu, w którym skończą się elementy w liście.

# Innymi słowy reduce nakłada kolejne elementy zgodnie z jakimś wzorem.

print(" + ".join([str(_) for _ in [1, 2, 3, 4]]), " = ", reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(" * ".join([str(_) for _ in [1, 2, 3, 4]]), " = ", reduce(lambda x, y: x * y, [1, 2, 3, 4]))

#%%

1 + 2 + 3 + 4  =  10
1 * 2 * 3 * 4  =  24

#%%

# Powrót do zadania 2
def factorial(n: int) -> int | str:
  if isinstance(n, str):
    return "Input as string not allowed. Input must be a positive integer or zero."

  if not isinstance(n, int) and not isinstance(n, float):
    return "Input allowed only in the form of a positive integer or zero."

  if not int(n) == n or n < 0:
    return "Only natural numbers allowed"

  if n == 0:
    return 1
  return reduce(lambda x, y: x * y, [_ for _ in range(1, int(n) + 1)])


assert factorial(n=0) == 1  # corner case: 0 obliczamy z definicji
assert factorial(n=1) == 1  # corner case: 1 to pierwszy n, dla którego wykorzystujemy wzór
assert factorial(n=1.0) == 1  # jeśli liczba nie ma części ułamkowej, to traktujemy ją jako całkowitą
assert factorial(n=8) == 40320  # middle case: standardowe obliczenia dla jakiegoś n

assert factorial(n=0.5) == "Only natural numbers allowed"  # nie obsługujemy ułamków
assert factorial(n=-10) == "Only natural numbers allowed"  # nie obsługujemy liczb ujemnych

assert factorial(n="string") == "Input as string not allowed. Input must be a positive integer or zero."  # nie obsługujemy stringów
assert factorial(n=None) == "Input allowed only in the form of a positive integer or zero."  # nie obsługujemy None'ów (i innych typów)

#%%
Загрузка…
Перейти к основному контенту
Testowanie: 10 stycznia 2024.ipynb
Testowanie: 10 stycznia 2024.ipynb_Пометка блокнота снята
Изменения не будут сохранены
Testowanie w języku Python: wstęp
Każdy popełnia błędy, które niestety mogą być bardzo kosztowne. Jako deweloperzy mamy tylko jeden sposób na podjęcie próby unikania tych błędów -- jest to otestowany kod.
Trudno jest przewidzieć wszystkie przypadki wykorzystania danego oprogramowania (w zasadzie jest to niestety niemożliwe). Mimo tego próbować warto. Pisanie testów pomaga nam w byciu kreatywnymi (tzn. w rozważaniu przeróżnych przypadków). Dzięki temu mamy szansę na ,,tanie'' wyeliminowanie części potencjalnych błędów.
Naszym celem jest uniknięcie wychwycenia błędów przez klientów, czyli użytkowników oprogramowania, bo to jest po prostu droższe i powoduje utratę wiarygodności.
Duża ilość testów pozwala nam na bezpieczniejszy proces wdrażania poprawek lub przepisywania aplikacji; jesteśmy w stanie od razu stwierdzić czy powstały na nowo kawałek kodu działa zgodnie z oczekiwaniami.
Testy są istotnym elementem dokumentacji kodu. Pomagają w zrozumieniu działania danych fragmentów oprogramowania, są też nieocenione we wzdrażaniu nowych oosób w dany projekt.
Jak testować oprogramowanie?
Wchodzi tester oprogramowania do baru. Patrzy na barmana i zamawia jedno piwo. Potem dwa piwa. Następnie zamawia milion piw, a zaraz potem zamawia brak piwa. Potem prosi o -1 piwo, a następnie o dokładnie 0 piw.

Przykład
Zadanie 1. Napisz funkcję, która implementuje matematyczne działanie obliczania silni z liczby n.

Definicja. Silnią z liczby n nazywamy liczbę n!=1⋅2⋅…⋅n, n∈N. Ponadto 0!=1.

Kryteria, które powinny być zastosowane do naszej funkcji.

Jeżeli liczba jest równa 0, to zwracamy 1.
Jeżeli liczba n jest naturalna i większa od 0, to zwracamy 1⋅2⋅…⋅n.
Jeżeli użytkownik poda nam liczbę, która nie jest naturalna lub nie jest zerem, to wydrukujmy specjalny komunikat o treści Only natural numbers allowed.
Jeżeli użytkownik poda nam tekst (jakikolwiek, tj. odrzucamy też np. "2"), to wydrukujmy specjalny komunikat o treści Input as string not allowed. Input must be a positive integer or zero.
Jeżeli użytkowni poda nam obiekt niebędący tekstem ani liczbą (tj. poda nam funkcję, None, podam nam klasę, itp.), to wydrukujmy komunikat Input allowed only in the form of a positive integer or zero.
[ ]
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
Sposób testowania z wykorzystaniem słowa kluczowego assert
Python udostępnia nam słowo kluczowe assert, które obudowuje operator porównania ==. W przypadku, gdy porównywane strony są sobie równe, to assert niczego nie robi, po prostu omija tą linijkę. Natomiast jeśli porównywane strony są różne, to podnosi wyjątek AssertionError i wskazuje, która asercja ,,nie przeszła'', tzn. które wartości nie są sobie równe.

Na przykład linijka

assert 1 == 1
nie będzie miała żadnego wpływu na działanie kodu, natomiast linijka

assert 1 == 2
spowoduje podniesienie wyjątku AssertionError no i przerwanie wykonywania kodu.

Uwaga. Liczby, stringi, listy, słowniki, krotki (ang. tuple) i inne struktury danych porównujemy z użyciem operatora ==, natomiast wartości logiczne True, False oraz singletony, tj. None porównujemy z wykorzystaniem operatora is. Na przykład

assert True is True
a nie

assert True == True
[ ]
# Przykład do is vs ==
a = 1
b = 1

print(a == b)
print(a is b)
print(f"address of a: {id(a)} \t address of b: {id(b)} \t diff: {id(a) - id(b)}")

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
print(f"address of a: {id(a)} \t address of b: {id(b)} \t diff: {id(a) - id(b)}")
account_circle
True
True
address of a: 133816556388592 	 address of b: 133816556388592 	 diff: 0
True
False
address of a: 133815286595328 	 address of b: 133816143160768 	 diff: -856565440
[ ]
# Zagadka
a = 1
b = a

print(a == b)
print(a is b)
print(f"address of a: {id(a)} \t address of b: {id(b)} \t diff: {id(a) - id(b)}")

a = [1, 2, 3]
b = a

print(a == b)
print(a is b)
print(f"address of a: {id(a)} \t address of b: {id(b)} \t diff: {id(a) - id(b)}")
account_circle
True
True
address of a: 133816556388592 	 address of b: 133816556388592 	 diff: 0
True
True
address of a: 133815286740736 	 address of b: 133815286740736 	 diff: 0
[ ]
# Testy do funkcji factorial

assert factorial(n=0) == 1  # corner case: 0 obliczamy z definicji
assert factorial(n=1) == 1  # corner case: 1 to pierwszy n, dla którego wykorzystujemy wzór
assert factorial(n=1.0) == 1  # jeśli liczba nie ma części ułamkowej, to traktujemy ją jako całkowitą
assert factorial(n=8) == 40320  # middle case: standardowe obliczenia dla jakiegoś n

assert factorial(n=0.5) == "Only natural numbers allowed"  # nie obsługujemy ułamków
assert factorial(n=-10) == "Only natural numbers allowed"  # nie obsługujemy liczb ujemnych

assert factorial(n="string") == "Input as string not allowed. Input must be a positive integer or zero."  # nie obsługujemy stringów
assert factorial(n=None) == "Input allowed only in the form of a positive integer or zero."  # nie obsługujemy None'ów (i innych typów)

Podsumowanie
Napisaliśmy funkcję i wymyśliliśmy sporo scenariuszy, które mogą się pojawić podczas korzystania z niej. Dzięki naszej kreatywności byliśmy w stanie przewidzieć różne problemy, które mogą się pojawić, a co za tym idzie potrafiliśmy poprawnie na nie zareagować.

Co więcej, testując zachowanie naszej funkcji, wiemy czego można od niej oczekiwać w określonych warunkach. Teraz, jeśli będziemy chcieli przepisać naszą funkcję lub, w jakiś sposób, ją zmodyfikować, to mamy punkt startowy, czyli zbiór warunków, które nasza funkcja musi spełniać.

Zadanie 2. Przepiszmy funkcję z zadania 1 z użyciem funkcji reduce z pakietu functools, będziemy używać wymienionej już funkcji reduce oraz słówka kluczowego lambda czyli funkcji anonimowej w języku Python.

[ ]
# Funkcja lambda, czyli funkcja anonimowa w języku Python

# 1. Funkcję lambda możemy wykorzystywać jak wszystkie inne funkcje w języku Python, tj.
# możemy po prostu zdefiniować jakąś funkcją w inny sposób (korzystając z innej składni).
# Jest to rzadkie użycie funkcji lambda.

def x_squared_def(x: float) -> float:
  return x ** 2


…
# 2. Funkcje anonimowe najczęściej wykorzystujemy jako "narzędzia" w argumentach innych funkcji,
# dobrym przykładem może być tutaj sortowanie.

# Zadanie: posortuj tablicę stringów ["caCc", "cbBc", "ccAc"] po trzeciej literce, czyli oczekiwany
# rezultat to ["ccAc", "cbBc", "ccCc"].

ls = ["caCc", "cbBc", "ccAc"]
print(sorted(ls, key=lambda x: x[2]))
account_circle
['ccAc', 'cbBc', 'caCc']
[ ]
from functools import reduce

# Funkcja: reduce (pakiet functools)
# Metoda ta jest wykorzystywana do nakładania na siebie tych samych obliczeń,
# funkcja ta przyjmuje dwa argumentu, funkcję (która definiuje jakieś działanie)
# oraz kolekcję, czyli np. listę.

# Dzięki reduce możemy rozwiązać np. problem posumowania elementów w liście, zapiszemy to
# jako reduce(lambda x, y: x + y, [1, 2, 3, 4]). Ta funkcja będzie działała następująco:
# krok 1: weź 1 i 2, wykonaj działanie 1 + 2 i zwróć wynik t… (3) i weź kolejny element z listy (3), zwróć 3 + 3 = 6,
# krok 3: weź wynik z poprzedniego kroku (6) i weź kolejny element z listy (4), zwróć 6 + 4 = 10,
# krok ...: powtarzaj do momentu, w którym skończą się elementy w liście.

# Innymi słowy reduce nakłada kolejne elementy zgodnie z jakimś wzorem.

print(" + ".join([str(_) for _ in [1, 2, 3, 4]]), " = ", reduce(lambda x, y: x + y, [1, 2, 3, 4]))
print(" * ".join([str(_) for _ in [1, 2, 3, 4]]), " = ", reduce(lambda x, y: x * y, [1, 2, 3, 4]))
account_circle
1 + 2 + 3 + 4  =  10
1 * 2 * 3 * 4  =  24
[ ]
# Powrót do zadania 2
def factorial(n: int) -> int | str:
  if isinstance(n, str):
    return "Input as string not allowed. Input must be a positive integer or zero."

  if not isinstance(n, int) and not isinstance(n, float):
    return "Input allowed only in the form of a positive integer or zero."

  if not int(n) == n or n < 0:
    return "Only natural numbers allowed"
…
assert factorial(n=0.5) == "Only natural numbers allowed"  # nie obsługujemy ułamków
assert factorial(n=-10) == "Only natural numbers allowed"  # nie obsługujemy liczb ujemnych

assert factorial(n="string") == "Input as string not allowed. Input must be a positive integer or zero."  # nie obsługujemy stringów
assert factorial(n=None) == "Input allowed only in the form of a positive integer or zero."  # nie obsługujemy None'ów (i innych typów)
TDD (Test-Driven Development)
TDD jest techniką pisania oprogramowania (nie jest to technika pisania testów), w której główną ideą jest rozpoczęscie prac programistycznych od napisania zbioru testów do jeszcze nieistniejącej funkcjonalności, a dopiero potem napisanie kodu implementującego tę funkcjonalność.

TDD nie jest jedyną słuszną techniką tworzenia oprogramowania. Alternatywnie można pisać testy równolegle z pisaniem kodu lub można je pisać po skończeniu implementacji rozwiązania (ale to nie jest już TDD, w TDD testy pojawiają się zawsze przed rozpoczęciem kodowania).

Cykle w TDD
Faza czerwona: napisanie i uruchomienie testów. Pierwszym krokiem w TDD jest stworzenie scenariuszy testowych (napisanie testów) i włączenie ich. Oczywiście testowanie zakończy się niepowodzeniem, bo testowana funkcjonalność jeszcze nie istnieje.
Faza zielona: napisanie minimalnej ilości kodu, pozwalającego na dostarczenie funkcjonalności. W tym miejscu testy powinny przechodzić, a więc kolor czerwony (błędy asercji) zmieniają się na kolor zielony. W tej fazie cyklu nie musimy pisać genialnego kodu, chodzi nam o rozwiązanie, które spełnia wymogi testowe.
Faza refaktoru: w tym kroku robimy tak, żeby nasz kod jednak był genialny, tzn. testy już przechodzą, mamy funkcjonalność i rozumiemy jak ona działa, a teraz mamy czas na popracowanie nad wydajnością, czytelnością, dobrymi praktykami pisania kodu, itd.
Zadanie 3. Napiszmy funkcję, która oblicza  n -ty wyraz ciągu Fibonacciego z wykorzystaniem techniki TDD.

Definicja. Ciągiem Fibonacciego nazywamy ciąg liczb naturalnych, określony rekurencyjnie w następujący sposób

pierwszy wyraz jest równy  0 , drugi jest równy  1 , a każdy następny jest sumą dwóch poprzednich.

Możemy powyższą definicję określić wzorem następująco
Fn=⎧⎩⎨0, dla n=0,1, dla n=1,Fn−1+Fn−2, dla n>1. 

Założenia dla naszego rozwiązania.

Możemy otrzymać jedynie liczbę (tzn. formularz odrzuca wartości tekstowe).
Kryteria dla naszej funkcji.

Dla  n=0  zwracamy 0 (corner case).
Dla  n=1  zwracamy 1 (corner case).
Dla  n>1  zwracamy sumę dwóch poprzednich wyrazów (middle case).
Jeśli  n∉N∪{0} , (ten zapis oznacza, że  n  nie jest liczbą naturalną ani nie jest zerem, czyli może być liczbą ujemną, ułamkiem lub liczbą niewymierną), to zwracamy liczbę  −1 . To nie ma związku z wzorem na ciąg Fibonacciego, sami ustaliliśmy sobie, że w przypadku, w którym wzór nie działa zwracamy  −1 .
Faza czerwona: napisanie testów i zrozumienie funkcjonalności
[ ]
def test():
  # przypadki standardowe
  assert fibonacci(n=0) == 0
  assert fibonacci(n=1) == 1
  assert fibonacci(n=1.0) == 1
  assert fibonacci(n=7) == 13

  # obsługa argumentów, dla których nie liczymy wartości
  assert fibonacci(n=0.5) == -1
  assert fibonacci(n=-10) == -1

# test()  # nie ma sensu wywoływać funkcji test(), bo będzie czerwono :)
Faza zielona: zaimplementowanie funkcjonalności i spełenienie testów
[ ]
# Faza zielona
def fibonacci(n: int) -> int:
  if n < 0 or not int(n) == n :  # jeśli n jest ujemne lub nie jest całkowite to zwracamy -1
    return -1

  if n == 0:
    return 0

  if n == 1:
    return 1

  return fibonacci(n=n-1) + fibonacci(n=n-2)


test()
Faza refaktoru: polepszenie jakości rozwiązania
Tutaj trudno o jednoznaczny przepis. Na pewno, z rzeczy, które możemy i powinniśmy zrobić, to jest dbałość o dobre praktyki programowania, tj. odpowiednie formatowanie, dodanie komentarzy do bardziej złożonych fragmentów rozwiązania, dodanie docstringów, itp.

Natomiast w tej fazie możemy również starać się o polepszenie ogólnej jakości kodu, ale tego nie da się generalizować, w zależności od środowiska, w którym ten kod będzie działał wymagania jakości mogą się znacząco różnić (np. niektórzy wymagają szybkiego kodu, a inni kodu, który wykorzystuje niewielką ilość pamięci).

W naszym przykładzie, oprócz standardowych reguł dbałości o kod, skupimy się na czasie obliczanie kolejnych wyrazów ciągu.

[ ]
%timeit fibonacci(n=30)
account_circle
384 ms ± 8.08 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
[ ]
FIB = {}


def fibonacci(n: int) -> int:
  """
  Computes the n-th element of the Fibonacci sequence.

  Args:
    n (int): the element of the Fibonacci sequence which will be evaluated.

  Returns:
    int: the n-th element the Fibonacci sequence.
  """
  if n < 0 or not int(n) == n :  # jeśli n jest ujemne lub nie jest całkowite to zwracamy -1
    return -1

  if not n in FIB:
      if n == 0 or n == 1:  # te wartości pochodzą z definicji
        value = n
      else:
        value = fibonacci(n=n-1) + fibonacci(n=n-2)
      FIB[n] = value

  return FIB[n]


test()
[ ]
%timeit fibonacci(n=30)
account_circle
163 ns ± 15.7 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
[ ]
print(f"Improvement: {384 * 1_000_000 / 163:0.2f}")
account_circle
Improvement: 2355828.22
[ ]
from functools import cache


@cache
def fibonacci(n: int) -> int:
  """
  Computes the n-th element of the Fibonacci sequence.

  Args:
    n (int): the element of the Fibonacci sequence which will be evaluated.

  Returns:
    int: the n-th element the Fibonacci sequence.
  """
  if n < 0 or not int(n) == n :  # jeśli n jest ujemne lub nie jest całkowite to zwracamy -1
    return -1

  if n == 0 or n == 1:  # te wartości pochodzą z definicji
    return n

  return fibonacci(n=n-1) + fibonacci(n=n-2)


test()
[ ]
%timeit fibonacci(n=30)
account_circle
135 ns ± 13.5 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
[ ]
print(f"Improvement: {384 * 1_000_000 / 137:0.2f}")
account_circle
Improvement: 2802919.71
Платные продукты Colab - Отменить подписку

#%%
TDD (Test-Driven Development)
TDD jest techniką pisania oprogramowania (nie jest to technika pisania testów), w której główną ideą jest rozpoczęscie prac programistycznych od napisania zbioru testów do jeszcze nieistniejącej funkcjonalności, a dopiero potem napisanie kodu implementującego tę funkcjonalność.

TDD nie jest jedyną słuszną techniką tworzenia oprogramowania. Alternatywnie można pisać testy równolegle z pisaniem kodu lub można je pisać po skończeniu implementacji rozwiązania (ale to nie jest już TDD, w TDD testy pojawiają się zawsze przed rozpoczęciem kodowania).

Cykle w TDD
Faza czerwona: napisanie i uruchomienie testów. Pierwszym krokiem w TDD jest stworzenie scenariuszy testowych (napisanie testów) i włączenie ich. Oczywiście testowanie zakończy się niepowodzeniem, bo testowana funkcjonalność jeszcze nie istnieje.
Faza zielona: napisanie minimalnej ilości kodu, pozwalającego na dostarczenie funkcjonalności. W tym miejscu testy powinny przechodzić, a więc kolor czerwony (błędy asercji) zmieniają się na kolor zielony. W tej fazie cyklu nie musimy pisać genialnego kodu, chodzi nam o rozwiązanie, które spełnia wymogi testowe.
Faza refaktoru: w tym kroku robimy tak, żeby nasz kod jednak był genialny, tzn. testy już przechodzą, mamy funkcjonalność i rozumiemy jak ona działa, a teraz mamy czas na popracowanie nad wydajnością, czytelnością, dobrymi praktykami pisania kodu, itd.
Zadanie 3. Napiszmy funkcję, która oblicza  n -ty wyraz ciągu Fibonacciego z wykorzystaniem techniki TDD.

Definicja. Ciągiem Fibonacciego nazywamy ciąg liczb naturalnych, określony rekurencyjnie w następujący sposób

pierwszy wyraz jest równy  0 , drugi jest równy  1 , a każdy następny jest sumą dwóch poprzednich.

Możemy powyższą definicję określić wzorem następująco
Fn=⎧⎩⎨0, dla n=0,1, dla n=1,Fn−1+Fn−2, dla n>1. 

Założenia dla naszego rozwiązania.

Możemy otrzymać jedynie liczbę (tzn. formularz odrzuca wartości tekstowe).
Kryteria dla naszej funkcji.

Dla  n=0  zwracamy 0 (corner case).
Dla  n=1  zwracamy 1 (corner case).
Dla  n>1  zwracamy sumę dwóch poprzednich wyrazów (middle case).
Jeśli  n∉N∪{0} , (ten zapis oznacza, że  n  nie jest liczbą naturalną ani nie jest zerem, czyli może być liczbą ujemną, ułamkiem lub liczbą niewymierną), to zwracamy liczbę  −1 . To nie ma związku z wzorem na ciąg Fibonacciego, sami ustaliliśmy sobie, że w przypadku, w którym wzór nie działa zwracamy  −1 .

#%%

def test():
  # przypadki standardowe
  assert fibonacci(n=0) == 0
  assert fibonacci(n=1) == 1
  assert fibonacci(n=1.0) == 1
  assert fibonacci(n=7) == 13

  # obsługa argumentów, dla których nie liczymy wartości
  assert fibonacci(n=0.5) == -1
  assert fibonacci(n=-10) == -1

# test()  # nie ma sensu wywoływać funkcji test(), bo będzie czerwono :)
  
#%%
  # Faza zielona
def fibonacci(n: int) -> int:
  if n < 0 or not int(n) == n :  # jeśli n jest ujemne lub nie jest całkowite to zwracamy -1
    return -1

  if n == 0:
    return 0

  if n == 1:
    return 1

  return fibonacci(n=n-1) + fibonacci(n=n-2)


test()

#%%

### Faza refaktoru: polepszenie jakości rozwiązania
Tutaj trudno o jednoznaczny przepis. Na pewno, z rzeczy, które możemy i powinniśmy zrobić, to jest dbałość o dobre praktyki programowania, tj. odpowiednie formatowanie, dodanie komentarzy do bardziej złożonych fragmentów rozwiązania, dodanie docstringów, itp.

Natomiast w tej fazie możemy również starać się o polepszenie ogólnej jakości kodu, ale tego nie da się generalizować, w zależności od środowiska, w którym ten kod będzie działał wymagania jakości mogą się znacząco różnić (np. niektórzy wymagają szybkiego kodu, a inni kodu, który wykorzystuje niewielką ilość pamięci).

W naszym przykładzie, oprócz standardowych reguł dbałości o kod, skupimy się na czasie obliczanie kolejnych wyrazów ciągu.

Faza refaktoru: polepszenie jakości rozwiązania
Tutaj trudno o jednoznaczny przepis. Na pewno, z rzeczy, które możemy i powinniśmy zrobić, to jest dbałość o dobre praktyki programowania, tj. odpowiednie formatowanie, dodanie komentarzy do bardziej złożonych fragmentów rozwiązania, dodanie docstringów, itp.

Natomiast w tej fazie możemy również starać się o polepszenie ogólnej jakości kodu, ale tego nie da się generalizować, w zależności od środowiska, w którym ten kod będzie działał wymagania jakości mogą się znacząco różnić (np. niektórzy wymagają szybkiego kodu, a inni kodu, który wykorzystuje niewielką ilość pamięci).

W naszym przykładzie, oprócz standardowych reguł dbałości o kod, skupimy się na czasie obliczanie kolejnych wyrazów ciągu.

#%%
%timeit fibonacci(n=30)

384 ms ± 8.08 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

#%%

FIB = {}


def fibonacci(n: int) -> int:
  """
  Computes the n-th element of the Fibonacci sequence.

  Args:
    n (int): the element of the Fibonacci sequence which will be evaluated.

  Returns:
    int: the n-th element the Fibonacci sequence.
  """
  if n < 0 or not int(n) == n :  # jeśli n jest ujemne lub nie jest całkowite to zwracamy -1
    return -1

  if not n in FIB:
      if n == 0 or n == 1:  # te wartości pochodzą z definicji
        value = n
      else:
        value = fibonacci(n=n-1) + fibonacci(n=n-2)
      FIB[n] = value

  return FIB[n]


test()

%timeit fibonacci(n=30)

163 ns ± 15.7 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

print(f"Improvement: {384 * 1_000_000 / 163:0.2f}")

Improvement: 2355828.22

#%%

from functools import cache


@cache
def fibonacci(n: int) -> int:
  """
  Computes the n-th element of the Fibonacci sequence.

  Args:
    n (int): the element of the Fibonacci sequence which will be evaluated.

  Returns:
    int: the n-th element the Fibonacci sequence.
  """
  if n < 0 or not int(n) == n :  # jeśli n jest ujemne lub nie jest całkowite to zwracamy -1
    return -1

  if n == 0 or n == 1:  # te wartości pochodzą z definicji
    return n

  return fibonacci(n=n-1) + fibonacci(n=n-2)


test()


%timeit fibonacci(n=30)

135 ns ± 13.5 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)

print(f"Improvement: {384 * 1_000_000 / 137:0.2f}")

Improvement: 2802919.71
#%%

Napisz funkcję capital_indexes. Funkcja powinna przyjmować jeden parametr, który jest napisem. Twoja funkcja powinna zwracać indeksy wszystkich znaków (liter), które są wielkie.

Przykład. Dla słowa HeLlO funkcja powinna zwrócić listę [0, 2, 4].

#%%

Napisz funkcję is_prime, która przyjmuje jeden argument  n , który jest liczbą naturalną większą od zera. Funkcja ma zwrócić wartość True jeśli liczba jest pierwsza, a False w przeciwnym wypadku.

Przykład. Dla  n=5  funkcja powinna zwrócić True, a dla  n=4  funkcja powinna zwrócić wartość False.

#%%

def is_prime(n: int) -> bool:
  if n <= 1:
    return False

  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:  # sprawdzamy czy reszta z dzielenie n przez i wynosi 0
      return False

  return True


assert is_prime(n=1) is False
assert is_prime(n=12) is False
assert is_prime(n=2) is True
assert is_prime(n=11) is True


#%%
Rodzaje testów
Testy techniczne
Testy jednostkowe (unitowe)

#%%





