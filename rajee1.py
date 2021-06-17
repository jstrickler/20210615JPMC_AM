ctemps = [-40, 0, 37, 75, 100]
#farenheit_gen= (for f in ctemps)
for celsius in ctemps:
    fahrenheit= ((9*celsius)/5)+32
    #print("Temperature coverted form Celsius to Farenheit for f"{i}" is: f"{F}")
    #print("{:.1f} C is {:.1f} F".format(celsius,fahrenheit))
    # print(f"{celsius: .1f}" " C is " f"{fahrenheit}" " F")
    s = f"{celsius:5.1f} C is {fahrenheit:5.1f} F"
    print(s)
