#grading system using mutiple if-else


def grade(score):
    if score >=90:
        return "A"
    else:
        if score >=80:
            return "B"
        else:
            if score >=70:
                return "C"
            else:
                if score >=60:
                    return "D"
                else:
                    return "F"

def main():
    score = float(input("Enter the score"))
    print(grade(score))

if __name__ == "__main__":
    main()
