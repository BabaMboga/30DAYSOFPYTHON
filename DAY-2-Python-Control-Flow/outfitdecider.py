temperature = float(input("Enter the current temper in Fahrenheit: "))
raining = input("Is it currently raining? (yes/no): ").lower() == "yes"

def outfit_suggestion(temperature,raining):
    if temperature < 50:
        outfit = "coat, hat, scarf, and gloves"
    elif 50 <= temperature <= 70 and not raining:
        outfit = "sweater or light jacket"
    elif 50 <= temperature <=70 and raining:
        outfit = "rain jacket and boots"
    elif temperature > 70 and not raining:
        outfit = "t-shirt and shorts"
    elif temperature > 70 and raining:
        outfit = "light jacket and rain boots"
    else:
        outfit = "an outfit appropriate for the condiions"
    
    print("Based on the current weather condiotions, it is suggested to wear", outfit +  ".")

outfit_suggestion(temperature,raining)
