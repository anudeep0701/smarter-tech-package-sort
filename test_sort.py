from sort import sort

def run_tests():
    test_cases = [
        ((10, 10, 10, 1), "STANDARD"),
        ((10, 10, 10, 20), "SPECIAL"),
        ((100, 100, 100, 10), "SPECIAL"),   # bulky via volume (boundary)
        ((150, 10, 10, 10), "SPECIAL"),     # bulky via dimension (boundary)
        ((100, 100, 100, 20), "REJECTED"),  # bulky + heavy
        ((150, 10, 10, 20), "REJECTED"),    # bulky + heavy
        ((149.9, 10, 10, 19.9), "STANDARD") # just under thresholds
    ]

    for inputs, expected in test_cases:
        got = sort(*inputs)
        assert got == expected, f"Input {inputs} -> expected {expected}, got {got}"

    print("All tests passed!")


if __name__ == "__main__":
    run_tests()
