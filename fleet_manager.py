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
    print("2. Add Crew Member")
    print("3. Remove Crew Member" )
    print("4.Update Crew Rank")
    print("5. Search Crew Member")
    print("Filter by Division")
    print("7. Exit")
    return input ("Enter your choice :")

def display_roster(names, ranks,divs, ids):
    print("\n--- Current Fleet Roster ---")
    for i in range(len(names)):
        print(f"ID: {ids[i]} | Name: {names[i]} | Rank: {ranks[i]} | Div: {divs[i]}")
    print("-----------------------------")

def add_member(names, ranks, divs, ids):
    print("\n_ _ Register New Member_ _")
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

def remove_member(names, ranks, divds, ids):
    target_id = input("Enter ID of member to remove: ")
    if target_id not in ids:
        print("Error: ID not found in records. ")
        return
    idx = ids.index(target_id)
    del names[idx], ranks[idx], divds[idx], ids[idx]
    print("Crew member removed successfully!")

def update_rank(names, ranks, divs, ids):
    target_id = input("Enter ID of member to update rank: ")
    if target_id not in ids:
        print("Error: ID not found in records. ")
        return
    idx = ids. index(target_id)
    new_rank = input(f"Enter new rank for {names[idx]}: ")
    ranks[idx] = new_rank
    print(f"Success! {names[idx]}'s rank updated to {new_rank}.")

    def search_member (names, ranks, divs, ids):
        search_term  = input("Enter ID or name to search for a crew member : "). strip()
        found = False
        print("\n--- Search Results --- ")
        for i in range (len(ids)):
            if search_term == ids[i] or search_term.lower() in names[i].lower():
                print(f"ID: {ids[i]}")
                print(f"Name: {names[i]}")
                print(f"Rank: {ranks[i]}")
                print(f"Division: {divs[i]}")
                print("-----------------")
                found = True
        if not found:
            print("No crew members match your search.")

    def filter_by_division(names, ranks, divs, ids):
        target_div = input("Enter division to filter by: "). strip(). lower()
        found = False
        print(f"\'\n---Crew Members in  {target_div.title()} division ---")
        for i in range (len(divs)):
            if divs[i].lower() == target_div:
            print(f"ID: {ids[i]}")
            print(f"Name: {names[i]}")
            print(f"Rank: {ranks[i]}")
            print("----------------")
            found = True
        if not found:
            print(f"No crew found in {target_div.title()} division.")




 



def main():

    names, ranks, divs, ids = start_database()
    my_name = "Peter"

    active = True
    while active:
        user_choice = display_menu(my_name)
        if user_choice == "1":
            display_roster(names, ranks, divs, ids)
        elif user_choice == "2" :
            add_member(names, ranks, divs, ids)
        elif user_choice =="3" :
            remove_member(names, ranks, divs, ids)
        elif user_choice == "4" :
            update_rank(names, ranks, divs, ids)
        elif user_choice == "5" :
            search_member(names, ranks, divs, ids)
        elif user_choice == "6" :
            filter_by_division(names, ranks, divs, ids)
            print("Exiting program.")
            active = False
        else:
            print("Invalid input, please try again.")
if __name__ == "__main__":
    main()
 
