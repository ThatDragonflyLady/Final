def display_inventory(products):
    print(f"{'ID':<5} {'Name':<20} {'Stock':<8} Status")
    for p in products:
        status = "Active" if p.active else "Inactive"
        print(f"{p.pid:<5} {p.name:<20} {p.quantity:<8} {status}")

def vendors_report(vendors):
    print("--- VENDORS ---")
    for v in vendors:
        print(f"{v.vid}: {v.name} | Contact: {v.contact} | Email: {v.email} | Address: {v.address}")

def purchase_orders_report(pos):
    print("--- PURCHASE ORDERS ---")
    for po in pos:
        print(f"PO#: {po.po_num} | Vendor ID: {po.vendor_id} | Date: {po.date} | Total: ${po.total:.2f} | Status: {po.status}")

def low_stock_report(products):
    print("--- LOW STOCK ALERTS ---")
    for p in products:
        if p.quantity <= p.reorder_level:
            print(f"ALERT: {p.name} (Qty: {p.quantity} | Reorder at: {p.reorder_level})")
