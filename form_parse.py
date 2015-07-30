from BeautifulSoup import BeautifulSoup as bs

html_data = """
<form action="demo_form.asp" method="get">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
Gender:
<input type="radio" name="gender" value="female">Female
<input type="radio" name="gender" value="male">Male

<input type="checkbox" name="food" value="fruit">Fruit
<input type="checkbox" name="food" value="veg">Veg
Comment: <textarea name="comment" rows="5" cols="40"></textarea>
  <input type="submit" value="Submit">

<select>
  <option value="volvo">Volvo</option>
  <option value="saab">Saab</option>
  <option value="opel">Opel</option>
  <option value="audi">Audi</option>
</select>

</form>
"""

html_proc = bs(html_data)
for e in html_proc.findAll('input', {'type':'text'}):
	print "What is your", e['name'],"?"
for s in html_proc.findAll('select'):
	print "Which of the following do you prefer? Select 1."
	for i,o in enumerate(s.findAll('option')):
		print "\t",i,o.getText()
print "Choose one of the following:"
for i,e in enumerate(html_proc.findAll('input', {'type':'radio'})):
	print "\t",i,e['value']
print "Choose any subset of the following:"
for i,e in enumerate(html_proc.findAll('input', {'type':'checkbox'})):
        print "\t",i,e['value']

