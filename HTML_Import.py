import webbrowser

f=open('1.html','w')

message = """<html>
<head>
</head>
<body>
<p> this is how we can create a html file</p>
</body>

</html>"""

f.write(message)
f.close()

webbrowser.open_new_tab("1.html")