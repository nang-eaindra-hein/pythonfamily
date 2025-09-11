from typing import List
from property import Property

class PropertyAgent:
    def __init__(self, registration_number, company, start_year):
        self.company = company
        self.registration_number = registration_number
        self.start_year = start_year

        # agent's personal share (70% of property commission by default)
        self.commission_sharing_rate = 0.70

        self.unsold_properties: List[Property] = []
        self.sold_properties: List[Property] = []

    def get_registration_number(self):
        return self.registration_number

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    def get_company(self):
        return self.company

    def set_company(self, company):
        self.company = company

    def get_start_year(self):
        return self.start_year

    def set_start_year(self, start_year):
        self.start_year = start_year

    def get_commission_sharing_rate(self):
        return self.commission_sharing_rate

    # --- inventory ops ---
    def add_unsold_property(self, property):
        if property not in self.unsold_properties and property not in self.sold_properties:
            self.unsold_properties.append(property)

    def sell_property(self, property):
        if property in self.unsold_properties:
            self.unsold_properties.remove(property)
            self.sold_properties.append(property)
        elif property in self.sold_properties:
            # already sold; ignore
            pass
        else:
            # allow direct sold add (not present before)
            self.sold_properties.append(property)

    def get_unsold_properties(self):
        return list(self.unsold_properties)

    def get_sell_properties(self):
        return list(self.sold_properties)

    # --- commissions ---
    def total_property_commission(self) -> float:
        """Sum of raw commissions from the properties sold (agency-level commission)."""
        return sum(p.calculate_commission() for p in self.sold_properties)

    def calculate_total_commission(self) -> float:
        """Agent's take-home commission (agent share of raw commissions)."""
        return self.total_property_commission() * self.commission_sharing_rate

    def __str__(self):
        return f"Agent {self.registration_number} ({self.company})"
