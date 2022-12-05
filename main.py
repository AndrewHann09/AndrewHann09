import datetime

# Defaults
f = open("OSICDef.dat", "r")

PolicyNum = int(f.readline())
BasicRate = float(f.readline())
Discount = float(f.readline())
Liability = float(f.readline())
GlassCov = float(f.readline())
LoanCov = float(f.readline())
HstRate = float(f.readline())
ProcessingFee = float(f.readline())
End = "Y"

# Inputs
while End == "Y":
    FirstName = input("Please enter your first name: ").title()
    LastName = input("Please enter your last name: ").title()
    Address = input("Please enter your address: ")
    City = input("Please enter the city you live in: ")
    Province = input("Please enter the province you live in: ")
    PostCode = input("Please enter your postal code: ")
    PhnNum = input("Please enter your phone number: ")
    NumCarsInsure = int(input("Please enter the number of cars being insured: "))
    LiabilityOpt = input("Would you like extra liability up to $1000000 (Y or N): ").upper()
    OptGlassCoverage = input("Would you like the optional glass coverage (Y or N): ").upper()
    OptLoanerCar = input("Would you like the optional loaner car (Y or N): ").upper()
    FullorMonth = input("Would you like to pay in full or monthly (F or M): ").upper()


# Calculations
    TotExtraCosts = 0
    InsurancePremiums = 0
    if NumCarsInsure == 1:
        InsurancePremiums = BasicRate
    elif NumCarsInsure > 1:
        InsurancePremiums = (BasicRate * Discount) * NumCarsInsure

    if OptGlassCoverage == "Y":
        TotExtraCosts += (GlassCov * NumCarsInsure)
    else:
        GlassCov = 0

    if OptLoanerCar == "Y":
        TotExtraCosts += (LoanCov * NumCarsInsure)
    else:
        LoanCov = 0

    if OptLoanerCar == "Y" or OptGlassCoverage == "Y":
        TotExtraCosts += (Liability * NumCarsInsure)
    else:
        Liability = 0

    TotInsurePrem = (TotExtraCosts + InsurancePremiums)
    TotalCost = (TotInsurePrem * HstRate)
    MonthlyPay = TotalCost / 8 + ProcessingFee

# Policies information
    f = open("Policies.dat", "a")
    f.write("{}, ".format(PolicyNum))
    f.write("{}, ".format(FirstName))
    f.write("{}, ".format(LastName))
    f.write("{}, ".format(Address))
    f.write("{}, ".format(City))
    f.write("{}, ".format(Province))
    f.write("{}, ".format(PostCode))
    f.write("{}, ".format(PhnNum))
    f.write("{}, ".format(NumCarsInsure))
    f.write("{}, ".format(LiabilityOpt))
    f.write("{}, ".format(OptGlassCoverage))
    f.write("{}, ".format(OptLoanerCar))
    f.write("{}, ".format(FullorMonth))
    f.write("{}\n".format(TotalCost))



# Receipt
    if FullorMonth == "F":
        print("One Stop Insurance Company")
        print()
        print("Customer                                                           Amount")
        print("Information               Options                                   Due")
        print("===========================================================================================")
        print(f"{PolicyNum}          Number of cars insured: {NumCarsInsure}                         {InsurancePremiums}")
        print(f"{FirstName}                Liability: {LiabilityOpt}                                 {Liability}")
        print(f"{LastName}                Glass coverage: {OptGlassCoverage}                               {GlassCov}")
        print(f"{Address}          Loaner car: {OptLoanerCar}                             {LoanCov}")
        print(f"{City}             Payment method: {FullorMonth}                        Total due: {float(TotalCost)}")
        print(f"{Province}")
        print(f"{PostCode}")
        print(f"{PhnNum}")
    elif FullorMonth == "M":
        print("One Stop Insurance Company")
        print()
        print("Customer                                                           Amount")
        print("Information               Options                                   Due")
        print("===========================================================================================")
        print(f"{PolicyNum}          Number of cars insured: {NumCarsInsure}                             {InsurancePremiums}")
        print(f"{FirstName}                Liability: {LiabilityOpt}                                 {Liability}")
        print(f"{LastName}                Glass coverage: {OptGlassCoverage}                               {GlassCov}")
        print(f"{Address}          Loaner car: {OptLoanerCar}                             {LoanCov}")
        print(f"{City}             Payment method: {FullorMonth}                        Total due per month: {float(MonthlyPay)}")
        print(f"{Province}")
        print(f"{PostCode}")
        print(f"{PhnNum}")


    End = input("Would you like the stop or enter another policy (Y or N): ").upper()

    if End == "N":
        print("Policy information processed and saved")
        break







