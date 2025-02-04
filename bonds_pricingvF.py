import pandas as pd 
import numpy as np
import datetime 
from datetime import datetime, timedelta 
from dateutil.relativedelta import relativedelta 

def bond_pricing(face_value, coupon_rate, freq, yield_to_maturity, purchase_date, next_coupon_date, maturity_date):
    purchase_date = datetime.strptime(purchase_date, "%Y-%m-%d")
    next_coupon_date = datetime.strptime(next_coupon_date, "%Y-%m-%d")
    maturity_date = datetime.strptime(maturity_date, "%Y-%m-%d")

    starting_date =  next_coupon_date
    date_rows = [next_coupon_date]
    while starting_date < maturity_date: 
        if freq ==  1:
            starting_date = starting_date.replace(year=(starting_date.year + 1))
            date_rows.append(starting_date)
        elif freq == 2: 
            starting_date = starting_date + relativedelta(month=6)
            date_rows.append(starting_date)
        else:
            raise ValueError("Compounding frequency should be either annual (1) or semiannual (2).")
        
    t_list = []
    for x in date_rows:
        t_list.append((x - purchase_date).days / 365 )
    
    data_rows = [dt.strftime("%Y-%M-%d") for dt in date_rows]

    c_rows = []
    for x in t_list:
        c_rows.append(np.round(face_value * coupon_rate, 2))
    c_rows[-1] += face_value

    pv_rows = []
    for x,y in zip(c_rows, t_list):
        pv_rows.append(np.round(x / (1 + yield_to_maturity) ** y, 2))

    payments_data = [data_rows, c_rows, pv_rows]
    payments_columns = ["Payments Dates", "Coupons", "Present Values"]
    payments_df = pd.DataFrame(payments_data, payments_columns)
    payments_df = payments_df.transpose()

    pv_times_t = []
    for x, y in zip(pv_rows, t_list):
        pv_times_t.append(x * y)

    tsquared = []
    for x in t_list:
        tsquared.append(x ** 2)

    pv_times_tsquared = []
    for x, y in zip(pv_rows, tsquared):
        pv_times_tsquared.append(x * y)

    calculations_data = [t_list, pv_times_t, tsquared, pv_times_tsquared]
    calculations_columns = ["t Values", "PV times t Values", "t squared Values","PV times t squared Values"]
    calculations_df = pd.DataFrame(calculations_data, calculations_columns)
    calculations_df = calculations_df.transpose()

    if freq == 1:
        last_coupon_date = next_coupon_date.replace(year =(next_coupon_date.year -1))
    elif freq == 2: 
        last_coupon_date = next_coupon_date - relativedelta(months=6)
    
    accrued_interests = np.round((purchase_date - last_coupon_date).days * coupon_rate * face_value / 365, 2)
    dirty_price = np.round(sum(payments_df["Present Values"]), 2)
    clean_price = np.round(dirty_price - accrued_interests, 2)
    mc_duration = np.round(sum(calculations_df["PV times t Values"]) / clean_price, 2)
    m_duration = np.round(mc_duration / (1 + yield_to_maturity), 2)
    convexity = np.round(sum(calculations_df["PV times t squared Values"]) / clean_price, 2)

    pricing_data = [dirty_price, accrued_interests, clean_price, mc_duration, m_duration, convexity]
    pricing_columns = ["Dirty Price", "Accrued Interests", "Clean Price", "Macaulay Duration", "Modified Duration", "Convexity"]
    pricing_df = pd.DataFrame(pricing_data, pricing_columns)

    return payments_df, pricing_df

payments_df, pricing_df = bond_pricing(1000, 0.02125, 1, 0.04, "2024-09-15","2024-09-29", "2029-09-29")

def bond_price_fluctuation(change_in_ytm):

    modified_duration = pricing_df.iloc[4, 0]
    convexity = pricing_df.iloc[5, 0]
    clean_price = pricing_df.iloc[2, 0]

    change_in_bond_price = np.round((-modified_duration * change_in_ytm) + 0.5 * convexity * (change_in_ytm / 100) ** 2 * 100, 4)
    new_bond_price = np.round(clean_price * (1 + change_in_bond_price), 2)

    fluctuation_data = [change_in_ytm, change_in_bond_price, new_bond_price]
    fluctuation_columns = ["Change in YTM", "Change in bond price", "New bond price"]

    bond_price_fluctuation_df = pd.DataFrame(fluctuation_data, fluctuation_columns)

    return bond_price_fluctuation_df

bond_price_fluctuation_df = bond_price_fluctuation(0.01)

print(payments_df)
print(pricing_df)
print(bond_price_fluctuation_df)


