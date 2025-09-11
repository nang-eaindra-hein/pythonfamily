from property_agent import PropertyAgent
from property import Property

agent123 = PropertyAgent("F222", "ABC Realty", 2011)

property3 = Property(3, "987 Lily Ln", 951753, "Freehold", 2018, "Townhouse", 200, 850000)
property4 = Property(4, "741 Tulip St", 123789, "Freehold", 2007, "Apartment", 220, 950000)
property5 = Property(5, "852 Orchid Dr", 987123, "Freehold", 2013, "Condo", 120, 1300000)

agent123.add_unsold_property(property3)
agent123.add_unsold_property(property4)
agent123.add_unsold_property(property5)

agent123.sell_property(property3)
agent123.sell_property(property4)

for p in agent123.get_sell_properties():
    print(f"sold: {p.address}, {p.postal_code}, {p.tenure}, {p.valuation}, {p.area}")

print("Agent raw commission total:", agent123.total_property_commission())
print("Agent take-home commission:", agent123.calculate_total_commission())
