# Custom Exception
class UserNotFoundException(Exception):
    def __init__(self, name):
        super().__init__(f"User '{name}' not found in the collection.")

# Function to search for a user
def search_user(collection, name_to_search):
    if name_to_search in collection:
        print(f"User '{name_to_search}' found in the collection.")
    else:
        raise UserNotFoundException(name_to_search)

if __name__ == "__main__":
    names_input = input("Enter names separated by commas: ")
    names_collection = [name.strip() for name in names_input.split(",")]

    name_to_search = input("Enter a name to search: ")

    try:
        search_user(names_collection, name_to_search)
    except UserNotFoundException as e:
        print(f" {e}")
