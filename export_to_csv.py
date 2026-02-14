import csv
import os
from pymongo import MongoClient
from config import Config

EXPENSE_CATEGORIES = ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]


class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = int(age)
        self.gender = str(gender)
        self.total_income = float(total_income)
        self.expenses = expenses or {}

    def to_row(self):
        row = {
            "age": self.age,
            "gender": self.gender,
            "total_income": self.total_income,
        }
        for cat in EXPENSE_CATEGORIES:
            row[cat] = float(self.expenses.get(cat, 0.0))
        row["total_expenses"] = sum(row[cat] for cat in EXPENSE_CATEGORIES)
        row["savings_estimate"] = self.total_income - row["total_expenses"]
        return row


def main():
    client = MongoClient(Config.MONGO_URI)
    db = client[Config.DB_NAME]
    col = db[Config.COLLECTION_NAME]

    docs = list(col.find({}))
    users = []
    for d in docs:
        users.append(
            User(
                age=d.get("age", 0),
                gender=d.get("gender", ""),
                total_income=d.get("total_income", 0.0),
                expenses=d.get("expenses", {}),
            )
        )

    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", "responses.csv")

    fieldnames = ["age", "gender", "total_income"] + EXPENSE_CATEGORIES + [
        "total_expenses",
        "savings_estimate",
    ]

    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for u in users:
            writer.writerow(u.to_row())

    print(f"Wrote {len(users)} rows to {out_path}")


if __name__ == "__main__":
    main()
