#returning how much i payed staff
def get_pay(todays_pay):
    return todays_pay

#multiplying the listing fee by the amount of parcels and returning the answer
def get_listing_fee(listing_fee):
    return listing_fee * 0.36

#returning how much postage i paid, when i sent the parcel
def get_postage(postage):
    return postage

#returning how much moeny was paid to me for the product
def get_sales(sales):
    return sales

#returning how much money was paid to me for postage of my parcel
def get_postage_paid(postage_paid):
    return postage_paid

#adding to the variable 'total_postage_paid'
total_postage_paid = 0
total_postage_paid += get_postage_paid(9.90)
total_postage_paid += get_postage_paid(9.90)
total_postage_paid += get_postage_paid(7.40)
total_postage_paid += get_postage_paid(10.10)
total_postage_paid += get_postage_paid(9.90)
#total_postage_paid += get_postage_paid()
#total_postage_paid += get_postage_paid()
#total_postage_paid += get_postage_paid()
#total_postage_paid += get_postage_paid()
#total_postage_paid += get_postage_paid()

#adding to the variable 'total_sales'
total_sales = 0
total_sales += get_sales(17.10) 
total_sales += get_sales(21.85)
total_sales += get_sales(7.70)
total_sales += get_sales(58.82)
total_sales += get_sales(41.80)
#total_sales += get_sales()
#total_sales += get_sales()
#total_sales += get_sales()
#total_sales += get_sales()
#total_sales += get_sales()

#adding to the variable 'total_postage'
total_postage = 0
total_postage += get_postage(2.88)
total_postage += get_postage(7.36)
total_postage += get_postage(6.40)
total_postage += get_postage(11.56)
total_postage += get_postage(9.60)
#total_postage += get_postage()
#total_postage += get_postage()
#total_postage += get_postage()
#total_postage += get_postage()
#total_postage += get_postage()

#adding to the variable 'total_listing_fee'
total_listing_fee = 0
total_listing_fee += get_listing_fee(3.0)
total_listing_fee += get_listing_fee(3.0)
total_listing_fee += get_listing_fee(2.0)
total_listing_fee += get_listing_fee(4.0)
total_listing_fee += get_listing_fee(3.0)
#total_listing_fee += get_listing_fee()
#total_listing_fee += get_listing_fee()
#total_listing_fee += get_listing_fee()
#total_listing_fee += get_listing_fee()
#total_listing_fee += get_listing_fee()
#total_listing_fee += get_listing_fee()

#adding to the variable 'blus_total_pay'
blus_total_pay = 0
blus_total_pay += get_pay(0.30)
blus_total_pay += get_pay(0.30)
blus_total_pay += get_pay(0.20)
blus_total_pay += get_pay(0.40)
blus_total_pay += get_pay(0.30)
#blus_total_pay += get_pay()
#blus_total_pay += get_pay()
#blus_total_pay += get_pay()
#blus_total_pay += get_pay()
#blus_total_pay += get_pay()

#returning the total profit after subtracting expenses and detucting 10% off sales for the final value fee
def sales_data():
    total_profit = 0
    total_profit += ((total_sales / 10) * 9) - total_postage - blus_total_pay - total_listing_fee + total_postage_paid
    return total_profit

#defining 'total_profit'
total_profit = 0
total_profit += sales_data()

#printing the users string
print('We have spent £' + str(round(total_postage, 2)) + ' on postage, £' + str(round(total_listing_fee, 2)) +
' in listing fees and £' + str(round(blus_total_pay, 3)) + ' has gone to Blu. We have made £' + str(round(total_sales, 2)) +
' in sales and are total profit is £' + str(round(total_profit, 2)) + ' after final value fee. ')
