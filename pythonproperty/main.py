from property import Property
from commercial_property import CommercialProperty
from property_agent import PropertyAgent
from property_agency_director import PropertyAgencyDirector
from commission_slip import CommissionSlip

def main():
    # Create some properties
    prop1 = Property(1, "123 Main St", 183450, "Freehold", 2005, "Condo", 120, 500000)
    prop2 = CommercialProperty(2, "456 Market St", 654321, "Leasehold", 2010, "Office", 300, 1200000)
    prop3 = Property(3, "789 Hill Rd", 118222, "Freehold", 2000, "House", 200, 800000)
    prop4 = Property(4, "376 Red Town", 458789, "Freehold", 2003, "Apartment", 250, 900000)
    prop5 = Property(5, "454 Jama Nai", 238789, "Freehold", 2001, "Condo", 50, 1500000)
    prop6 = Property(6, "162 Oak St", 328567, "Leasehold", 2002, "House", 180, 750000)
    prop7 = Property(7, "982 Pine St", 878543, "Freehold", 2004, "Condo", 130, 600000)
    prop8 = CommercialProperty(8, "753 Elm St", 560789, "Leasehold", 2012, "Office", 350, 1400000)
    prop9 = Property(9, "642 Birch St", 234667, "Freehold", 2008, "Apartment", 220, 850000)
    prop10 = Property(10, "875 Cedar St", 123689, "Freehold", 2015, "House", 190, 950000)
    prop11 = Property(11, "543 Maple St", 986654, "Leasehold", 2009, "Condo", 140, 650000)
    prop12 = CommercialProperty(12, "321 Walnut St", 865432, "Freehold", 2011, "Office", 310, 1250000)
    prop13 = Property(13, "874 Spruce St", 876123, "Leasehold", 2007, "House", 170, 700000)
    prop14 = Property(14, "125 Ash St", 345668, "Freehold", 2003, "Apartment", 240, 800000)
    prop15 = Property(15, "643 Cherry St", 678601, "Freehold", 2016, "Condo", 150, 550000)
    prop16 = Property(16, "784 Fir St", 455123, "Leasehold", 2001, "House", 210, 820000)
    prop17 = CommercialProperty(17, "215 Poplar St", 254890, "Freehold", 2014, "Office", 320, 1300000)
    prop18 = Property(18, "987 Hickory St", 785012, "Freehold", 2005, "Apartment", 260, 900000)
    prop19 = Property(19, "431 Palm St", 123590, "Leasehold", 2013, "House", 200, 870000)
    prop20 = Property(20, "569 Willow St", 654153, "Freehold", 2002, "Condo", 160, 600000)
    prop21 = Property(21, "142 Juniper St", 344789, "Leasehold", 2006, "Apartment", 230, 810000)
    prop22 = CommercialProperty(22, "356 Alder St", 678334, "Freehold", 2017, "Office", 340, 1350000)
    prop23 = Property(23, "763 Magnolia St", 567323, "Freehold", 2000, "House", 220, 890000)
    prop24 = Property(24, "258 Cypress St", 234367, "Leasehold", 2010, "Condo", 170, 580000)
    prop25 = Property(25, "693 Redwood St", 789245, "Freehold", 2004, "Apartment", 250, 950000)
    prop26 = Property(26, "826 Oakwood St", 103256, "Leasehold", 2008, "House", 240, 760000)
    prop27 = CommercialProperty(27, "478 Birchwood St", 652789, "Freehold", 2012, "Office", 330, 1450000)
    prop28 = Property(28, "369 Maplewood St", 325678, "Freehold", 2015, "Condo", 130, 610000)
    prop29 = Property(29, "159 Cedarwood St", 826123, "Leasehold", 2009, "House", 210, 710000)
    prop30 = Property(30, "754 Sprucewood St", 597890, "Freehold", 2007, "Apartment", 270, 870000)

    # Create agents
    agent1 = PropertyAgent("A123", "ABC Realty", 2015)
    agent2 = PropertyAgent("B456", "XYZ Realty", 2018)
    agent3 = PropertyAgent("C789", "LMN Realty", 2020)
    agent4 = PropertyAgent("D456", "XZY Realty", 2012)
    agent5 = PropertyAgent("E943", "CEF Realty ", 2014)
    agent6 = PropertyAgent("F322", "EEF Realty", 2013)

    # Assign inventory / mark sales
    for p in (prop1, prop2, prop3, prop4, prop5):
        agent1.add_unsold_property(p)
    agent1.sell_property(prop2)
    agent1.sell_property(prop3)
    agent1.sell_property(prop4)

    for p in (prop6, prop7, prop8, prop9, prop10):
        agent2.add_unsold_property(p)
    agent2.sell_property(prop6)
    agent2.sell_property(prop7)
    agent2.sell_property(prop8)

    for p in (prop11, prop12, prop13, prop14, prop15):
        agent3.add_unsold_property(p)
    agent3.sell_property(prop15)
    agent3.sell_property(prop13)
    agent3.sell_property(prop14)

    for p in (prop16, prop17, prop18, prop19, prop20):
        agent4.add_unsold_property(p)
    agent4.sell_property(prop18)
    agent4.sell_property(prop19)
    agent4.sell_property(prop20)

    for p in (prop21, prop22, prop23, prop24, prop25):
        agent5.add_unsold_property(p)
    agent5.sell_property(prop23)
    agent5.sell_property(prop24)
    agent5.sell_property(prop25)

    for p in (prop26, prop27, prop28, prop29, prop30):
        agent6.add_unsold_property(p)
    agent6.sell_property(prop26)
    agent6.sell_property(prop29)
    agent6.sell_property(prop30)

    # Directors & teams
    director1 = PropertyAgencyDirector("D101", "ABC Realty", 2010, 0.06, 0.75)
    director1.add_agent(agent1)
    director1.add_agent(agent2)
    director1.add_agent(agent3)

    director2 = PropertyAgencyDirector("E202", "XYZ Realty", 2012, 0.10, 0.85)
    director2.add_agent(agent4)
    director2.add_agent(agent5)
    director2.add_agent(agent6)

    # Reports
    print("\nCommission Slip\n" + CommissionSlip.generate_commission_report(agent1))
    print(CommissionSlip.generate_commission_report(agent2))
    print(CommissionSlip.generate_commission_report(director1))

    print("\nCommission Slip\n" + CommissionSlip.generate_commission_report(agent4))
    print(CommissionSlip.generate_commission_report(director2))

if __name__ == "__main__":
    main()
