time = 7532

hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

time = f"{hours} Hours, {minutes} Minutes, and {seconds} Seconds"
print(time)