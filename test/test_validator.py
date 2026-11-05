# tests/test_validator.py
from validator import validate_email, validate_phone, validate_snils


def test_validate_email():
    assert validate_email("test@example.com") == True
    assert validate_email("invalid") == False


def test_validate_phone():
    for phone in ("+79991234567", "79991234567", "+7 999-123-45-67"):
        assert validate_phone(phone)
    for phone in ("89991234567", "+7999123", "", "+79991234567\n", "+7٩٩٩١٢٣٤٥٦٧"):
        assert not validate_phone(phone)
    

def test_validate_snils():
    # Валидные СНИЛС (рассчитаны по алгоритму)
    assert validate_snils("11223344595") == True
    # 1*7 + 1*4 + 9*3 + 9*2 + 9*1 = 65, not 32 in the template.
    assert validate_snils("001-001-999 65") == True  # с форматированием
    assert validate_snils("001-001-999 32") == False
    
    # Невалидные: неверный формат
    assert validate_snils("123") == False              # слишком короткий
    assert validate_snils("123456789012") == False     # слишком длинный
    assert validate_snils("abcdefghijk") == False      # не цифры
    
    # Невалидные: неверная контрольная сумма
    assert validate_snils("11223344500") == False
