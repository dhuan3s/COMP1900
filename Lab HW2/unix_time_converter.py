unix_time = int(input("Enter a Unix time: "))

days = unix_time // 86400
remainder = unix_time % 86400

hours = remainder // 3600
remainder = remainder % 3600

minutes = remainder // 60

seconds = remainder % 60
print(f"That is \n{days}d\n{hours}h \n{minutes}m \n{seconds}s\nsince midnight on January 1, 1970.")