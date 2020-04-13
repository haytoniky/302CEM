import math
# https://www.ird.gov.hk/chi/ese/st_comp_2020_21_budget/cstcfrm.htm

def cal_MPF(income):
    if income < 7100 * 12:
        mpf = 0
    elif income >= 30000 * 12:
        mpf = 1500 * 12
    else:
        mpf = income * 0.05
    return math.floor(mpf)


def cal_netIncome(income):
    return income - cal_MPF(income)


def cal_ncIncome(income):
    basic_allowance = 132000
    return cal_netIncome(income) - basic_allowance


def srTax(netIncome):
    rate = 0.15
    return netIncome * rate


def prTax(ncIncome):
    rate = 0.02
    tax = 0
    nci_per_year = 50000

    while ncIncome > 0:
        if ncIncome > nci_per_year:
            tax = tax + nci_per_year * rate
            rate += 0.04
            ncIncome = ncIncome - nci_per_year
            if rate > 0.14:
                tax = tax + ncIncome * 0.17
                break
        else:
            tax = tax + ncIncome * rate
            break

    return math.floor(tax)


def cal_stax(income):
    netIncome = cal_netIncome(income)
    ncIncome = cal_ncIncome(income)

    if netIncome >= 2022000:
        # standard rate tax
        tax = srTax(netIncome)
    else:
        # progressive rate tax
        tax = prTax(ncIncome)

    return math.floor(tax)


def cal_jtax(husband_income, wife_income):
    netIncome = cal_netIncome(husband_income) + cal_netIncome(wife_income)
    ncIncome = cal_ncIncome(husband_income) + cal_ncIncome(wife_income)

    if netIncome >= 3144000:
        # standard rate tax
        tax = srTax(netIncome)
    else:
        # progressive rate tax
        tax = prTax(ncIncome)
    return math.floor(tax)



if __name__ == '__main__':
    # income per year
    answer = input("Are you single or married?")
    if answer == "single":
        your_income = int(input("\nPlease enter your personal input per year:"))
        print("\nYour's MPF : " + str(cal_MPF(your_income)))
        print("\nYour tax payable : " + str(cal_stax(your_income)))

        if your_income >= 2022000:
            # standard rate tax
            print("\nIt is using standard rate tax")
        else:
            # progressive rate tax
            print("\nIt is using progressive rate tax")

    elif answer == "Single":
        your_income = int(input("\nPlease enter your personal income per year:"))
        print("\nYour's MPF : " + str(cal_MPF(your_income)))
        print("\nYour tax payable : " + str(cal_stax(your_income)))

        if your_income >= 2022000:
            # standard rate tax
            print("\nIt is using standard rate tax")
        else:
            # progressive rate tax
            print("\nIt is using progressive rate tax")
    else:

        husband_income = int(input("\nPlease enter husband's personal income per year:"))
        wife_income = int(input("Please enter wife's personal income per year:"))
        print("\nHusband's MPF : " + str(cal_MPF(husband_income)))
        print("Wife's MPF : " + str(cal_MPF(wife_income)))

        print("\nHusband tax payable : " + str(cal_stax(husband_income)))
        print("Wife tax payable : " + str(cal_stax(wife_income)))
        print("\nSeparate taxation : " + str(cal_stax(husband_income) + cal_stax(wife_income)))
        print("Joint taxation : " + str(cal_jtax(husband_income, wife_income)))
        if cal_stax(husband_income) + cal_stax(wife_income) <= cal_jtax(husband_income, wife_income):
            print("\nIt is recommended separate assessment.")
        else:
            print("\nIt is recommended joint assessment.")
