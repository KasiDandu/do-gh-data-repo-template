import re


def standardise_column_name(name: str) -> str:
    """'  Claim Ref # ' -> 'claim_ref'"""
    return re.sub(r"[^0-9a-zA-Z]+", "_", name.strip()).strip("_").lower()
