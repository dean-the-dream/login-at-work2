from screeninfo import get_monitors

monitor = 0
for m in get_monitors():
    if m.is_primary == True:
        monitor = m


win_y = 980
win_x = 700
screen_y = int(monitor.height)
screen_x = int(monitor.width)


x_start = (screen_x / 2) - (win_x / 2)
y_start = (screen_y / 2) - (win_y / 2)

print(f"({x_start},{y_start})")
print(screen_y)
