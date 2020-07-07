from passwd import PasswordRequirements


def test_min_length():
    length_8 = PasswordRequirements(min_length=8)

    assert length_8.check("abcd1234")
    assert not length_8.check("abc123")

    # No minimum characters requirement if not specified
    assert PasswordRequirements().check("abc123")


def test_min_digits():
    digits_2 = PasswordRequirements(min_digits=2)

    assert not digits_2.check("abc")
    assert not digits_2.check("abc1")

    assert digits_2.check("abc12")
    assert digits_2.check("abc123")

def test_special_characters():
    special_1 = PasswordRequirements(min_special=1)

    assert special_1.check("abc$")
    assert special_1.check("abc$%^@*")

    assert not special_1.check("abc")
    assert not special_1.check("abc123")


def test_combinations():
    length_6_digits_3 = PasswordRequirements(min_length=6, min_digits=3)

    assert length_6_digits_3.check("abc123")

    assert not length_6_digits_3.check("ab123")
    assert not length_6_digits_3.check("abcd12")
    assert not length_6_digits_3.check("ab12")
