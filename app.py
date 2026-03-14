from flask import Flask, render_template, request, redirect, url_for, session
import store

app = Flask(__name__)
app.secret_key = "nimbuspay-dev-key"


@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))


@app.route("/dashboard")
def dashboard():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    customer = store.get_customer(user.customer_id)
    team_members = store.get_users_for_customer(user.customer_id)
    subscription = store.get_subscription_for_customer(user.customer_id)
    invoices = store.get_invoices_for_customer(user.customer_id)
    template = f"dashboard_{subscription.plan}.html"
    return render_template(template,
                           user=user, customer=customer,
                           team=team_members, subscription=subscription,
                           invoices=invoices)


@app.route("/login")
def login():
    users = store.load_users()
    customers = {c.id: c for c in store.load_customers()}
    subscriptions = {s.customer_id: s for s in store.load_subscriptions()}
    # Show only account holders (admins) - one per customer
    admins = [u for u in users if u.role == "admin"]
    return render_template("login.html", users=admins,
                           customers=customers, subscriptions=subscriptions)


@app.route("/set-user", methods=["POST"])
def set_user():
    user_id = request.form.get("user_id")
    if user_id:
        session["user_id"] = user_id
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/account")
def account():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    customer = store.get_customer(user.customer_id)
    return render_template("account.html", user=user, customer=customer)


@app.route("/account/edit", methods=["GET", "POST"])
def account_edit():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    customer = store.get_customer(user.customer_id)

    if request.method == "POST":
        customer.company_name = request.form["company_name"]
        customer.address = request.form["address"]
        customer.city = request.form["city"]
        customer.state = request.form["state"]
        customer.zip = request.form["zip"]
        customer.billing_email = request.form["billing_email"]
        customer.phone = request.form["phone"]
        store.save_customer(customer)
        # No confirmation message - intentional UX problem
        return redirect(url_for("account"))

    return render_template("account_edit.html", user=user, customer=customer)


@app.route("/team")
def team():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    customer = store.get_customer(user.customer_id)
    team_members = store.get_users_for_customer(user.customer_id)
    # No role enforcement - everyone sees this
    # No way to add/remove members - intentional missing feature
    return render_template("team.html", user=user, customer=customer, team=team_members)


@app.route("/subscription")
def subscription():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    customer = store.get_customer(user.customer_id)
    sub = store.get_subscription_for_customer(user.customer_id)
    return render_template("subscription.html", user=user, customer=customer, subscription=sub)


@app.route("/billing")
def billing():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    customer = store.get_customer(user.customer_id)
    invoices = store.get_invoices_for_customer(user.customer_id)
    # No download option - intentional missing feature
    return render_template("billing.html", user=user, customer=customer, invoices=invoices)


@app.route("/payment")
def payment():
    user = get_current_user()
    if not user:
        return redirect(url_for("login"))
    customer = store.get_customer(user.customer_id)
    sub = store.get_subscription_for_customer(user.customer_id)
    return render_template("payment.html", user=user, customer=customer, subscription=sub)


def get_current_user():
    user_id = session.get("user_id")
    if user_id:
        return store.get_user(user_id)
    return None


if __name__ == "__main__":
    app.run(debug=True, port=5000)
