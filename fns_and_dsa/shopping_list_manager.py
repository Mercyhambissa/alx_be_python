def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            # Prompt for and add an item
            Item = input("Enter the Item to add: ")
            shopping_list.append(Item)  
        elif choice == '2':
            # Prompt for and remove an item
            try: 
                Rinput = input("Enter the Item you want remove: ")
                shopping_list.remove(Rinput)
                print(f"'{Rinput}' removed from shopping list.")
            except ValueError:
                print(f"Error: '{Rinput}' not found in shopping list.'")
        elif choice == '3':
            # Display the shopping list
            for i in range (len(shopping_list)):
                print(shopping_list[i])
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()