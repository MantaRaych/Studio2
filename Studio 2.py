################################################################
# Program Filename: Studio 2.py
# Author: Rachel Lindgren
# Date: 4/6/2022
# Description: Calculate cost of gas-powered vs electric car
# Input: MPG or MPGe
# Output: Average cost over a year
################################################################

#Givens
Mpy = 14032 #Miles an Oregonian drives per year
GalEquiv = 33.7 #kWh
ORGasPrice = 4.72 #$ per gallon
CAGasPrice = 5.92 #$ per gallon
CorvPrice_kWh = 0.1116 #$/kWh
ChargePrice_kwH = 0.30 #$/kWh
Gas_Sedan = 30 #mpg
Hybrid_Sedan = 45 #mpg
Gas_SUV = 20 #mpg
Hybrid_SUV = 30 #mpg
Tesla = 126 #mpge
Bolt = 108 #mpge

#Calculating gallons used per year
Gal_per_Year = 14032/30

#Cost per year
OR_Cost_per_year = Gal_per_Year * 4.72