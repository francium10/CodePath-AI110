# Vague types demo:
#  This code is intentionally written with vague types to demonstrate
#  the importance of precise type annotations.
#  The function `calculate_cart_total` accepts
#  an iterable of cart items, but the exact structure
#  of these items is not specified, which can lead to
#  confusion and potential errors. The discount parameters
#  are also vaguely typed, allowing for both percentage and
#  absolute discounts without clear distinction. This code serves
#  as an example of how vague types can make it difficult to understand
#  the expected input and output, and why it's important to use precise
#  types for better code clarity and maintainability.


"""Demo of calculating a shopping cart total with a discount."""

from __future__ import annotations

from typing import Iterable, Mapping, MutableMapping, Optional, TypedDict, Union


class CartItem(TypedDict):
    """A single item in a shopping cart."""

    name: str
    price: float  # price per unit
    quantity: int


def calculate_cart_total(
    items: Iterable[CartItem],
    discount: float = 0.0,
    discount_is_percent: bool = True,
) -> float:
    """Calculate the total cost of a shopping cart.

    Args:
        items: An iterable of cart items. Each item must include `price` and `quantity`.
        discount: Discount value (percent or absolute).
        discount_is_percent: If True, treat `discount` as a percentage (0.0-100.0).
            If False, treat `discount` as an absolute dollar amount.

    Returns:
        The total price after discount, never below 0.
    """

    subtotal = 0.0
    for item in items:
        subtotal += item["price"] * item["quantity"]

    if discount_is_percent:
        discount_amount = subtotal * (discount / 100.0)
    else:
        discount_amount = discount

    total = subtotal - discount_amount
    return max(total, 0.0)


if __name__ == "__main__":
    # Example usage
    example_cart = [
        {"name": "Apples", "price": 1.99, "quantity": 3},
        {"name": "Milk", "price": 2.49, "quantity": 1},
        {"name": "Bread", "price": 3.49, "quantity": 2},
    ]

    print("Cart total (no discount):", calculate_cart_total(
        example_cart))  # pyright: ignore[reportArgumentType]
    print("Cart total (10% off):", calculate_cart_total(
        example_cart, discount=10.0))  # type: ignore
    print(
        "Cart total ($5 off):",
        calculate_cart_total(example_cart, discount=5.0,  # pyright: ignore[reportArgumentType]
                             discount_is_percent=False),  # type: ignore
    )
