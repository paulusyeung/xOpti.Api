# app/generate_schemas.py
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from .models import Base  # Import Base
import inspect
import sys
from importlib import import_module
from datetime import datetime  # For datetime type
from decimal import Decimal    # For Decimal type

# Import app.models dynamically
models_module = import_module("app.models")
models = {name: cls for name, cls in inspect.getmembers(models_module, 
        lambda x: inspect.isclass(x) and x.__module__ == 'app.models' and issubclass(x, Base) and x != Base)}

# Generate Pydantic schemas for each model
schemas = {name: sqlalchemy_to_pydantic(cls) for name, cls in models.items()}

# Map Python types to Pydantic-compatible string names
type_map = {
    int: "int",
    str: "str",
    bool: "bool",
    float: "float",
    datetime: "datetime",
    Decimal: "Decimal"  # Add Decimal mapping
}

# Write to a file
with open("app/schemas_auto.py", "w") as f:
    f.write("from pydantic import BaseModel\n")
    f.write("from datetime import datetime\n")
    f.write("from decimal import Decimal\n\n")  # Add Decimal import
    for name, schema_class in schemas.items():
        f.write(f"class {name}(BaseModel):\n")
        for field_name, field in schema_class.__fields__.items():
            # Use type_map to get the correct type string
            field_type = field.annotation
            type_name = type_map.get(field_type, field_type.__name__)
            f.write(f"    {field_name}: {type_name} | None\n")
        f.write("\n    class Config:\n        orm_mode = True\n\n")

print("Schemas generated in app/schemas_auto.py")