def HDL_analysis(HDL_level):
        if HDL_level >= 60:
                return "Normal"
        elif 40 <= HDL_level < 60:
                return "Borderline low"
        else:
                return "Low"


def LDL_analysis(LDL_level):
        if LDL_level <= 130:
                return "Normal"
        elif 130 <= LDL_level < 159:
                return "Borderline high"
        elif 160 <= LDL_level < 189:
                return "High"
        else:
                return "Very high"


def cholesterol_analysis():
        print("Cholesterol Analysis")
        HDLinput = input("Enter test result: ")
        test_info = HDLinput.split("=")
        if test_info[0] == "HDL":
                answer = HDL_analysis(int(test_info[1]))
                print("The level is {}".format(answer))
        elif test_info[0] == "LDL":
                answer = LDL_analysis(int(test_info[1]))
                print("The level is {}".format(answer))
        else:
                print("Test not recognized")


def new_feature():
        pass


def name_function():
        first_name = input("First name: ")
        last_name = input("Last name: ")
        return first_name, last_name


def interface():
        while True:
                print("Cholesterol Calculator")
                print("Options: ")
                print(" 1 - Cholesterol Analysis")
                print(" 9 - Quit")
                choice = input("Enter your options: ")
                if choice == "9":
                        return
                elif choice == "1":
                        cholesterol_analysis()


def fever_check(temp_list):
        fever = False
        for temperature in temp_list:
                if temperature > 98.6:
                        fever = True
        return fever


if __name__ == "__main__":
        interface()
