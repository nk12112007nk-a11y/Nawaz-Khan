"""
Problem 37 [Conditional Statements / Mixed / Applied]
Given coordinates (x, y), determine which quadrant the point lies in
"""
def quadrant(x, y):
    if x == 0 and y == 0:
        return "Origin"
    elif x == 0:
        return "On Y-axis"
    elif y == 0:
        return "On X-axis"
    elif x > 0 and y > 0:
        return "Quadrant I"
    elif x < 0 and y > 0:
        return "Quadrant II"
    elif x < 0 and y < 0:
        return "Quadrant III"
    else:
        return "Quadrant IV"

if __name__ == "__main__":
    for x, y in [(3, 4), (-3, 4), (-3, -4), (3, -4), (0, 0)]:
        print(f"({x},{y}): {quadrant(x, y)}")
