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

## Phase 3 Dashboard Redesign

The Starter and Enterprise dashboard templates were redesigned based on persona research, content inventories, and wireframes from the TIM58 Project Phase 3 design document.

### Jamie's Dashboard (Starter) — `dashboard_starter.html`

Redesigned for a solo consultant whose primary goal is invoice and billing management.

**Layout (top to bottom):**

1. **Changes Saved banner** — confirmation alert at the top (shown via `?saved=1` query param) addressing Jamie's concern about not knowing if changes were saved
2. **Invoices** — promoted to the top section as the highest priority; table includes #, Period, Amount, Status, Issued, Date Paid, and a Download button per row
3. **Payment Method + Subscription (side by side)** — card summary with Update Payment Method button on the left; plan, price, renewal date, and billing cycle on the right
4. **Account Info** — company name, phone, billing email, and address
5. **Action buttons** — Update Account Info and Contact Support

**Excluded elements:** Team section (Jamie is a solo user), Started date, Plan change buttons (Upgrade/Downgrade/Cancel)

### Jennifer's Dashboard (Enterprise) — `dashboard_enterprise.html`

Redesigned for an operations director who manages a large team and needs at-a-glance invoice oversight.

**Layout (top to bottom):**

1. **Account Summary card** — plan name and next renewal on the left; invoice status counts (Overdue, Pending, Paid) on the right for immediate risk visibility
2. **Team Management** — member count, table with Name/Email/Role, expandable rows (first 5 shown with an Expand toggle for the rest), and Add Member / Remove / Change Role action buttons
3. **Invoices** — select-all checkbox, per-row checkboxes for batch selection, table with Invoice/Period/Amount/Status/Issued/Paid, and a Download button
4. **Subscription + Contact Support** — plan name, price, billing cycle, billing email, and next renewal, with a Contact Support button alongside

**Excluded elements:** Company address/phone, Card on File / Update Card / Remove Card (Northwind uses invoice billing)

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

> **Note:** Issues 2, 3, 5, and 8 are partially addressed in the Phase 3 dashboard redesign through UI additions (download buttons, confirmation banners, support links, and team management controls). Full backend implementation is outside the current scope.

