import cgi
import cgitb
import sys,io
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, 
    encoding='utf-8'
)
cgitb.enable()

print("Content-Type: text/html; charset=utf-8")
print("")

#辞書型で保存
form = cgi.FieldStorage()

for k in form.keys():
    print( k, " = ", form.getvalue(k), "<br>" )

if "mode" in form:
    print("<p>mode = ", form["mode"], "</p>")
else:
    print("<p>mode = ない</p>")

# mede = form.getvalue("mode", default=None)
# print("<p>", mode, "</p>")