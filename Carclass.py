class Car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0
    def drive(self):
        self.odometer=self.odometer+1
    def get_info(self):
        print(f"the car travelled {self.odometer} kms")