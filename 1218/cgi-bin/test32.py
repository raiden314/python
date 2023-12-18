import cgi
import sys,io
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, 
    encoding='utf-8'
)

print("Content-Type: text/html; charset=utf-8")
print("")

#辞書型で保存
form = cgi.FieldStorage()

for k in form.keys():
    print( k, " = ", form.getvalue(k), "<br>" )