katz_deli = []

def line(katz_deli):
    if (len(katz_deli) == 0):
        print("The line is currently empty.")
    else:
        current_line_list = list()
        [current_line_list.append(f"{index + 1}. {name}") for index, name in enumerate(katz_deli)]
        current_line = " ".join(current_line_list)
        print(f"The line is currently: {current_line}")

    
def take_a_number(katz_deli, name):
    katz_deli.append(name)
    print(f"Welcome, {name}. You are number {len(katz_deli)} in line.")

def now_serving(katz_deli):
    for name in katz_deli:
        print(f"Currently serving {name}.")
        del(katz_deli[0])
        return katz_deli
    print("There is nobody waiting to be served!")
    