class UnitConverter:
    def __init__(self):
        self.MILES_FACTOR = 0.621371
        self.INCH_TO_CM = 2.54
        self.LBS_TO_KG = 0.453592
        self.K_TO_M = 1000
        self.LITER_TO_GALLON = 0.264172
        self.SQFT_TO_SQMT = 0.092903
      
    # --- Distance & Length ---
    def kilo_to_miles(self, km):
        return km * self.MILES_FACTOR

    def miles_to_kilo(self, miles):
        return miles / self.MILES_FACTOR

    def kilo_to_meters(self, km):
        return km * self.K_TO_M

    def inch_to_cm(self, inches):
        return inches * self.INCH_TO_CM

    def cm_to_inch(self, cm):
        return cm / self.INCH_TO_CM

    # --- Weight ---
    def kg_to_lbs(self, kg):
        return kg / self.LBS_TO_KG

    def lbs_to_kg(self, lbs):
        return lbs * self.LBS_TO_KG

    # --- Temperature ---
    def celsius_to_fahrenheit(self, c):
        return (c * 9/5) + 32

    def fahrenheit_to_celsius(self, f):
        return (f - 32) * 5/9

    # --- Digital Storage ---
    def gb_to_mb(self, gb):
        return gb * 1024

    def mb_to_gb(self, mb):
        return mb / 1024
      
    # --- Time Conversions ---
    def hours_to_minutes(self, hours):
        return hours * 60

    def minutes_to_seconds(self, minutes):
        return minutes * 60

    def days_to_hours(self, days):
        return days * 24
      
    # --- Volume Conversions ---
    def liters_to_gallons(self, liters):
        return liters * self.LITER_TO_GALLON

    def gallons_to_liters(self, gallons):
        return gallons / self.LITER_TO_GALLON

    def ml_to_liters(self, ml):
        return ml / 1000
      
    # --- Area Conversions ---
    def sqft_to_sqmeters(self, sqft):
        return sqft * self.SQFT_TO_SQMT

    def sqmeters_to_sqft(self, sqmt):
        return sqmt / self.SQFT_TO_SQMT

    def acres_to_sqft(self, acres):
        return acres * 43560
