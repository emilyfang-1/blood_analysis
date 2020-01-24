def cholesterol_analysis():
        print("Cholesterol Analysis")
        HDLinput = input("Enter test result: ")
        test_info = HDLinput.split("=")


def interface():
        while True:
                print("Cholesterol Calculator")
                print("Options: ")
                print("	9 - Quit")
                choice = input("Enter your options: ")
                if choice == "9":
                        return
                elif choice == "1":
                        cholesterol_analysis()
                        
	
if __name__ == "__main__":
        interface()
