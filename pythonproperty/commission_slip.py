from typing import Union
from property_agent import PropertyAgent
from property_agency_director import PropertyAgencyDirector

class CommissionSlip:
    @staticmethod
    def generate_commission_report(entity: Union[PropertyAgent, PropertyAgencyDirector]) -> str:
        is_director = isinstance(entity, PropertyAgencyDirector)
        header = (
            f"[Director Commission Report] {entity.registration_number} - {entity.company}"
            if is_director else
            f"[Agent Commission Report] {entity.registration_number} - {entity.company}"
        )

        lines = [
            header,
            "-" * len(header),
            f"Year Started: {entity.start_year}",
            f"Properties sold: {len(entity.get_sell_properties())}",
        ]

        sold = entity.get_sell_properties()
        if sold:
            lines.append("\nSold Properties:")
            for p in sold:
                lines.append(
                    f"- ID {p.id}: {p.property_type} @ {p.address} | "
                    f"Valuation ${p.valuation:,.2f} | Rate {p.commission_rate*100:.2f}% | "
                    f"Raw Commission ${p.calculate_commission():,.2f}"
                )

        raw_total = sum(p.calculate_commission() for p in sold)
        agent_take_home = entity.calculate_total_commission()

        lines.append(f"\nAgent raw commission total: ${raw_total:,.2f}")
        lines.append(f"Agent take-home (@ {entity.commission_sharing_rate*100:.2f}%): ${agent_take_home:,.2f}")

        if is_director:
            sub_take = entity.subordinate_commission_total()
            override = sub_take * entity.director_commission_rate
            lines += [
                f"Subordinates: {len(entity.get_agents())}",
                f"Subordinates' take-home total: ${sub_take:,.2f}",
                f"Director override (@ {entity.director_commission_rate*100:.2f}%): ${override:,.2f}",
                "-----------",
                f"Director grand total: ${agent_take_home + override:,.2f}",
            ]
        else:
            lines.append(f"Agent grand total: ${agent_take_home:,.2f}")

        return "\n".join(lines) + "\n"
