"""Tests for data validation."""
import pytest
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.validate_data import validate_customers


def test_valid_customer_data():
    """Test that valid customer data passes validation."""
    data_path = os.path.join(os.path.dirname(__file__), "..", "data", "raw", "customers.csv")
    assert validate_customers(data_path) is True


def test_invalid_email_format():
    """Test that invalid email format fails validation."""
    import pandas as pd
    from src.validate_data import customer_schema
    
    invalid_data = pd.DataFrame({
        "customer_id": [1],
        "name": ["Test User"],
        "email": ["invalid-email"],  # Invalid email format
        "age": [25],
        "registration_date": ["2023-01-01"]
    })
    
    with pytest.raises(Exception):
        customer_schema.validate(invalid_data)


def test_invalid_age_range():
    """Test that age outside valid range fails validation."""
    import pandas as pd
    from src.validate_data import customer_schema
    
    invalid_data = pd.DataFrame({
        "customer_id": [1],
        "name": ["Test User"],
        "email": ["test@example.com"],
        "age": [15],  # Age below minimum (18)
        "registration_date": ["2023-01-01"]
    })
    
    with pytest.raises(Exception):
        customer_schema.validate(invalid_data)

