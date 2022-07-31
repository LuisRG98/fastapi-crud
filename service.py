class InventoryService:

    inventory = {}

    def __init__(self):
        self.inventory = InventoryService.inventory

    def show_items(self):
        for item in self.inventory:
            self.inventory[item]
            return self.inventory

    def add_product(self, item_id, item):
        if item_id in self.inventory:
            return {"Error": "Item ID already exists."}
        self.inventory[item_id] = item
        return self.inventory[item_id]

    def update_product(self, item_id, item):
        if item_id not in self.inventory:
            return {"Error": "Item ID does not exists"}
        if item.name is not None:
            self.inventory[item_id].name = item.name

        if item.price is not None:
            self.inventory[item_id].price = item.price

        if item.brand is not None:
            self.inventory[item_id].brand = item.brand

        return self.inventory[item_id]
    
    def get_item(self, item_id):
        return self.inventory[item_id]

    def delete_item(self, item_id):
        if item_id not in self.inventory:
            return {"Error": "Item does not exists"}

        del self.inventory[item_id]
        return {"Success": "Item deleted"}
