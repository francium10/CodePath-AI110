# We are going to build a simple shopping cart application
# in Python.
# But this time we will include detailed specifications of
# what the code should do


# Write a function with the following specification:
# This function takes a named discount code and applies it to a shopping cart of items.
# function name: discount_calc
# arguments: a list of items dicts
# code
# cart(a list of item dicts)
# code(a string representing a discount code)
# all_codes(dict mapping discounts codes to their percent discount)

# An item dict has three key value pairs:
# Name-the name of the item
# Price-the per unit price of the item
# Quantity-the quantity of the items

# The function should return a dict with the following keys
# originalCart-the original cart passed in (before discount)
# discounted cart-the cart after discount is applied (same as input cart)

def discount_calc(cart, code, all_codes, originalCart=None):
    """Apply a discount code to a shopping cart.

    Args:
        cart (list[dict]): list of item dicts with keys 'Name', 'Price', 'Quantity'.
        code (str): discount code to apply.
        all_codes (dict): mapping of discount code -> percent discount (0-100).
        originalCart (list[dict], optional): original cart to return (if different).

    Returns:
        dict: {
            'originalCart': <list of items before discount>,
            'discounted cart': <list of items after discount (same as input cart)>,
        }
    """

    # Use a copy of the cart so callers do not accidentally mutate it
    cart_copy = [item.copy() for item in cart]
    original = originalCart if originalCart is not None else [
        item.copy() for item in cart]

    # Calculate subtotal
    subtotal = 0.0
    for item in cart_copy:
        price = float(item.get("Price", 0))
        qty = int(item.get("Quantity", 0))
        subtotal += price * qty

    # Apply discount
    discount_percent = float(all_codes.get(
        code, 0)) if code in all_codes else 0.0
    valid_code = code in all_codes
    discount_amount = subtotal * (discount_percent / 100.0)
    total = subtotal - discount_amount

    return {
        "originalCart": original,
        "discounted cart": cart_copy,
    }


if __name__ == "__main__":
    # Basic test case for discount_calc
    demo_cart = [
        {"Name": "T-shirt", "Price": 20.0, "Quantity": 2},
        {"Name": "Hat", "Price": 15.0, "Quantity": 1},
    ]
    codes = {"SPRING10": 10, "WELCOME": 5}

    result = discount_calc(demo_cart, "SPRING10", codes)

    # Validate return structure
    assert isinstance(result, dict), "Expected result to be a dict"
    assert "originalCart" in result, "Missing 'originalCart' in result"
    assert "discounted cart" in result, "Missing 'discounted cart' in result"

    # Ensure the returned carts match the input data
    assert result["originalCart"] == demo_cart
    assert result["discounted cart"] == demo_cart

    # Ensure the function does not mutate the original list object
    assert result["originalCart"] is not demo_cart
    assert result["discounted cart"] is not demo_cart

    print("All discount_calc tests passed")
