while True:
    user_input=input("Wpisz liczbę: ")
    try:
        value = float(user_input)
        print("Podałeś liczbę {}, do trzeciej potęgi jej wartość={}".format(value,pow(value,3)))
    except ValueError:
        if user_input=="stop":
            break
        else:
            print("wprowadz liczbe a nie napis!")