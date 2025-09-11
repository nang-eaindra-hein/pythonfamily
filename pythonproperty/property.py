class Property:
    def __init__(
        self,
        id: int,
        address: str,
        postal_code: int,
        tenure: str,
        completion_year: int,
        property_type: str,
        area: float,
        valuation: float,
        commission_rate: float = 0.01,  # default 1%
    ):
        self.id = id
        self.address = address
        self.postal_code = self._validate_postal_code(postal_code)
        self.tenure = tenure
        self.completion_year = completion_year
        self.property_type = property_type
        self.area = area
        self.valuation = valuation
        self.commission_rate = commission_rate

    @staticmethod
    def _validate_postal_code(pc) -> int:
        if isinstance(pc, int) and 100000 <= pc <= 999999:
            return pc
        raise ValueError("Postal code must be a 6 digit number")

    # --- getters/setters (use only if needed) ---
    def get_id(self): return self.id
    def set_id(self, id_: int): self.id = id_

    def get_address(self): return self.address
    def set_address(self, address: str): self.address = address

    def get_postal_code(self): return self.postal_code
    def set_postal_code(self, postal_code: int): self.postal_code = self._validate_postal_code(postal_code)

    def get_tenure(self): return self.tenure
    def set_tenure(self, tenure: str): self.tenure = tenure

    def get_completion_year(self): return self.completion_year
    def set_completion_year(self, year: int): self.completion_year = year

    def get_property_type(self): return self.property_type
    def set_property_type(self, t: str): self.property_type = t

    def get_area(self): return self.area
    def set_area(self, area: float): self.area = area

    def get_valuation(self): return self.valuation
    def set_valuation(self, valuation: float): self.valuation = valuation

    def calculate_commission(self) -> float:
        """Agency commission amount based on the property's commission_rate."""
        return self.valuation * self.commission_rate

    def __str__(self) -> str:
        return (
            f"{self.property_type} @ {self.address} ({self.postal_code}) "
            f"{self.area} sq ft, ${self.valuation:,.2f}, rate {self.commission_rate*100:.2f}%"
        )

    def display_info(self) -> str:
        return (
            f"ID: {self.id}\n"
            f"Address: {self.address}\n"
            f"Postal Code: {self.postal_code}\n"
            f"Tenure: {self.tenure}\n"
            f"Completion Year: {self.completion_year}\n"
            f"Property Type: {self.property_type}\n"
            f"Area: {self.area} sq ft\n"
            f"Valuation: ${self.valuation:,.2f}\n"
            f"Commission Rate: {self.commission_rate * 100:.2f}%\n"
            f"Commission: ${self.calculate_commission():,.2f}"
        )
