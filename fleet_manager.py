def start_database() :
    names = ["Picard", "Riker","Data", "Wolf", "Troy" ]
    ranks = ["Rank 1", "Rank 2","Rank 3", "Rank 4", "Rank 5"]
    divs  = ["Division A", "Division B", "Division C","Division D", "Division E"]
    ids   = ["001","002", "003", "004", "005"]

    print("Database Intialized.")
    return names, ranks,divs, ids

def display_menu(student_name):
    print(f"\n--- Fleet Manager: {student_name} ---")
    print("1. View Crew Roster")
    print("2. Add Member")
    print("3. Exit")

    choice = input ("Select an option: ")
    return choice

def add_member(names, ranks,divs, ids):
    print("\n___ Register New Member___")
    new_id = input("Enter ID number:")
    if new_id in ids:
        print("Error: This ID already exists!")
    else:
        new_name = input("Enter Name: ")
        new_rank = input("Enter Rank: ")
        new_div = input("Enter Division: ")
        names.append(new_name)
        ranks.append(new_rank)
        divs. append(new_div)
        ids. append(new_id)
        print(f"Success! {new_name} has been added.")


def main():

    names, ranks, divs, ids = start_database()
    my_name = "Peter"

    active = True
    while active:
        user_choice = display_menu(my_name)
        if user_choice == "1":
            print("\nViewing Crew Roster...(Function coming next)")
        elif user_choice == "2" :
            add_member(names, ranks, divs, ids)
        elif user_choice =="3" :
            print("Exiting program.")
            active = False
        else:
            print("Invalid input, please try again.")
if __name__ == "__main__":
    main()
 
