from datetime import date , time , datetime

#calling the today
#function of date class
today = date.today()
now = datetime.now()
print("today's date is ",today)
print("\ncurrent date and time is ",now)

#printings date's components
print("\ndate componets", today.year, today.month, today.day)