import sqlite3
def initializeDatabase():
    with sqlite3.connect("chocolate_house.db") as conn:
        cursor = conn.cursor()

       
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS seasonal_flavors (flavor_id INTEGER PRIMARY KEY AUTOINCREMENT,flavor_name TEXT NOT NULL,availability_period TEXT NOT NULL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ingredients (ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,ingredient_name TEXT NOT NULL,stock_quantity INTEGER NOT NULL
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customer_feedback (feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,customer_name TEXT NOT NULL,flavor_suggestion TEXT,allergy_concern TEXT
            )
        """)
        print("Database done successfully!")


def AddSeasonalFlavorzzzzzz():
    FlavorName = input("Enter the seasonal flavor name: ")
    availabili = input("Enter the availability period (e.g., Winter, Spring): ")
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO seasonal_flavors (flavor_name, availability_period)
            VALUES (?, ?)
        """, (FlavorName, availabili))
        connection.commit()
        print("Seasonal flavor added")

def AddIngredientsz():
    IngredientName = input("Enter the ingredient name: ")
    StockQuantity = int(input("Enter the stock quantity: "))
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO ingredients (ingredient_name, stock_quantity)
            VALUES (?, ?)
        """, (IngredientName, StockQuantity))
        connection.commit()
        print("Ingredient added ")

def AddCustFeedback():
    CustomerName = input("Enter your name: ")
    FlavorSuggestion = input("Enter your flavor suggestion: ")
    AllergyConcern = input("Do you have any allergy concerns? ")
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO customer_feedback (customer_name, flavor_suggestion, allergy_concern)
            VALUES (?, ?, ?)
        """, (CustomerName, FlavorSuggestion, AllergyConcern))
        connection.commit()
        print("Customer feedback added")

def ViewSeasnlFlavors():
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM seasonal_flavors")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def ViewIngredients():
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM ingredients")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

def ViewCustFeedback():
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM customer_feedback")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
def DelSeasonalFlavor():
    flavor_id = int(input("Enter the Flavor ID to delete: "))
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM seasonal_flavors WHERE flavor_id = ?", (flavor_id,))
        connection.commit()
        print("Seasonal flavor deleted successfully!")

def DelIngredient():
    ingredient_id = int(input("Enter the Ingredient ID to delete: "))
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM ingredients WHERE ingredient_id = ?", (ingredient_id,))
        connection.commit()
        print("Ingredient deleted successfully!")

def DelCustFeedback():
    feedback_id = int(input("Enter the Feedback ID to delete: "))
    with sqlite3.connect("chocolate_house.db") as connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM customer_feedback WHERE feedback_id = ?", (feedback_id,))
        connection.commit()
        print("Customer feedback deleted successfully!")

def MainMenu():
    while True:
        print("\nChocolate House")
        print("1. Add Seasonal Flavor")
        print("2. Add Ingredient")
        print("3. Add Customer Feedback")
        print("4. View Seasonal Flavors")
        print("5. View Ingredients")
        print("6. View Customer Feedback")
        print("7. Delete Seasonal Flavor")
        print("8. Delete Ingredient")
        print("9. Delete Customer Feedback")
        print("10. Exit")
        choice = input("Please select an option (1-10): ")
        if choice == '1':
            AddSeasonalFlavorzzzzzz()
        elif choice == '2':
            AddIngredientsz()
        elif choice == '3':
            AddCustFeedback()
        elif choice == '4':
            ViewSeasnlFlavors()
        elif choice == '5':
            ViewIngredients()
        elif choice == '6':
            ViewCustFeedback()
        elif choice == '7':
            DelSeasonalFlavor()
        elif choice == '8':
            DelIngredient()
        elif choice == '9':
            DelCustFeedback()
        elif choice == '10':
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please try again.")
initializeDatabase()
MainMenu()
