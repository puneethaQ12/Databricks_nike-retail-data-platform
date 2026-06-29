import os
import random
import pandas as pd
from faker import Faker

fake = Faker("en_IN")

OUTPUT_FOLDER = "../datasets/raw"
NUMBER_OF_CUSTOMERS = 1000


def generate_customer_id(number):
    return f"C{number:06d}"


def generate_customers():

    customers = []

    for i in range(1, NUMBER_OF_CUSTOMERS + 1):

        first_name = fake.first_name()
        last_name = fake.last_name()

        customers.append({

            "customer_id": generate_customer_id(i),

            "first_name": first_name,

            "last_name": last_name,

            "email": f"{first_name.lower()}.{last_name.lower()}@gmail.com",

            "phone": fake.msisdn()[:10],

            "city": fake.city(),

            "state": fake.state(),

            "country": "India",

            "signup_date": fake.date_between("-5y", "today"),

            "customer_status": random.choice(["ACTIVE", "INACTIVE"])

        })

    df = pd.DataFrame(customers)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    df.to_csv(f"{OUTPUT_FOLDER}/customers.csv", index=False)

    print(f"Generated {len(df)} customers")


if __name__ == "__main__":
    generate_customers()
