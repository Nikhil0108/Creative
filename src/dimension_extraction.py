import re

def extract_dimensions(text):
    """Extract dimensions and units from the text."""
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
