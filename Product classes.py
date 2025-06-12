class Product:
    def __init__(self,product_id,name,description,is_active=True):
        self.product_id=product_id
        self.name=name
        self.description=description
        self.is_active=is_active

    def update(self, name=None,description=None):
        if name:
            self.name=name
        if description:
            self.description=description
    def suspend(self):
        self.is_active=False
    def __str__(self):
        status="Active" if self.is_active else "Suspended"
        return f"Product ID:{self.product_id}, Name:{self.name},Status:{self.status}"
