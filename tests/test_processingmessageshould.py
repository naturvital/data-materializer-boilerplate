from src.main import materialize


def test_succeed():
  result = materialize()
  assert result is not None
