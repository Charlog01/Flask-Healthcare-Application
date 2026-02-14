from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime
from config import Config

application = Flask(__name__)
application.config.from_object(Config)

client = MongoClient(application.config["MONGO_URI"], serverSelectionTimeoutMS=5000)
db = client[application.config["DB_NAME"]]
responses = db[application.config["COLLECTION_NAME"]]

EXPENSE_CATEGORIES = ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]


def _to_float(value):
    if value is None:
        return 0.0
    value = str(value).strip()
    if value == "":
        return 0.0
    return float(value)


@application.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        age = int(request.form.get("age", "0"))
        gender = request.form.get("gender", "").strip()
        total_income = _to_float(request.form.get("total_income"))

        expenses = {}
        for cat in EXPENSE_CATEGORIES:
            checked = request.form.get(f"chk_{cat}")
            amount = _to_float(request.form.get(f"amt_{cat}"))
            if checked:
                expenses[cat] = amount

        doc = {
            "age": age,
            "gender": gender,
            "total_income": total_income,
            "expenses": expenses,
            "created_at": datetime.utcnow(),
        }
        responses.insert_one(doc)
        return render_template("success.html")

    return render_template("index.html", categories=EXPENSE_CATEGORIES)


@application.route("/health")
def health():
    return {"status": "ok"}


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000, debug=True)
