# BBSoft Python SDK

A Python SDK for the [BBSoft FMS API](https://api.bbsoft.co.za/index.html). All GET endpoints return data as **pandas DataFrames**.

## Installation

```bash
pip install -e .
```

**Dependencies:** `requests`, `pandas` (installed automatically).

## Authentication

Set your API key as an environment variable:

```bash
export BBS-API-KEY="your-api-key-here"
```

Or pass it directly:

```python
from bbsoft import BBSoftClient

client = BBSoftClient(api_key="your-api-key-here")
```

## Quick Start

```python
from bbsoft import BBSoftClient

client = BBSoftClient()  # reads BBS-API-KEY from environment

# List all accounts
df = client.accounts.list()
print(df.head())

# Get transactions for a date range
df = client.transactions.get_by_date("2026-01-01", "2026-01-31")
print(df.shape)
```

## Resources

### Accounts — `client.accounts`

```python
client.accounts.list()                                  # all accounts
client.accounts.get_by_id(1)                            # by record ID
client.accounts.get_by_account_number("ACC001")         # by account number
client.accounts.get_by_status(active=True)              # by active/inactive

client.accounts.create("ACC002", "My Account", 5000.0)  # create
client.accounts.update("ACC002", "My Account", 6000.0, active=True)  # update
```

### Account Discounts — `client.discounts`

```python
client.discounts.list()                                 # all discounts
client.discounts.get_by_id(1)                           # by record ID
client.discounts.get_by_account_number("ACC001")        # by account number

client.discounts.create("ACC001", "PROD01", 0.50)       # create
client.discounts.update("ACC001", "PROD01", 0.75, active=True)  # update
```

### Vehicles — `client.vehicles`

```python
client.vehicles.list()                                  # all vehicles
client.vehicles.get_by_id(1)                            # by record ID
client.vehicles.get_by_registration("ABC123GP")         # by registration

client.vehicles.create("ACC001", "ABC123GP", "John Doe")
client.vehicles.update("ACC001", "ABC123GP", "John Doe", active=True)
```

### Fuel Orders — `client.fuel_orders`

```python
client.fuel_orders.list()                               # all orders
client.fuel_orders.get_by_id(1)                         # by record ID
client.fuel_orders.get_by_account_number("ACC001")      # by account number
client.fuel_orders.get_by_order_number("ORD001")        # by order number
client.fuel_orders.get_by_date("2026-01-01", "2026-01-31")  # by date range

# Create a fuel order
client.fuel_orders.create(
    product_code="PROD01",
    account_number="ACC001",
    vehicle_registration="ABC123GP",
    driver="John Doe",
    order_number="ORD001",
    order_reference="REF001",
    order_litres=100.0,
    order_expiry="2026-06-30",
)

# Cancel a fuel order
client.fuel_orders.cancel(id=1, order_expiry="2026-04-01")
```

### Products — `client.products`

```python
from bbsoft import ProductType, MIF

client.products.list()                                  # all products
client.products.get_by_id(1)                            # by record ID
client.products.get_by_product_code("PROD01")           # by product code

# Create a product
client.products.create(
    product_code="PROD01",
    product_barcode="1234567890",
    product_description="Diesel 50ppm",
    product_price=22.50,
    type=ProductType.DIESEL_50PPM,
    mif=MIF.DIESEL_50PPM_ALL,
)

# Update price
client.products.update_price("PROD01", 23.00, "2026-04-01")
```

### Shifts — `client.shifts`

```python
client.shifts.list()                                    # all shifts
client.shifts.get_by_id(1)                              # by record ID
client.shifts.get_by_date("2026-01-01", "2026-01-31")   # by date range

client.shifts.change("2026-03-27")                      # create/change shift
```

### Transactions — `client.transactions`

```python
from bbsoft import TransactionStatus, PaymentType

# Lookups
client.transactions.get_by_id(1)
client.transactions.get_by_greater_id(100)
client.transactions.get_by_invoice_id(42)
client.transactions.get_by_shift(5)
client.transactions.get_by_order_number("ORD001")
client.transactions.get_by_status(TransactionStatus.COMPLETED)

# Date-range queries
client.transactions.get_by_date("2026-01-01", "2026-01-31")
client.transactions.get_completed_by_date("2026-01-01", "2026-01-31")

# Filtered queries
client.transactions.get_by_payment_type(PaymentType.CASH, "2026-01-01", "2026-01-31")
client.transactions.get_by_pump_pos(1, "2026-01-01", "2026-01-31")
client.transactions.get_by_attendant("Jane", "2026-01-01", "2026-01-31")

# Infinity transactions
client.transactions.get_infinity_by_id(1)
client.transactions.get_infinity_by_date("2026-01-01", "2026-01-31")

# Update invoice number
client.transactions.update_invoice(id=1, invoice_number="INV001")
```

## Working with DataFrames

All GET methods return pandas DataFrames, so you can use the full pandas API:

```python
df = client.transactions.get_by_date("2026-01-01", "2026-01-31")

# Filter
cash_only = df[df["paymentType"] == "CASH"]

# Aggregate
daily_totals = df.groupby("transactionDate")["amount"].sum()

# Export
df.to_csv("transactions.csv", index=False)
df.to_excel("transactions.xlsx", index=False)
```

## Date Formats

Date parameters accept any of these formats:

```python
from datetime import date, datetime

client.shifts.get_by_date("2026-01-01", "2026-01-31")           # strings
client.shifts.get_by_date(date(2026, 1, 1), date(2026, 1, 31))  # date objects
client.shifts.get_by_date(datetime(2026, 1, 1, 8, 0), datetime(2026, 1, 31, 17, 0))  # datetimes
```

## Enums

The SDK provides enums for type-safe parameter values:

| Enum | Values |
|---|---|
| `ProductType` | `DIESEL_10PPM`, `DIESEL_50PPM`, `DIESEL_500PPM`, `UNLEADED_93`, `UNLEADED_95`, `LEAD_REPLACEMENT_93`, `LEAD_REPLACEMENT_95`, `SUPER`, `PARAFFIN`, `OIL`, `CARWASH` |
| `TransactionStatus` | `AUTHORIZED`, `BUSY`, `FINISHED`, `PROCESSED`, `COMPLETED`, `IQ_COMPLETED`, `PROCESSED_SPEEDPOINT` |
| `PaymentType` | `ACCOUNT`, `CASH`, `CARD`, `EFT` |
| `MIF` | Various product/integration mappings (see `bbsoft/enums.py`) |

## Error Handling

```python
from bbsoft import BBSoftClient, AuthenticationError, NotFoundError, ServerError, BBSoftError

client = BBSoftClient()

try:
    df = client.accounts.get_by_id(999)
except AuthenticationError:
    print("Invalid API key")
except NotFoundError:
    print("Account not found")
except ServerError:
    print("API server error — try again later")
except BBSoftError as e:
    print(f"API error ({e.status_code}): {e}")
```
