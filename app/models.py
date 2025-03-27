from django.db import models

class Client(models.Model):
    username = models.CharField(max_length=100)
    national_id = models.CharField(max_length=20, unique=True)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.username


class House(models.Model):
    house_number = models.CharField(max_length=20, unique=True)
    rent_amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    last_reading = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"House {self.house_number}"


class Receipt(models.Model):
    receipt_number = models.AutoField(primary_key=True)
    date_issued = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    
    # Invoice details
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    rental_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    electricity_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    electricity_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    water_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    water_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    security_charge = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    previous_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    other_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    previous_water_reading=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    current_water_reading=models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 



    
    def total_amount(self):
        return (
            self.monthly_rent + self.rental_deposit + self.electricity_deposit + 
            self.electricity_bill + self.water_deposit + self.water_bill + 
            self.service_charge + self.security_charge + self.previous_balance + 
            self.other_charges
        )

    def __str__(self):
        return f"Receipt {self.receipt_number} - {self.client.username}"
