## Modify the Database
Add an Email column to the Staff table in PostgreSQL. Assuming you’re using psql or a similar tool:

``` sql
ALTER TABLE "Staff" 
ADD COLUMN "Email" VARCHAR(255) UNIQUE;
VARCHAR(255) is a typical length for email fields; adjust if needed.
UNIQUE ensures no duplicate emails (optional but recommended for auth).
```

If you want existing staff to have emails, update them manually or via a script:

``` sql
UPDATE "Staff" SET "Email" = LOWER("StaffFirstName" || '.' || "StaffLastName" || '@example.com')
WHERE "Email" IS NULL;
```

## Script to Hash All Plain-Text Passwords
If you have multiple unhashed passwords:

Run this script to update all plain-text passwords in Staff:
``` python
# hash_passwords.py
from passlib.context import CryptContext
import psycopg2

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Connect to your database
conn = psycopg2.connect("postgresql://postgres:mc%4024949981@10.0.1.19:5432/SynergyV")
cur = conn.cursor()

# Find plain-text passwords (assuming they don’t start with $2b$)
cur.execute("SELECT \"StaffCode\", \"Password\" FROM \"Staff\" WHERE \"Password\" NOT LIKE '$2b$%'")
unhashed = cur.fetchall()

for staff_code, plain_password in unhashed:
    hashed = pwd_context.hash(plain_password)
    cur.execute("UPDATE \"Staff\" SET \"Password\" = %s WHERE \"StaffCode\" = %s", (hashed, staff_code))
    print(f"Updated {staff_code}: {plain_password} -> {hashed}")

conn.commit()
cur.close()
conn.close()
```

Run it:
``` bash
python hash_passwords.py
```

Verify:
``` sql
SELECT "StaffCode", "Email", "Password" FROM "Staff";
```
All Password values should now be bcrypt hashes.


## Step 1: Regenerate app/models.py Without Views
Run sqlacodegen with the --noviews option to exclude views:

``` bash
sqlacodegen postgresql://postgres:mc%4024949981@10.0.1.19:5432/SynergyV --noviews > app/models.py
```
* --noviews: Tells sqlacodegen to skip database views and only generate models for tables.

## Step 2: Regenerate app/schemas_auto.py
Since app/models.py will now only contain tables, regenerate the Pydantic schemas:

``` bash
python -m app.generate_schemas
```

## Step 3: Run the Server Again
Start the server:

``` bash
uvicorn app.main:app --reload
```

