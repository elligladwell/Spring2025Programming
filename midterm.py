#Name: Elli Gladwell
#UID: U1335224
#Source Statement: the resources I used for this project were ChatGPT and a friend of mine. My friend graduated in Computer Science so he was a lot of help. I used ChatGPT mostly to generate the books I used as opposed to thinking of them all myself. My friend was the greatest help to me, though. I feel that in the past assignments I have been mostly successful because they give step-by-step instructions in tandem with the textbook. Trying to remember everything and apply it on my own proved very difficult and I needed my friend to walk me through a lot of it.
import csv

#A simple function to display the Main Menu
def displayMenu():
    print("\nMain Menu:")
    print("1. Display all books")
    print("2. Find a book")
    print("3. Review book stats")
    print("4. Exit the program")

#A simple function to display all books in the csv file
def displayAllBooks():
    booksF = open('books.csv', 'r') #opens and reads the csv file and stores all the data in a variable called 'booksF'
    print("displaying books...")
    print(booksF.read()) #reads the data and prints all of it

### FIND A BOOK ####

#A simple function to display the search Menu
def displayFindMenu():
    print("\nSearch Menu:")
    print("1. Find books by title")
    print("2. Find books by Author Name")
    print("3. Find books by Publication Year")
    print("4. Find books by Genre")
    print("5. Go back to main menu")

#Function to find a book based on a given title
def findTitle(title):
    results = [] #stores results in an array for exporting to a csv
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    print("Search Results: ")
    for row in reader: #loops through all the books in the csv file
        if row and row[0].strip().lower() == title: #row[0] means column 0, which is where the title's of books are stored
            print(", ".join(row)) 
            results.append(row) #appends the search result to the results array
    if not results:
        print("No book found with that title.")
    else:
        saveFile(results) #calls to saveFile with the results as a parameter to export the results as a csv file

#Function to find a book based on a given author
def findAuthor(author):
    results = []
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    print("Search Results: ")
    for row in reader:
        if row and row[1].strip().lower() == author: #row[1] is the columnn where author's are stored
            print(", ".join(row))
            results.append(row)
    if not results:
        print("No book found with that author.")
    else:
        saveFile(results)

#Function to find a book based on a given year
def findYear(year):
    results = []
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    print("Search Results: ")
    for row in reader:
        if row and row[2].strip().lower() == year:
            print(", ".join(row))
            results.append(row)
    if not results:
        print("No book found with that publication year.")
    else:
        saveFile(results)

#Function to find a book based on a given genre
def findGenre(genre):
    results = []
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    print("Search Results: ")
    for row in reader:
        if row and row[3].strip().lower() == genre:
            print(", ".join(row))
            results.append(row)
    if not results:
        print("No book found with that genre.")
    else:
        saveFile(results)
    
#saves and exports a csv file with the search results from the 'find' functions
def saveFile(results):
    while True:
        csvChoice = input("Would you like to save your search results as a CSV file? Enter Y/N: ").lower()
        if csvChoice == "y":
            print("Created a csv file named 'searchResults.csv'")
            saveF = open('searchResults.csv', 'w', newline='') #like bookF but instead this is in 'write' mode and uses the writer functions instead of reader functions
            writer = csv.writer(saveF)
            writer.writerows(results)
            break
        elif csvChoice == "n":
            print("No saving selected, returning to search menu...")
            break
        else:
            print("Must input 'Y' or 'N': ")

#A function that calls other 'find' functions depending on the menu input from displayFindMenu()
def findBook():
    while True:
        displayFindMenu()
        choice = input("choose an option 1-5: ")
        if choice == "1":
            title = input("Enter a title: ").strip().lower()
            findTitle(title)
        elif choice == "2":
            author = input("Enter an Author: ").strip().lower()
            findAuthor(author)
        elif choice == "3":
            year = input("Enter a publication year: ").strip().lower()
            findYear(year)
        elif choice == "4":
            genre = input("Enter a genre: ").strip().lower()
            findGenre(genre)
        elif choice == "5":
            print("Returning to Main Menu..")
            break
        else:
            print("Invalid choice, Please enter 1-5 only: ")
#########################

### Review Book Stats ###

def displayReviewMenu():
    print("\nStats Menu:")
    print("1. Number of books per genre")
    print("2. Book with the most words")
    print("3. Average word count of all books")
    print("4. Average word count by genre")
    print("5. Book with the most pages")
    print("6. Go back to main menu")

def booksPerGenre():
    genreCount = {} #dictionary
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    headers = next(reader) # Skips the column headers
    for row in reader:
        genre = row[3].strip().lower()
        genreCount[genre] = genreCount.get(genre, 0) + 1 #0 in the perenthesis is the default value of genreCount

    for genre, count in genreCount.items():
        print(f"{genre}: {count}")

def booksMostWords():
    wordCount = 0
    bookWithMostWords = ""
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    headers = next(reader) # Skips the column headers
    for row in reader:
        title = row[0].strip() #title is in column 0
        count = int (row[4].strip())
        if count > wordCount: #if the current wordCount is greater, then update the book with the highest count
            wordCount = count
            bookWithMostWords = title
    print(f"The book with most words is, {bookWithMostWords} ({wordCount} words)")

def averageCountAllBooks():
    wordCount = 0
    bookCount = 0#number of total books in the csv
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    headers = next(reader) # Skips the column headers
    for row in reader:
        count = int (row[4].strip())
        wordCount = wordCount + count
        bookCount += 1   # increment book Count by 1
    averageCount = round(wordCount / bookCount)
    print(f"Average word count of all books is {averageCount} words.")

def averageCountByGenre():
    wordCount = {}
    bookCount = {}
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    headers = next(reader) # Skips the column headers
    for row in reader:
        genre = row[3].strip().lower()
        count = int (row[4].strip())
        wordCount[genre] = wordCount.get(genre, 0) + count
        bookCount[genre] = bookCount.get(genre, 0) + 1
    print("Average word count by Genre: ")
    for genre in wordCount:
        averageCount = round(wordCount[genre] / bookCount[genre])
        print(f"{genre.capitalize()}: {averageCount} words.")

def booksMostPages():
    pageCount = 0
    bookWithMostPages = ""
    booksF = open('books.csv', 'r')
    reader = csv.reader(booksF)
    headers = next(reader) # Skips the column headers
    for row in reader:
        title = row[0].strip() #title is in column 0
        count = int (row[5].strip())
        if count > pageCount: #if the current wordCount is greater, then update the book with the highest count
            pageCount = count
            bookWithMostPages = title
    print(f"The book with most pages is, {bookWithMostPages} ({pageCount} pages)")

def reviewBook():
    while True:
        displayReviewMenu()
        choice = input("choose an option 1-6: ")
        if choice == "1":
            booksPerGenre()
        elif choice == "2":
            booksMostWords()
        elif choice == "3":
            averageCountAllBooks()
        elif choice == "4":
            averageCountByGenre()
        elif choice == "5":
            booksMostPages()
        elif choice == "6":
            print("Returning to Main Menu..")
            break
        else:
            print("Invalid choice, Please enter 1-5 only: ")


############################

def main():
    while True:
        displayMenu()
        choice = input("Choose an option 1-4: ")
        if choice == "1":
            displayAllBooks()
        elif choice == "2":
            findBook()
        elif choice == "3":
            reviewBook()
        elif choice == "4":
            print("Exiting Program...")
            break
        else:
            print("Invalid choice, Please enter 1-4 only: ")
main()
