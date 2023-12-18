import sys,io
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, 
    encoding='utf-8'
)
print("Content-Type: text/html; charset=utf-8")

print("")
print("<html><head><meta charset='utf8'></head>")
print("<body><h1>名古屋工学院専門学校</h1></body></html>")