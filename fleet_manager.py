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

def main():
    
    names, ranks, divs, ids = start_database()
    my_name = "Peter"

    active = True
    while active:
        user_choice = display_menu(my_name)
        if user_choice == "1":
            print("\nViewing Crew Roster...(Function coming next)")
        elif user_choice == "2" :
            print("\nAdding New Member...(Function coming next)")
        elif user_choice =="3" :
            print("Exiting program.")
            active = False
        else:
            print("Invalid input, please try again.")
if __name__ == "__main__":
    main()
 
