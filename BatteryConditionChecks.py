from BMSThresholdLevels import limits
def isBatteryOk(temperature,soc,chargeRate):
    return (isTemperatureOk(temperature) and isSocOk(soc)) and isChargeRateOk(chargeRate)

def isTemperatureOk(temperature):
    if not (CheckFactorOk(limits['temperature']['min'], limits['temperature']['max'], temperature)):
        print("Temperature is out of range and is " + CheckFactorHigh(limits['temperature']['max'] , temperature))
        return False
    else:
        return True
    
def isSocOk(soc):
    if not (CheckFactorOk(limits['state_of_charge']['min'], limits['state_of_charge']['max'], soc)):
        print("State of charge is out of range and is " + CheckFactorHigh(limits['state_of_charge']['max'], soc))
        return False
    else:
        return True
    
def isChargeRateOk(chargeRate):
    if (CheckFactorHigh(limits['charge_rate']['max'], chargeRate)=="high"):
        print("Charge Rate is out of range")
        return False
    else:
        return True
    
def CheckFactorHigh(maximum,factorvalue):
    return "high" if(factorvalue>maximum) else "low"
    
def CheckFactorOk(minimum, maximum, factorvalue):
    return not (factorvalue < minimum or factorvalue > maximum)
