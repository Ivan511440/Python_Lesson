MSG_INPUT_NUMBER = 'Введите число: '
MSG_PRIME = 'Простое.'
MSG_COMPOSITE = 'Состовное'
MSG_NOT_PRIME = 'Не простое'
RANGE = 100_000 + 1

def is_prime(number) -> str:
    """Проверяет простое ли число"""
    if number in (0, 1):
        return MSG_NOT_PRIME
    
    for d in range(2, int(number ** 0.5) + 1):
        if not number % d:
            return MSG_COMPOSITE
        
    return MSG_PRIME


def check_range_number(number) -> bool:
    """Проверяет лежит ли число в диапазоне"""
    return True if number in range(RANGE) else False


def input_number() -> int:
    """Вводит число"""
    try:
        number = int(input(MSG_INPUT_NUMBER))
        
    except ValueError:
        return input_number()
    
    return number if check_range_number(number) else input_number()


def main() -> None:
    """Основная функция"""
    number = input_number()
    print(is_prime(number))


if __name__ == '__main__':
    main()
    


