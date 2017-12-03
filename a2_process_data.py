#######################################################
### You can ignore the following lines of code.
### It loads the contents of a CSV file for you.
### The file's name should be a2_input.csv.
### You do NOT need to know how it works.
#######################################################

import csv

contents = []
with open("a2_input.csv") as input_file:
    for row in csv.reader(input_file):
        contents = contents + [row]

#######################################################
### Do your data processing below.
### The below code gives some examples
### of how to access the data.
### Print your results using the print function.
#######################################################

print ("""
<!DOCTYPE html>
<html>
	<head>
		<title>Score of Watched Films in Turkey</title>
		<meta charset='UTF-8'>
	</head>")
	<body style= 'background-color: black;'>""")
print ('<table align = "center">')
print ("<style>")
print ("""table, th, td {
border: 1px solid White;
font-size: 20px;
padding: 20px;
color: White;
font-family: "Courier";
text-align: center;
}
h1 {
font-family: "Courier";
font-size: 30px;
color: White;
}
p {
font-family: "Courier";
font-size: 20px;
color: White;
}
ul, li {
padding: 15px;
font-family: "Courier";
font-size: 20px;
color: White;
}""")
print ("</style>")
print ("<tr>")
print ("	<th>")
print contents[0][0]
print ("	</th>")
print ("	<th>")
print contents[0][1]
print ("	</th>")
print ("	<th>")
print contents[0][2]
print ("	</th>")
print ("	<th>")
print contents[0][3]
print ("	</th>")
print ("	<th>")
print contents[0][4]
print ("	</th>")
print ("</tr>")
for i in range (2,20):
	print ("<tr>")
	print ("	<td>")
	print contents[i][0]
	print ("	<td>")
	print contents[i][1]
	print ("	</td>")
	print ("	<td>")
	print contents[i][2]
	print ("	</td>")
	print ("	<td>")
	print contents[i][3]
	print ("	</td>")
	print ("	<td>")
	print contents[i][4]
	print ("	</td>")
	print ("</tr>")
print ("</table>")
for i in range (2,16):
	if (str(contents[i+1][1]) > str(contents[i][1])):
		print ("<p>Number of Native Movies <b><i>increased</i></b> in " + contents[i+1][0] + ".</p>")
	else:
		print ("<p>Number of Native Movies <b><i>decreased</i></b> in " + contents[i+1][0] + ".</p>")
print ("<h1>Percentage of Native Movies:</h1>")
print ("<ul>")
x=1
while x<18:
	d = str(contents[x][0])
	a = float(contents[x][1])
	b = a + float(contents[x][2])
	c = a/b *100
	print ("	<li>" + str(d) + ": %" + str(c) + "</li>")
	x +=1
print ("</ul>")
print type(contents)
print ("""<p>Summary: As seen in the table above,
Turkish people watch foreign movies more than native movies.
But the difference between them have been decreasing year by
year. People have been getting more interested in native movies.
</p>""")
print ("""
<p>Link for the source:
<a href="http://www.tuik.gov.tr/">www.tuik.gov.tr</a>
</p>""")
print ("</body>")
print ("</html>")
