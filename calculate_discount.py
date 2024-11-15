# Function to calculate the final price after applying discount
def calculate_discount(initial_price, discount_rate):
    # Check if the discount is 20% or higher
    if discount_rate >= 20:
        # Calculate the final price after applying the discount
        final_price = initial_price * (1 - discount_rate / 100)
        return final_price
    else:
        # If the discount is lower than 20%, return the original price
        return initial_price

# Prompt the user for the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: $"))
    discount_percent = float(input("Enter the discount percentage: "))
    
    # Calculate the final price after applying the discount
    final_amount = calculate_discount(original_price, discount_percent)
    
    # Print the final price
    if final_amount != original_price:
        print(f"After applying the {discount_percent}% discount, the final price is: ${final_amount:.2f}")
    else:
        print(f"No discount applied. The original price is: ${final_amount:.2f}")

except ValueError:
    print("Please enter valid numbers for price and discount percentage.")
