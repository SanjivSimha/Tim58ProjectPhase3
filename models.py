from dataclasses import dataclass
from typing import Optional
from datetime import date

@dataclass
class Customer:
    id: str
    company_name: str
    address: str
    city: str
    state: str
    zip: str
    billing_email: str
    phone: str

@dataclass
class User:
    id: str
    customer_id: str
    name: str
    email: str
    role: str  # admin, billing, viewer - BUT NOT ENFORCED

@dataclass
class Subscription:
    id: str
    customer_id: str
    plan: str
    price: int
    billing_cycle: str
    started_at: date
    renews_at: date
    payment_method: str
    card_last_four: Optional[str]
    card_brand: Optional[str]
    card_exp: Optional[str]

@dataclass
class Invoice:
    id: str
    customer_id: str
    amount: int
    status: str
    issued_at: date
    paid_at: Optional[date]
    period: str
