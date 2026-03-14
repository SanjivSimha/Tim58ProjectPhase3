import json
from pathlib import Path
from datetime import datetime
from models import Customer, User, Subscription, Invoice

DATA_DIR = Path(__file__).parent / "data"

def parse_date(date_str):
    if date_str:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    return None

def load_customers() -> list[Customer]:
    with open(DATA_DIR / "customers.json") as f:
        return [Customer(**c) for c in json.load(f)]

def load_users() -> list[User]:
    with open(DATA_DIR / "users.json") as f:
        return [User(**u) for u in json.load(f)]

def load_subscriptions() -> list[Subscription]:
    with open(DATA_DIR / "subscriptions.json") as f:
        data = json.load(f)
    subs = []
    for s in data:
        subs.append(Subscription(
            id=s["id"],
            customer_id=s["customer_id"],
            plan=s["plan"],
            price=s["price"],
            billing_cycle=s["billing_cycle"],
            started_at=parse_date(s["started_at"]),
            renews_at=parse_date(s["renews_at"]),
            payment_method=s["payment_method"],
            card_last_four=s.get("card_last_four"),
            card_brand=s.get("card_brand"),
            card_exp=s.get("card_exp")
        ))
    return subs

def load_invoices() -> list[Invoice]:
    with open(DATA_DIR / "invoices.json") as f:
        data = json.load(f)
    invoices = []
    for i in data:
        invoices.append(Invoice(
            id=i["id"],
            customer_id=i["customer_id"],
            amount=i["amount"],
            status=i["status"],
            issued_at=parse_date(i["issued_at"]),
            paid_at=parse_date(i.get("paid_at")),
            period=i["period"]
        ))
    return invoices

def get_user(user_id: str) -> User | None:
    users = load_users()
    return next((u for u in users if u.id == user_id), None)

def get_customer(customer_id: str) -> Customer | None:
    customers = load_customers()
    return next((c for c in customers if c.id == customer_id), None)

def get_users_for_customer(customer_id: str) -> list[User]:
    users = load_users()
    return [u for u in users if u.customer_id == customer_id]

def get_subscription_for_customer(customer_id: str) -> Subscription | None:
    subs = load_subscriptions()
    return next((s for s in subs if s.customer_id == customer_id), None)

def get_invoices_for_customer(customer_id: str) -> list[Invoice]:
    invoices = load_invoices()
    return sorted([i for i in invoices if i.customer_id == customer_id], 
                  key=lambda x: x.issued_at, reverse=True)

def save_customer(customer: Customer):
    customers = load_customers()
    for i, c in enumerate(customers):
        if c.id == customer.id:
            customers[i] = customer
            break
    data = [{"id": c.id, "company_name": c.company_name, "address": c.address,
             "city": c.city, "state": c.state, "zip": c.zip,
             "billing_email": c.billing_email, "phone": c.phone} 
            for c in customers]
    with open(DATA_DIR / "customers.json", "w") as f:
        json.dump(data, f, indent=2)
