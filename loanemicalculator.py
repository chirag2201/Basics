def calculate_emi(principal,annual_int_rate,tenure_yrs):
    #convert annual interest rate to monthly and percentage
    monthly_int_rate = annual_int_rate / (12*100)
    #convert tenure in years to months
    tenure_months = tenure_yrs * 12

    #calculate emi using the formula
    emi = principal * monthly_int_rate *(1+monthly_int_rate)** tenure_months / ((1+ monthly_int_rate)) ** tenure_months - 1
    return emi

def main():
    print("Loan EMI Calculator")
    print("------------------")

    try:
        #Input: Principal,interest_rate and tenure
        principal = float(input("Enter the loan amount(Principal): "))
        annual_interest_rate = float(input("Enter the loan annual Interest rate: "))
        tenure_years = int(input("Enter the loan tenure years: "))

        #validate inputs
        if principal <=0 or annual_interest_rate<=0 or tenure_years<=0:
            print("All values must be positive!")
            return
        
        #calculate EMI
        emi = calculate_emi(principal,annual_interest_rate,tenure_years)

        #Display result
        print(f"\nYour monthly EMI is: Rs {emi:.2f}")
        print(f"\nTotal Repayment amount: Rs {emi*tenure_years*12:.2f}")
        print(f"\nTotal interest payable: Rs{(emi*tenure_years*12)-principal:.2f}")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")

if __name__ == "__main__":
    main()