#!C:\Users\31415\AppData\Local\Programs\Python\Python38-32\python.exe

print("Content-type:text/html\n\n")
import cgi

enterfile = "<form><label for='fname'>Enter file name:</label><br><input type='file' id='fname' name='fname'><br><input type='submit'></form>"
print(enterfile)
form = cgi.FieldStorage()
#Opens file
with open(form.getvalue("fname")) as f:
    content = f.readlines()

#Csv content to list
rows = [line for line in content]
table = "<table style='border:1px solid black;'>"

#Creating the header(s)
table+= "".join(["<th style='border:1px solid black;'>"+value+"</th>" for value in rows[0].split(",")])
rows=rows[1:]

#This inputs and formats row values via csv (loop)
for row in rows:
    table+= "<tr>" + "".join(["<td style='border:1px solid black;'>"+value+"</td>" for value in row.split(",")]) + "</tr>" + "\n"
table+="</table>"
print(table)
