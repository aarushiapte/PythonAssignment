#regex
#Q1
import re
def checkDate(date):
    if re.match(
            r'(January?|February?|March?|April?|May|June?|July?|August?|September?|October?|November?|December?)\s+\d{2,2},\s+\d{4}',
            date):
        return True
    else:
        return False


print(checkDate('June 10, 2021'))

#Q2
import re
valid1 = r"^[349][\d]{3}(-[\d]{4}){3}$"
def checkNumber(num):

        if re.match(valid1, num):
            print("Valid card number")
        else:
            print("Invalid card number")

print(checkNumber("3456-8798-7685-8345"))


