import pytest
from unittest.mock import Mock

import sys
# insert at 1, 0 is the script path (or '' in REPL)
if not '../bitops' in sys.path:
    sys.path.insert(1, '../bitops')


from bitops.BinaryOperations import get_bit, set_bit, clear_bit, get_bit_range_as_int, ENDIANNESS

class TestBinaryOperations:
    def test_get_bit_ok(self):
        assert 1 == get_bit(0x0F, 2)
        assert 0 == get_bit(0x0F, 7)
        assert 1 != get_bit(0x0F, 2, endiannes=ENDIANNESS.LITTLE)
        assert 0 != get_bit(0x0F, 7, endiannes=ENDIANNESS.LITTLE)

        assert 1 == get_bit(0x01, 0)
        assert 1 == get_bit(0x02, 1)
        assert 1 == get_bit(0x04, 2)
        assert 1 == get_bit(0x08, 3)
        assert 1 == get_bit(0x10, 4)
        assert 1 == get_bit(0x20, 5)
        assert 1 == get_bit(0x40, 6)
        assert 1 == get_bit(0x80, 7)

        assert 1 == get_bit(0x01, 7, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x02, 6, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x04, 5, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x08, 4, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x10, 3, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x20, 2, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x40, 1, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x80, 0, endiannes=ENDIANNESS.LITTLE)

    def test_get_bit_wrong_input(self):
        with pytest.raises(ValueError):
            assert 1 == get_bit(0xFF, 8)
            
        with pytest.raises(ValueError):
            assert 1 == get_bit(None, 4)

        with pytest.raises(ValueError):
            assert 1 == get_bit(0x12, None)

    def test_get_bit_long_input(self):
        assert 1 == get_bit(0x11223344556677889900000000FF01, 0)
        assert 0 == get_bit(0x11223344556677889900000000FF00, 0)
        assert 1 == get_bit(0x11223344556677889900000000FF11, 3, endiannes=ENDIANNESS.LITTLE)
        assert 0 == get_bit(0x01223344556677889900000000FF11, 3, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x01223344556677889900000000FF11, 19, endiannes=ENDIANNESS.LITTLE)
        assert 0 == get_bit(0x01222344556677889900000000FF11, 19, endiannes=ENDIANNESS.LITTLE)
        assert 1 == get_bit(0x01223344556677889901000000FF11, 40)
        assert 0 == get_bit(0x01222344556677889900000000FF11, 40)


    def test_set_bit_ok(self):
        assert 0x04 == set_bit(0x00, 2)
        assert 0xFF == set_bit(0x7F, 7)
        assert 0x0800007F == set_bit(0x7F, 27)
        assert 0x20 == set_bit(0x00, 2, endiannes=ENDIANNESS.LITTLE)
        assert 0xFF == set_bit(0xFE, 7, endiannes=ENDIANNESS.LITTLE)
        assert 0x10000001 == set_bit(0x10000000, 31, endiannes=ENDIANNESS.LITTLE)
        assert 0xFF == set_bit(0x7F, 7)
        assert 0x20 == set_bit(0x00, 2, endiannes=ENDIANNESS.LITTLE)
        assert 0xFF == set_bit(0xFE, 7, endiannes=ENDIANNESS.LITTLE)


    def test_set_bit_wrong_input(self):
        with pytest.raises(ValueError):
            set_bit(None, 4)

        with pytest.raises(ValueError):
            set_bit(0x12, None)

    def test_clear_bit_ok(self):
        assert 0x00 == clear_bit(0x04, 2)
        assert 0x7F == clear_bit(0xFF, 7)
        assert 0x00 == clear_bit(0x20, 2, endiannes=ENDIANNESS.LITTLE)
        assert 0xFE == clear_bit(0xFF, 7, endiannes=ENDIANNESS.LITTLE)


    def test_clear_bit_wrong_input(self):
        with pytest.raises(ValueError):
            clear_bit(0xFF, 8)

        with pytest.raises(ValueError):
            clear_bit(None, 4)

        with pytest.raises(ValueError):
            clear_bit(0x12, None)


    def test_get_bit_range_as_int(self):
        assert 7 == get_bit_range_as_int(0x07, 0, 3)
        assert 1 == get_bit_range_as_int(0x80, 7, 8)
        assert 8 == get_bit_range_as_int(0x80, 4, 8)
        assert 2 == get_bit_range_as_int(0x80, 6, 8)
        assert 3 == get_bit_range_as_int(0xFF, 6, 8)
