class Product:
    def __init__(self, pid, name, cat, qty, reorder_lvl, reorder_qty, price, vid, active=True):
        self.pid = pid
        self.name = name
        self.category = cat
        self.quantity = int(qty)
        self.reorder_level = int(reorder_lvl)
        self.reorder_qty = int(reorder_qty)
        self.price = float(price)
        self.vendor_id = vid
        self.active = active
        
    def to_dict(self):
        return self.__dict__


class Vendor:
    def __init__(self, vid, name, contact, email, address):
        self.vid = vid
        self.name = name
        self.contact = contact
        self.email = email
        self.address = address
        
    def to_dict(self):
        return self.__dict__


class PurchaseOrder:
    def __init__(self, po_num, vid, date, items, total, status="Pending"):
        self.po_num = po_num
        self.vid = vid
        self.date = date
        self.items = items
        self.total = total
        self.status = status

    def to_dict(self):
        return self.__dict__
            
            
            
            
        
        