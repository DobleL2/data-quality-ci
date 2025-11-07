"""Data validation module using pandera."""
import pandas as pd
import pandera as pa
from pandera import Column, DataFrameSchema, Check


# Define schema for customer data
customer_schema = DataFrameSchema({
    "customer_id": Column(int, checks=Check.greater_than(0)),
    "name": Column(str, checks=Check(lambda x: len(x) > 0, element_wise=True)),
    "email": Column(str, checks=Check.str_matches(r'^[^@]+@[^@]+\.[^@]+$')),
    "age": Column(int, checks=Check.in_range(18, 100)),
    "registration_date": Column(str, checks=Check.str_matches(r'^\d{4}-\d{2}-\d{2}$'))
})


def validate_customers(file_path: str) -> bool:
    """
    Validate customer data against schema.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        True if validation passes, raises ValidationError otherwise
    """
    df = pd.read_csv(file_path)
    customer_schema.validate(df)
    return True

def sum(x,y):
    return x+y