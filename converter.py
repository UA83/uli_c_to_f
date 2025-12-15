def celsius_to_fahrenheit(celsius: float) -> float:
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def main():
    print("--- Celsius to Fahrenheit Converter ---")
    user_input = input("Enter temperature in Celsius: ")
    
    try:
        celsius = float(user_input)
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
    except ValueError:
        print("Error: Please enter a valid number.")

if __name__ == "__main__":
    main()
