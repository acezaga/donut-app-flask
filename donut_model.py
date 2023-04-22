class DonutModel:
    donuts = [ # Assume this is our database table for now
        {"id": 1, "name": "choco waco", "flavor": "chocolate", "price": 1.50},
        {"id": 2, "name": "mango delight", "flavor": "mango", "price": 2.00},
        {"id": 3, "name": "strawberry shortcake", "flavor": "strawberry", "price": 3.00},
    ]

    def get_donuts(self, flavor=None):
        # Don't do business logic here
        if flavor:
            result_donuts = []
            for donut in self.donuts:
                if donut["flavor"] == flavor:
                    result_donuts.append(donut)
            return result_donuts

        return self.donuts
    
    def add_donut(self, name, flavor, price):
        last_id = self.donuts[-1]["id"]
        self.donuts.append({
            "id": last_id + 1,
            "name": name,
            "flavor": flavor,
            "price": price
        })
        return {
            "id": last_id + 1,
            "name": name,
            "flavor": flavor,
            "price": price
        }
    
    def update_donut(self, id, name, flavor, price):
        for donut in self.donuts:
            if donut["id"] == id:
                donut["name"] = name
                donut["flavor"] = flavor
                donut["price"] = price
                return donut
        return None
    
    def delete_donut(self, id):
        for index, donut in enumerate(self.donuts):
            if donut['id'] == id:
                self.donuts.pop(index)
                return True
        return False