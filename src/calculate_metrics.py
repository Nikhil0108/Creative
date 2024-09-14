def calculate_area(width, height):
    """Calculates the area if width and height are provided."""
    if width and height:
        return width[0] * height[0], f"{width[1]}^2"
    return None, None

def calculate_volume(length, width, height):
    """Calculates volume based on length, width, and height."""
    if isinstance(length, tuple) and isinstance(width, tuple) and isinstance(height, tuple):
        return length[0] * width[0] * height[0], f"{length[1]}^3"
    else:
        # Handle cases where dimensions are not in tuple format
        return length * width * height, "unknown unit"


def format_weight(weight):
    """Formats weight for output."""
    if isinstance(weight, tuple):
        return f"{weight[0]} {weight[1]}"
    else:
        # Handle cases where weight is not in tuple format
        return f"{weight} unknown unit"
