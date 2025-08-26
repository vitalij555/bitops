![Upload Python Package](https://github.com/vitalij555/bitops/workflows/Upload%20Python%20Package/badge.svg)
[![PyPi version](https://img.shields.io/pypi/v/bitops.svg?style=flat-square) ](https://pypi.python.org/pypi/bitops) [![Supported Python versions](https://img.shields.io/pypi/pyversions/bitops.svg?style=flat-square) ](https://pypi.org/project/bitops) [![License](https://img.shields.io/pypi/l/bitops.svg?style=flat-square) ](https://choosealicense.com/licenses) [![Downloads](https://pepy.tech/badge/bitops)](https://pepy.tech/project/bitops) [![codecov](https://codecov.io/gh/vitalij555/bitops/branch/master/graph/badge.svg)](https://codecov.io/gh/vitalij555/bitops)




# bitops — Tiny Python bit manipulation helpers

A lightweight set of utilities for common bit-twiddling tasks (get/set/clear bits, extract/set ranges, compute byte sizes), with **BIG** and **LITTLE** endianness support.

Works great as a foundation for parsers (e.g., BER-TLV, EMV) and binary protocols.

---

## Features

- \`ENDIANNESS\` enum (\`BIG\`, \`LITTLE\`)
- Bit queries: \`get_bit\`, \`is_bit_set\`
- Bit mutation: \`set_bit\`, \`clear_bit\`
- Ranged extraction & setting: \`get_bit_range_as_int\`, \`set_bit_range_from_int\`
- Utility: \`get_effective_length_in_bytes\` (how many bytes to represent an int)

---

## Install

```bash
pip install bitops


## Quick Start

```python
from bitops.BinaryOperations import (
    ENDIANNESS,
    get_bit, set_bit, clear_bit,
    get_bit_range_as_int, set_bit_range_from_int,
    get_effective_length_in_bytes
)

# Single-bit access (big-endian bit numbering)
assert get_bit(0x0F, 2) == 1
assert get_bit(0x0F, 7) == 0

# Little-endian bit numbering
assert get_bit(0x01, 7, endiannes=ENDIANNESS.LITTLE) == 1

# Set / clear
x = set_bit(0x00, 5)          # -> 0b0010_0000
y = clear_bit(0xFF, 7)        # -> 0b0111_1111

# Ranges: [start, end) half-open, bit 0 is LSB in big-endian numbering
v = get_bit_range_as_int(0b1110_0101, 2, 5)  # -> 0b101 = 5

# Set a range: insert value's bits starting at position 'pos'
z = set_bit_range_from_int(0x00, 2, 0b101)   # -> 0b0001_0100 (0x14)

# Byte width utility
assert get_effective_length_in_bytes(0x00) == 1
assert get_effective_length_in_bytes(0x1234) == 2
```


## API

`ENDIANNESS`

- `ENDIANNESS.BIG`: big-endian bit numbering in APIs (bit 0 is LSB, positions increment toward MSB).
- `ENDIANNESS.LITTLE`: mirrored bit positions across the byte width of the value.

Note: Functions take an integer `value`. For endianness handling, the code computes the width using `get_effective_length_in_bytes(value)`.

`get_effective_length_in_bytes(value: int) -> int`

Return minimal number of bytes required to represent `value`. Zero returns 1.

`is_bit_set(value: int, n: int, endiannes=ENDIANNESS.BIG) -> bool`

Return `True` if bit `n` is set under the specified endianness.

`get_bit(value: int, n: int, endiannes=ENDIANNESS.BIG) -> int`

Return the bit (0 or 1). Validates bounds and `None`.

`set_bit(value: int, n: int, endiannes=ENDIANNESS.BIG) -> int`

Return `value` with bit `n` set.

`clear_bit(value: int, n: int, endiannes=ENDIANNESS.BIG) -> int`

Return `value` with bit `n` cleared.

`get_bit_range_as_int(value: int, start: int, end: int, endiannes=ENDIANNESS.BIG) -> int`

Extract bits [start, end) as an integer. Validates bounds; supports LITTLE endianness via mirrored positions.

`set_bit_range_from_int(target_byte: int, pos: int, value: int, endiannes=ENDIANNESS.BIG) -> int`

Insert `value`’s bits into `target_byte` starting at bit position `pos` (honoring endianness).
Bounds are validated against the current byte-width of `target_byte`.


## Endianness Notes

- For `ENDIANNESS.BIG`, bit 0 is LSB; bit 7 is MSB (for a single byte). For multi-byte integers, bit positions continue upward.
- For `ENDIANNESS.LITTLE`, functions mirror positions across the computed width of `value`. E.g., in an 8-bit value, querying bit 0 (BIG) corresponds to bit 7 (LITTLE).


## Testing

This repo uses `pytest`.

```python
pip install -r requirements-dev.txt
pytest -v
```


## Error Handling

All APIs raise `ValueError` for:

- `value` or positions being `None`
- Bit indices out of current width for `value`
- Unknown endianness

Some parameter checks use `AssertionError` semantics (e.g., invalid ranges). You may later convert these to explicit `ValueError` for consistency.


## Versioning & Compatibility

- Python 3.8+
- No external dependencies


## Contributing

Issues and PRs are welcome! Please:

1. Open an issue to discuss larger changes
2. Add tests for new behavior
3. Run `pytest` locally before opening a PR



## License

MIT License — see `LICENSE`.



