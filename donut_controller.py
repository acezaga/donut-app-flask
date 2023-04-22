from donut_model import DonutModel

class DonutController:
    def __init__(self, donut_model = None): # Dependency Injection
        self.donut_model = donut_model if donut_model is not None else DonutModel()

    def get_donuts(self, flavor=None):
        # You can perform additional filtering or business logic here
        return self.donut_model.get_donuts(flavor)
    
    def add_donut(self, name, flavor, price):
        return self.donut_model.add_donut(name, flavor, price)
    
    def update_donut(self, id, name, flavor, price):
        return self.donut_model.update_donut(id, name, flavor, price)
    
    def delete_donut(self, id):
        return self.donut_model.delete_donut(id)