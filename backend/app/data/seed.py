"""Seed utility for local/mock development."""

from app.data.mock_data import STOCKS


def seed() -> int:
    return len(STOCKS)


if __name__ == "__main__":
    print(f"Seeded {seed()} stocks in mock mode")
