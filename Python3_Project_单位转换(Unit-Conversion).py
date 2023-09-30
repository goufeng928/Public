#! /usr/bin/env python3

# Create By GF 2023-07-08

# Python3_Project_单位转换(Unit-Conversion).py

# ----------------------------------------------------------------------------------------------------

import re

# ----------------------------------------------------------------------------------------------------

def FuncUnitConversion(VarOrgString:str):

    ListNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    ListPunctuation = ["."]

    DictUnit = {"百":100,
                "千":1000,
                "万":10000,
                "亿":100000000}
    
    # --------------------------------------------------
    
    PartNumber = re.search("[0-9\.\+\-]*", VarOrgString).group()
    
    PartNotNumber = re.search("[^0-9\.\+\-]", VarOrgString).group()
    
    ListIntAndDec = PartNumber.split(".")
    
    PartInteger = ListIntAndDec[0]
    
    PartDecimal = ListIntAndDec[1]

    # --------------------------------------------------

    Divisor = int
    Divisor = 1

    if len(PartDecimal) == 1:
        Divisor = 10
    elif len(PartDecimal) == 2:
        Divisor = 100

    # --------------------------------------------------

    RtnDigit = float

    RtnDigit = float("%s%s" % (PartInteger, PartDecimal))

    RtnDigit = RtnDigit / Divisor

    if PartNotNumber == "万":
        RtnDigit = RtnDigit * DictUnit["万"]
    elif PartNotNumber == "亿":
        RtnDigit = RtnDigit * DictUnit["亿"]

    # --------------------------------------------------

    print(RtnDigit)

    return RtnDigit

def Running():

    VarOrgString = "21.45亿"

    FuncUnitConversion(VarOrgString)

# ----------------------------------------------------------------------------------------------------

if __name__ == "__main__":

    Running()

# ----------------------------------------------------------------------------------------------------
# EOF
