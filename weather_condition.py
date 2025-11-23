def weather_season(season):
    if season=="autumn":
        print("Weather is cool and windy.")
    elif season=="spring":
        print("Weather is warm with flowers blooming.")
    else:
        print("Enter autumn or spring only.")
user_input= input("Enter season (autumn or spring)").lower().strip()
weather_season(user_input)