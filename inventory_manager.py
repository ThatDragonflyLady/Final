from itertools import product
from operator import pos

import models 
from models import Product
def add_product(products, pid, name, cat, qty, r_lvl, r_qty, price, vid):
    new_prod = Product(pid, name, cat, qty, r_lvl, r_qty, price, vid)
    products.append(new_prod)

def add_vendor(vendors, vid, name, contact, email, address):
    new_vendor = Product.Vendor(vid, name, contact, email, address)
    vendors.append(new_vendor)

def add_purchase_order(pos, po_num, vid, date, items, total, status):
    new_po = Product.PurchaseOrder(po_num, vid, date, items, total, status)
    pos.append(new_po)

def process_shipment(po_num, pos, products):
    for po in pos:
        if po.po_num == po_num:
            if po.status == "Received":
                return "Error: Already received."
            for item in po.items:
                for prod in products:
                    if prod.pid == item['pid']:
                        prod.quantity += item['qty']
            
            po.status = "Received"
            return "Shipment processed successfully."
    return "Order not found."

def search_by_id(inventory, product_id):
    """Exact match for a specific Product ID."""
    return next((product for product in inventory if product.pid == product_id), None)

def search_by_name(inventory, search_term):
    """Partial string match; case-insensitive."""
    return [p for p in inventory if search_term.lower() in p.name.lower()]

def search_by_category(inventory, category_name):
    """Filters products by a specific category."""
    return [p for p in inventory if p.category.lower() == category_name.lower()]

def search_by_vendor(inventory, vendor_id):
    """Finds all products associated with a specific Vendor ID."""
    return [p for p in inventory if p.vendor_id == vendor_id]
