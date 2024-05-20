import sys
import atheris
from json import JSONDecodeError
from utils import is_expected_error


with atheris.instrument_imports():
    import jsonpickle

expected_errors = {
    "jsonpickle/unpickler.py": [
        ("object has no attribute 'split'", 283),
        ("not enough values to unpack", 283),
        ("object has no attribute 'split'", 197),
        ("object has no attribute 'encode'", 404),
        ("object has no attribute 'encode'", 407),
        ("object is not iterable", 448),
        ("list indices must be integers or slices", 539),
        ("object is not iterable", 481),
        ("object is not iterable", 448),
        ("object is not iterable", 808),
        ("object is not iterable", 859),
        ("unhashable type", 407),
        ("object argument after * must be an iterable", 493),
        ("No module named", 288),
        ("list index out of range", 160),
        ("'utf-8' codec can't encode character", 407),
        ("too many values to unpack", 283),
        ("object is not callable", 493),
    ],
    "base64.py": [
        ("bad base85 character at", -1),
        ("base85 overflow in hunk", -1),
        ("Invalid base64-encoded string", -1),
        ("Incorrect padding", -1),
    ],
}


def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    fuzz_string = fdp.ConsumeUnicodeNoSurrogates(
        fdp.ConsumeIntInRange(0, fdp.remaining_bytes())
    )

    try:
        jsonpickle.unpickler.decode(fuzz_string)
    except (RecursionError, JSONDecodeError):
        return -1
    except Exception as e:
        if is_expected_error(e, expected_errors):
            return 0
        raise e


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
