'''Extend 'gym_member.py' to calculate `total_fee` (monthly fee times plan months), add a one-time
 `registration_fee` of ₹500, and store the result in `amount_payable`, then print all three. 
 Use a monthly fee of ₹1200 and a 6-month plan, so the amount payable is ₹7700. Hint: Write numbers
 without commas in code, for example 1200. '''


monthly_fee=1200
month_plan=6
registration_fee=500

total_fee= monthly_fee * month_plan
amount_payable= total_fee + registration_fee

print("Total Fee:-",total_fee)
print("Registration fee:-",registration_fee)
print("Amount Payable :-",amount_payable)



