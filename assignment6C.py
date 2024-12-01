class EligibleforEntrance(Exception):
    pass

class NotEligibleforEntrance(Exception):
    pass

def check_eligibility():
    try:
        physics = int(input("Enter Physics marks: "))
        chemistry = int(input("Enter Chemistry marks: "))
        maths = int(input("Enter Maths marks: "))

        if physics < 55 or chemistry < 55 or maths < 55:
            raise NotEligibleforEntrance("Marks in one or more subjects are less than 45. Not eligible for entrance.")
        else:
            raise EligibleforEntrance("Congratulations! You are eligible for entrance.")

    except NotEligibleforEntrance as e:
        print(f"Exception: {e}")
    except EligibleforEntrance as e:
        print(f"Exception: {e}")
    except ValueError:
        print("Error: Please enter valid numeric marks.")

check_eligibility()