import re

def extract_dimensions(text):
    """Extract dimensions and units from the text."""
    # Regex patterns for various units
    patterns = {
        'cm': r'(\d+(\.\d+)?)\s*cm',
        'mm': r'(\d+(\.\d+)?)\s*mm',
        'inch': r'(\d+(\.\d+)?)\s*inch',
        'foot': r'(\d+(\.\d+)?)\s*foot',
        'metre': r'(\d+(\.\d+)?)\s*metre',
        'yard': r'(\d+(\.\d+)?)\s*yard',
        'kg': r'(\d+(\.\d+)?)\s*kg',
        'gram': r'(\d+(\.\d+)?)\s*gram',
        'ton': r'(\d+(\.\d+)?)\s*ton',
        'pound': r'(\d+(\.\d+)?)\s*pound',
        'watt': r'(\d+(\.\d+)?)\s*watt',
        'kilowatt': r'(\d+(\.\d+)?)\s*kilowatt',
        'kilovolt': r'(\d+(\.\d+)?)\s*kilovolt',
        'volt': r'(\d+(\.\d+)?)\s*volt',
    }
    
    dimensions = []
    
    for unit, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        for match in matches:
            dimensions.append((float(match[0]), unit))
    
    return dimensions

def map_entities(text, dimensions):
    """Maps extracted dimensions to entities like length, width, height, weight using keywords."""
    length = width = height = weight = None

    # Lowercase the text for easier keyword matching
    text = text.lower()
    
    # Define keywords to identify the type of dimension
    keywords = {
        'length': ['length', 'size', 'dimension', 'height'],
        'width': ['width'],
        'height': ['height'],
        'weight': ['weight', 'mass', 'ton', 'pound', 'kg', 'gram']
    }
    
    # Safely pop from dimensions list
    def safe_pop():
        return dimensions.pop(0) if dimensions else None
    
    # Assign dimensions based on keywords
    if any(keyword in text for keyword in keywords['length']):
        length = safe_pop()
    if any(keyword in text for keyword in keywords['width']):
        width = safe_pop()
    if any(keyword in text for keyword in keywords['height']):
        height = safe_pop()
    if any(keyword in text for keyword in keywords['weight']):
        weight = safe_pop()
    
    # Assign remaining dimensions if not already assigned
    while dimensions:
        if length is None:
            length = safe_pop()
        elif width is None:
            width = safe_pop()
        elif height is None:
            height = safe_pop()
        elif weight is None:
            weight = safe_pop()
        else:
            break
    
    # Ensure all dimensions are tuples
    def ensure_tuple(value):
        if value is not None and not isinstance(value, tuple):
            return (value[0], value[1])
        return value
    
    length = ensure_tuple(length)
    width = ensure_tuple(width)
    height = ensure_tuple(height)
    weight = ensure_tuple(weight)
    
    return length, width, height, weight
