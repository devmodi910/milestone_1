MENU_PROMPT = "\nEnter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit:"
movies = []

def add_movie():
    title = input("Enter the movie tite: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie year ")

    movies.append({
        'title':title,
        'director':director,
        'year':year

    })

def show_movies():
    pass

def find_movie():
    pass

def menu():
    selection = input(MENU_PROMPT)
    while selection!='q':
        if selection == 'a':
            add_movie()
        elif selection == 'l':
            show_movies()
        elif selection == 'f':
            find_movie()
        else:
            print("Unknown command ")
        selection = input(MENU_PROMPT)
menu()