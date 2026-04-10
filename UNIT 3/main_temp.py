from Temperature import cel_to_far
from Temperature import far_to_cel
from Temperature import cel_to_kel

def main():
    while True:
        print("\nTemperature Conversion Program.")
        print("1.Celsius to Fahrenheit.")
        print("2.Fahrenhiet to Celsius.")
        print("3.Celsius to Kelvin.")
        print("4.Exit.")

        try:
            choice = int(input("Enter your choice(1-4):"))

            if choice == 1:
                c = float(input("Enter Temperature in Celsius:"))
                print("Fahrenheit:", cel_to_far.convert(c))
            elif choice == 2:
                f = float(input("Enter Temperature in Fahrenheit:"))
                print("Celsius:", far_to_cel.convert(f))
            elif choice == 3:
                c = float(input("Enter Temperature in Celsius:"))
                print("Kelvin:", cel_to_kel.convert(c))
            elif choice == 4:
                print("Exiting Program...")
                break
            else:
                print("Invalid choice! Please try again.")
        except ValueError:
            print("Invalid value! Please enter numeric values.")
if __name__=="__main__":
    main()