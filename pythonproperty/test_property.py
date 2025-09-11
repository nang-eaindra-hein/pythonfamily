from property import Property

property1 = Property(1, "Common St", 564566, "Freehold", 2008, "Apartment", 80, 500000)
print(property1.get_address())
print(property1.get_postal_code())

# incorrect postal code -> expect ValueError
try:
    Property(2, "Common St", 57744, "Freehold", 2008, "Apartment", 80, 500000)  # 5 digits
except ValueError as e:
    print("Caught expected error:", e)
