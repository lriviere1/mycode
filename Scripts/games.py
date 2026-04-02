def ask_yes_no(question):
    response = input(question).lower()
    while response not in ("y", "n"):
        print("Please enter 'y' or 'n'")
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except ValueError:
            print("Enter a valid number.")
    return response