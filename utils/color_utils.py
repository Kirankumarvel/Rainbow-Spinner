import random

def generate_gradient_colors(num_colors):
    """Generate a rainbow gradient with the specified number of colors"""
    colors = []
    for i in range(num_colors):
        # Calculate RGB values for rainbow colors
        r = int(max(0, 255 * (1 - abs((i / num_colors) * 6 - 3) / 3)))
        g = int(max(0, 255 * (1 - abs((i / num_colors) * 6 - 2) / 3)))
        b = int(max(0, 255 * (1 - abs((i / num_colors) * 6 - 4) / 3)))
        colors.append((r/255, g/255, b/255))  # Normalize to 0-1 for turtle
    return colors

def random_pastel_color():
    """Generate a random pastel color"""
    return (
        random.random() * 0.5 + 0.5,
        random.random() * 0.5 + 0.5,
        random.random() * 0.5 + 0.5
    )