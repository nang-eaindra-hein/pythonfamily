from typing import List
from property_agent import PropertyAgent

class PropertyAgencyDirector(PropertyAgent):
    """
    Director is also an agent (earns personal commissions using their own share rate),
    plus an overriding commission on subordinate agents' commissions.
    """
    def __init__(self, registration_number, company, start_year,
                 director_commission_rate, commission_sharing_rate):
        super().__init__(registration_number, company, start_year)
        self.agents: List[PropertyAgent] = []

        # validate and set rates (avoid name clashes with attributes)
        self._set_director_commission_rate(director_commission_rate)  # 0.05..0.15
        self._set_commission_sharing_rate(commission_sharing_rate)    # 0.75..0.90 (director's own share)

    # manage agents
    def add_agent(self, agent):
        if agent not in self.agents:
            self.agents.append(agent)
        else:
            print("Agent is already in the list")

    def get_agents(self):
        return list(self.agents)

    def remove_agent(self, agent):
        if agent in self.agents:
            self.agents.remove(agent)
        else:
            print("Agent is not found in the list")

    # validation helpers
    def _set_commission_sharing_rate(self, rate):
        if 0.75 <= rate <= 0.90:
            self.commission_sharing_rate = rate
        else:
            raise ValueError("Commission sharing rate must be between 0.75 and 0.90")

    def get_commission_sharing_rate(self):
        return self.commission_sharing_rate

    def _set_director_commission_rate(self, rate):
        if 0.05 <= rate <= 0.15:
            self.director_commission_rate = rate
        else:
            raise ValueError("Director commission rate must be between 0.05 and 0.15")

    def get_director_commission_rate(self):
        return self.director_commission_rate

    # commission totals
    def subordinate_commission_total(self) -> float:
        """Total take-home commissions of all subordinate agents."""
        return sum(a.calculate_total_commission() for a in self.agents)

    def calculate_total_commission(self) -> float:
        """
        Director's total = personal take-home (using director's share)
        + override (director_commission_rate * subordinates' take-home totals).
        """
        personal = super().calculate_total_commission()
        override = self.subordinate_commission_total() * self.director_commission_rate
        return personal + override

    def __str__(self):
        return f"Director {self.registration_number} ({self.company})"
