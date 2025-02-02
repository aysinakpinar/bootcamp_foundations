def as_sun_lover(temp):
    if temp >= 25:
        return "great"
    else:
        return "not great"
    
def as_snow_lover(temp):
    if temp <= 0:
        return "great"
    else:
        return "not great"
    
def report_weather(temperature, for_person):
    return for_person(temperature)

print(report_weather(25, as_sun_lover))
print(report_weather(0, as_sun_lover))
print(report_weather(24, as_snow_lover))
print(report_weather(-2, as_snow_lover))