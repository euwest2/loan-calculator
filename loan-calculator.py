import streamlit as st
import math

st.write("What do you want to calculate?")
st.write('type "n" for number of monthly payments,')
st.write('type "a" for annuity monthly payment amount,')
st.write('type "p" for loan principal:')

option = st.text_input("> ")
if option == "n":
    loan_prin = float(st.number_input("Enter the loan principal: "))
    mon_pay = float(st.number_input("Enter the monthly payment: "))
    loan_int = float(st.number_input("Enter the loan interest: ")) / 1200
    num_periods = math.ceil(math.log((mon_pay / (mon_pay - (loan_int * loan_prin))), (1 + loan_int)))
    if num_periods == 1:
        st.write("It will take", num_periods, "month to repay this loan")
    if num_periods < 12:
        st.write("It will take", num_periods, "months to repay this loan")
    if num_periods > 12:
        num_periods_years = math.floor(num_periods / 12)
        num_periods_months = num_periods - (num_periods_years * 12)
        st.write("It will take", num_periods_years, "years and", num_periods_months, "months to repay this loan!")

if option == "a":
    loan_prin = float(st.number_input("Enter the loan principal: "))
    num_periods = float(st.number_input("Enter the number of periods: "))
    loan_int = float(st.number_input("Enter the loan interest: ")) / 1200
    mon_pay = round((loan_prin * ((loan_int * pow(1 + loan_int, num_periods))/(pow(1 + loan_int, num_periods) - 1))),2)
    st.write("Your monthly payment = $", mon_pay)

if option == "p":
    mon_pay = float(st.number_input("Enter the annuity payment: "))
    num_periods = float(st.number_input("Enter the number of periods: "))
    loan_int = float(st.number_input("Enter the loan interest: ")) / 1200
    loan_prin = round((mon_pay / ((loan_int * pow(1 + loan_int, num_periods))/(pow(1 + loan_int, num_periods) - 1))),2)
    st.write("Your loan principal = $", loan_prin)