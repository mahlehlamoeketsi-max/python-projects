#Question 2 - Online Purchase Summariser

#Import required modules
from datetime import datetime
import pickle

#MATHEMATICAL FUNCTIONS


def calculate_vat(price):
    """
    This function calculates 15% VAT.
    """

    vat = price * 0.15

    return vat


def calculate_discount(price, discount_percentage):
    """
    This function calculates the discount amount.
    """

    discount = price * (discount_percentage / 100)

    return discount


def calculate_final_amount(price, vat_amount, discount_amount):
    """
    This function calculates the final amount.
    """

    final_amount = price + vat_amount - discount_amount

    return final_amount

#MAIN PROGRAM

def main():

    print("-------------------------------------")
    print(" ONLINE PURCHASE SUMMARISER ")
    print("-----------------------------------\n")

    #Ask user for item price
    price = float(input("Enter the item price: R"))

    #Ask user for discount percentage
    discount_percentage = float(input("Enter discount percentage: "))

    #Calculate VAT
    vat_amount = calculate_vat(price)

    #Calculate discount
    discount_amount = calculate_discount(price, discount_percentage)

    #Calculate final amount
    final_amount = calculate_final_amount(
        price,
        vat_amount,
        discount_amount
    )

    #Generate timestamp
    purchase_time = datetime.now()

    #Format timestamp
    formatted_time = purchase_time.strftime("%Y-%m-%d %H:%M:%S")

    #DISPLAY PURCHASE SUMMARY


    print("\n========== PURCHASE SUMMARY ==========")

    print(f"Original Item Price : R{price:.2f}")
    print(f"VAT Amount (15%)    : R{vat_amount:.2f}")
    print(f"Discount Amount     : R{discount_amount:.2f}")
    print(f"Final Amount        : R{final_amount:.2f}")
    print(f"Purchase Time       : {formatted_time}")

    #CREATE RECEIPT DICTIONARY
    

    receipt_data = {
        "Original Price": price,
        "VAT Amount": vat_amount,
        "Discount Amount": discount_amount,
        "Final Amount": final_amount,
        "Timestamp": formatted_time
    }

    
    #WRITE TO TEXT FILE


    with open("receipt.txt", "w") as file:

        file.write("========== PURCHASE SUMMARY ==========\n")
        file.write(f"Original Item Price : R{price:.2f}\n")
        file.write(f"VAT Amount (15%)    : R{vat_amount:.2f}\n")
        file.write(f"Discount Amount     : R{discount_amount:.2f}\n")
        file.write(f"Final Amount        : R{final_amount:.2f}\n")
        file.write(f"Purchase Time       : {formatted_time}\n")

    print("\nReceipt saved to receipt.txt")

    
    # SERIALISE DATA USING PICKLE


    with open("receipt.pkl", "wb") as pickle_file:
        pickle.dump(receipt_data, pickle_file)

    print("Receipt serialised successfully to receipt.pkl")


#Run the program
main()