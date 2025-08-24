"""Pytest configuration and fixtures."""

import pytest
from pathlib import Path
import tempfile
import os


@pytest.fixture
def temp_ctf_file():
    """Create a temporary CTF file for testing."""
    content = [
        '05' + '0' + '0' + '4111111111111111' + '001' + ' ' * 142,
        '06' + '0' + '0' + '5555444433332222' + '002' + ' ' * 142,
    ]

    # Ensure all records are exactly 168 characters
    content = [record[:168].ljust(168) for record in content]

    with tempfile.NamedTemporaryFile(mode='w', suffix='.ctf', delete=False) as f:
        f.write('\n'.join(content))
        temp_file_path = f.name

    yield temp_file_path

    # Cleanup
    if os.path.exists(temp_file_path):
        os.unlink(temp_file_path)


@pytest.fixture
def sample_transaction():
    """Sample transaction data for testing."""
    return {
        'Transaction Code': '05',
        'Transaction Description': 'Sales Draft',
        'Account Number': '4111111111111111',
        'Source Amount': '000000100050',
        'Source Currency Code': '840',
        'Merchant Name': 'TEST MERCHANT',
        'Merchant City': 'NEW YORK',
        'Merchant Country Code': 'USA',
        'Purchase Date (MMDD)': '1215',
        'TCRs_Present': ['0', '1', '5']
    }

