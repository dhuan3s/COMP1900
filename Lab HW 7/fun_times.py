def time_difference(time1, time2):
    # split times into components
    t1_parts = time1.split(":")
    t2_parts = time2.split(":")

    hours1 = int(t1_parts[0])
    minutes1 = int(t1_parts[1])
    seconds1 = int(t1_parts[2])

    hours2 = int(t2_parts[0])
    minutes2 = int(t2_parts[1])
    seconds2 = int(t2_parts[2])

    # subtract seconds
    seconds_diff = seconds2 - seconds1
    if seconds_diff < 0:
        seconds_diff += 60
        minutes2 -= 1

    # subtract minutes
    minutes_diff = minutes2 - minutes1
    if minutes_diff < 0:
        minutes_diff += 60
        hours2 -= 1

    # subtract hours
    hours_diff = hours2 - hours1

    # format with leading zeros
    if hours_diff < 10:
        hours_str = "0" + str(hours_diff)
    else:
        hours_str = str(hours_diff)

    if minutes_diff < 10:
        minutes_str = "0" + str(minutes_diff)
    else:
        minutes_str = str(minutes_diff)

    if seconds_diff < 10:
        seconds_str = "0" + str(seconds_diff)
    else:
        seconds_str = str(seconds_diff)

    return hours_str + ":" + minutes_str + ":" + seconds_str

print(time_difference('07:00:00', '07:00:00'))
print(time_difference('12:08:12', '14:32:50'))
print(time_difference('17:30:18', '18:50:03'))
print(time_difference('17:30:08', '21:19:33'))
print(time_difference('21:58:59', '22:03:12'))
print(time_difference('22:59:59', '23:00:00'))