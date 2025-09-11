from property import Property

class CommercialProperty(Property):
    def __init__(
        self,
        id: int,
        address: str,
        postal_code: int,
        tenure: str,
        completion_year: int,
        property_type: str,   # e.g., 'Office', 'Factory', 'Retail', ...
        area: float,
        valuation: float,
        commission_rate: float = 0.02,  # default 2% for commercial
    ):
        super().__init__(
            id,
            address,
            postal_code,
            tenure,
            completion_year,
            property_type,
            area,
            valuation,
            commission_rate,
        )
        self.commercial_property_type = self._validate_commercial_type(property_type)

    def _validate_commercial_type(self, property_type: str) -> str:
        allowed = {"office", "flatted factory", "factory", "retail", "warehouse"}
        if isinstance(property_type, str) and property_type.lower() in allowed:
            return property_type
        raise ValueError(
            f"Invalid commercial property type: {property_type}. "
            f"Allowed: {', '.join(sorted(allowed))}"
        )

    def get_commercial_property_type(self):
        return self.commercial_property_type
