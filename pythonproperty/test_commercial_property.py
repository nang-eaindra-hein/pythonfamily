from commercial_property import CommercialProperty

# valid
property1 = CommercialProperty(1, "Common St", 564566, "Freehold", 2008, "Office", 80, 500000)
print(property1.get_address())
print(property1.get_postal_code())
print(property1.get_tenure())
print(property1.get_valuation())
print(property1.get_area())
print(property1.get_commercial_property_type())

# invalid type -> expect ValueError
try:
    bad = CommercialProperty(2, "Common St", 574544, "Freehold", 2008, "Apartment", 80, 500000)
    print("SHOULD NOT PRINT", bad.get_commercial_property_type())
except ValueError as e:
    print("Caught expected error:", e)
