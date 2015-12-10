import re
text = "Guido will be out of the office from 12/15/2012 - 1/3/2013"
print("This is given text: " + text)
# A regex pattern for a date.
datepat = re.compile('(\d+)/(\d+)/(\d+)')

#Find and print all dates
for m in datepat.finditer(text):
    print(m.group())
print("Done Printing dates")

# Find all dates, but print in a different format
monthnames = [None, 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', \
                'Sep', 'Oct', 'Nov', 'Dec']

for m in datepat.finditer(text):
    print ("%s %s, %s" % (monthnames[int(m.group(1))], m.group(2), m.group(3)))
print("Done printing dates in different pattern")

# Replace all dates with fields in the European format (day/month/year)
def fix_date(m):
    return "%s/%s/%s" % (m.group(2), m.group(1), m.group(3))
newtext = datepat.sub(fix_date, text)
print (newtext)
#And alternative replacement
newtext = datepat.sub(r'\2/\1/\3', text)
print (newtext)
