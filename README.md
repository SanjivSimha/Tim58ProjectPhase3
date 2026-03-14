# NimbusPay Customer Portal - Starter System

Self-service portal for NimbusPay customers.

## Setup

```bash
pip install flask
```

## Running

```bash
python app.py
```

Open http://localhost:5000 in your browser.

## Accounts

The login page shows one account holder per customer. Each account is on a different plan tier.

| Account Holder | Company | Plan |
|---|---|---|
| David Chen | Riverstone Consulting | Business |
| Maria Santos | Bloom & Branch Design | Starter |
| Jennifer Adams | Northwind Logistics | Enterprise |
| Jamie Taylor | Solo Freelancer LLC | Starter |

Each plan tier has its own dashboard template (`dashboard_starter.html`, `dashboard_business.html`, `dashboard_enterprise.html`). The app routes to the correct template based on the account's plan.

## Current Features

- View account information
- Edit account details
- View team members
- View subscription info
- View billing history
- View payment method

## Known Issues

The portal has several UX problems that cause support tickets:

1. **No role enforcement** - The data has roles (admin, billing, viewer) but everyone sees and can edit everything

2. **Cannot add/remove team members** - Have to contact support

3. **Cannot download invoices** - Invoices visible but no PDF download

4. **Cannot update payment method** - Button exists but doesn't work

5. **No confirmation on save** - Unclear if changes were saved

6. **No empty states** - Solo users see empty team table

7. **Confusing navigation** - Flat list of pages with no grouping

8. **No support path** - No way to contact support from portal

