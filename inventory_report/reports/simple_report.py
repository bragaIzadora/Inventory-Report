from inventory_report.inventory import Inventory
from datetime import datetime


class SimpleReport:
    def __init__(self):
        self._inventories = []

    def add_inventory(self, inventory: Inventory) -> None:
        self._inventories.append(inventory)

    def generate(self) -> str:
        products = [
            product
            for inv in self._inventories
            for product in inv.data
        ]

        if not products:
            return (
                "Oldest manufacturing date: N/A\n"
                "Closest expiration date: N/A\n"
                "Company with the largest inventory: N/A"
            )

        oldest_date = min(
            datetime.strptime(p.manufacturing_date, "%Y-%m-%d")
            for p in products
        ).strftime("%Y-%m-%d")

        today = datetime.today()
        valid_dates = [
            datetime.strptime(p.expiration_date, "%Y-%m-%d")
            for p in products
            if datetime.strptime(p.expiration_date, "%Y-%m-%d") > today
        ]
        closest_expiration = (
            min(valid_dates).strftime("%Y-%m-%d") if valid_dates else "N/A"
        )

        company_counts = {}
        for p in products:
            company_name = p.company_name
            count = company_counts.get(company_name, 0)
            company_counts[company_name] = count + 1

        largest_company = max(
            company_counts, key=company_counts.get, default="N/A"
        )

        return (
            f"Oldest manufacturing date: {oldest_date}\n"
            f"Closest expiration date: {closest_expiration}\n"
            f"Company with the largest inventory: {largest_company}"
        )
