import inventory_manager as im
import file_manager as  fm
import reports
import models

class Product:
    pass

class Vendor:
    pass

class PurchaseOrder:
    pass

def main_menu():
    
    products = fm.load_data('products.json', Product)
    vendors = fm.load_data('vendors.json', Vendor)
    pos = fm.load_data('pos.json', PurchaseOrder)
    
    while True:
        print("\n---Inventory System---")
        print("1. Product Management")
        print("2. Vendor Management")
        print("3. Purchase Orders")
        print("4. Reports")
        print("5. Exit")
        
        choice = input("Select an option:")
        
        if choice == '1':
            pid = input("Product ID:")
            name = input("Name:")
            cat = input("Category:")
            qty = input("Quantity:")
            r_lvl = input("Reorder Level:")
            r_qty = input("Reorder Quantity:")
            price = input("Price:")
            vid = input("Vendor ID:")
            im.add_product(products, pid, name, cat, qty, r_lvl, r_qty, price, vid)
            reports.display_inventory(products)
            
        elif choice == '2':
            vid = input("Vendor ID:")
            name = input("Name:")
            contact = input("Contact:")
            email = input("Email:")
            address = input("Address:")
            im.add_vendor(vendors, vid, name, contact, email, address)
            reports.vendors_report(vendors)
            
        elif choice == '3':
            po_num = input("Purchase Order Number:")
            vid = input("Vendor ID:")
            date = input("Date (YYYY-MM-DD):")
            items = input("Items_ordered:")
            total = input("Total cost:")
            status = input("Status:")
            im.add_purchase_order(pos, po_num, vid, date, items, total, status)
            #result = im.process_shipment(po_num, pos, products)
            #print(result)
            reports.purchase_orders_report(pos)
        
        elif choice == '4':
            reports.low_stock_report(products)
            reports.display_inventory(products)
            
        elif choice == '5':
            fm.save_data('products.json', products)
            fm.save_data('vendors.json', vendors)
            fm.save_data('pos.json', pos)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()