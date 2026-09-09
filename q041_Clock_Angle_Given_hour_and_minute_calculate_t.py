"""
Problem 41 [Conditional Statements / Mixed / Applied]
Clock Angle : Given hour and minute, calculate the smaller angle between the two hands.
"""
def clock_angle(hour, minute):
    hour = hour % 12
    minute_angle = 6 * minute
    hour_angle = 30 * hour + 0.5 * minute
    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360 - angle)
    return angle

if __name__ == "__main__":
    for h, m in [(3, 0), (6, 30), (9, 15)]:
        print(f"{h}:{m:02d} -> Angle = {clock_angle(h, m):.2f} degrees")
