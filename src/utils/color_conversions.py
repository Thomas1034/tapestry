def dec2rgb(value: int) -> tuple[int, int, int]:
    """
    Converts a decimal value to an RGB tuple. Truncates values larger than 0xFFFFFF to their least significant 24 bits before conversion.
    :param color_code: A string representing a Java hexadecimal value (e.g., "0xRRGGBB").
    :return: A tuple (R, G, B) with RGB values in the range 0–255.
    """
    
    value = value & 0xFFFFFF

    r = (value >> 16) & 0xFF
    g = (value >> 8) & 0xFF
    b = (value) & 0xFF

    return (r, g, b)

def java2rgb(color_code):
    """
    Converts a Java hexadecimal value to an RGB tuple. Values larger than 0xFFFFFF are truncated to their least significant 24 bits before conversion.

    :param color_code: A string representing a Java hexadecimal value (e.g., "0xRRGGBB").
    :return: A tuple (R, G, B) with RGB values in the range 0–255.
    """
    
    # Strip off the 0x.
    color_code = color_code.lstrip("0x")
    
    return dec2rgb(int(color_code, 16))

def html2rgb(color_code):
    """
    Converts an HTML color code to an RGB tuple.

    :param color_code: A string representing an HTML color code (e.g., "#RRGGBB" or "#RGB", optionally leaving out the '#').
    :return: A tuple (R, G, B) with RGB values in the range 0–255.
    """
    
    # Strip off the #
    color_code = color_code.lstrip("#")

    # Special-case 3-digit short form (e.g., #RGB)
    if len(color_code) == 3:
        r, g, b = (int(color_code[i] * 2, 16) for i in range(3))
    # Handle 6-digit full format (e.g., #RRGGBB)
    elif len(color_code) == 6:
        r, g, b = (int(color_code[i:i+2], 16) for i in (0, 2, 4))
    else:
        raise ValueError("Invalid color code length. Must be 3 or 6 hexadecimal digits.")
    
    return r, g, b
