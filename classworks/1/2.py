def time_to_seconds(weeks, days, hours, minutes, seconds):
    return (
        (weeks * 7 * 24 * 60 * 60)
        + (days * 24 * 60 * 60)
        + (hours * 60 * 60)
        + (minutes * 60)
        + seconds
    )


print(bin(time_to_seconds(11, 2, 5, 32, 7))[2:])
