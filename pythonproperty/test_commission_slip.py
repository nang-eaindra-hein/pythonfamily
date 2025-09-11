from property_agent import PropertyAgent
from property_agency_director import PropertyAgencyDirector
from property import Property
from commission_slip import CommissionSlip

def test_commission_slip():
    agent = PropertyAgent("K66", "CKK Group", 2010)
    p1 = Property(1, "A St", 111111, "Freehold", 2010, "Condo", 120, 500000)
    p2 = Property(2, "B St", 222222, "Freehold", 2012, "House", 200, 800000)
    agent.add_unsold_property(p1); agent.sell_property(p1)
    agent.add_unsold_property(p2); agent.sell_property(p2)

    director = PropertyAgencyDirector("D88", "CKK Group", 2005, 0.10, 0.80)
    director.add_agent(agent)

    print(CommissionSlip.generate_commission_report(agent))
    print(CommissionSlip.generate_commission_report(director))

if __name__ == "__main__":
    test_commission_slip()
