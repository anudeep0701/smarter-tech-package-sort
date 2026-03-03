def sort(width, height, length, mass):
    """
    Dispatch a package to the correct stack based on size and mass.

    Bulky if:
      - volume >= 1,000,000 cm^3 OR
      - any dimension >= 150 cm
    Heavy if:
      - mass >= 20 kg

    Returns: "STANDARD", "SPECIAL", or "REJECTED"
    """
    bulky = (width * height * length >= 1_000_000) or (max(width, height, length) >= 150)
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    if bulky or heavy:
        return "SPECIAL"
    return "STANDARD"
