import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1] / "src" / "glue"))

from transforms import standardise_column_name  # noqa: E402


def test_spaces_and_symbols():
    assert standardise_column_name("  Claim Ref # ") == "claim_ref"


def test_already_clean():
    assert standardise_column_name("customer_id") == "customer_id"
