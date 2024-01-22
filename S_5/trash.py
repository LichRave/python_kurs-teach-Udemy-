

#%%
class MyError(Exception):
    pass

if __name__ == '__main__':
    a = 5
    b = 0
    try:
        if b == 0:
            raise MyError('b nie może być zerem!')

        result = a / b
        print(f'result {result}')
    except MyError:
        print('Nie dziel przez zero!')
    finally:
        print('FINALLY')

print('KONIEC')

#%%

if __name__ == "__main__":
    a = 5
    b = 0
    try:
        result = a/b
        print(f"result{result}")
     except ValueError:
         print("no zero division!")
    finally:
        print("final")

print("end")

#%%

if __name__== 'main':
    a = 5
    b = 0
    try:
        result = a/b
        print(f'result{result}')
    except ValueError:
        print('nie dziel pprzez zero!')
    finally:
        print('FINALLY')

print('Koniec')

#%%

