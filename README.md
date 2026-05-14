# Final
Project title: Final Inventory System
Project description: Python Final project is an inventory system
List of features: you can add and store your products, vendors names and contact into, how much inventory you have, when your inventory is low, and track your shipping.
List of Required Files:
file_manager.py 
inventory_manager.py
 main.py 
models.py,
 reports.py 
.json 
main.py is the file that runs the project

instructions for running the program:
Go to main.py and open and run the program
There are five choices you have to choose from:
Choice One: Product Management Prompts and stores product ID: Name: Category: Quantity: Reorder Level: Reorder Quantity: Price: Vendor ID:

Choice Two:Vendor Management Prompts and stores Vendor ID: Name: Contact: Email: Address: This section is only for vendor contact info

Choice Three: Purchase Orders Tracks and Stores Purchase Order Number: Vendor ID: Date (YYYY-MM-DD): Items_ordered: Total cost: Status:
Choice Four: Reports Creates a low stock report
Choice Five Exit: Exits the system and auto saves

Explanation of how Data is Stored: The data is stored using json flies  main_menu()  run the fm.load_data reads products.json, vendors.json, and pos.json.
im.add_product allows me to add the product using inventory_management I shortened inventory_ to im and file_management to fm 
fm.save_data()saves upon 5 Exiting
products.json: Stores Product objects (Product ID, Name, Category, Quantity, etc.).
vendors.json: Stores Vendor objects (Vendor ID, Name, Contact, Email, Address).
pos.json: Stores PurchaseOrder objects (PO Number, Vendor ID, Date, Items, Total, Status). [1, 2, 3, 4, 5]


Amanda Sprague
Class Python-54197




