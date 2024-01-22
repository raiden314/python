import cgi
import os.path
import sys,io
import html
sys.stdout = io.TextIOWrapper(
    sys.stdout.buffer, 
    encoding='utf-8'
)
# print("Content-Type: text/html; charset=utf-8")
# print("")

FILE_LOG = "chat-log.txt"

def print_html( body ):
    print("Content-Type: text/html; charset=utf-8")
    print("")
    print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>チャット</h1>
    <div>
        <form action="cgi-bin/chat.py" >
            名前：<input type="text" name="name" size="8">
            本文：<input type="text" name="body" size="20">
            <input type="submit" value="発言">
            <input type="hidden" name="mode" value="write">
        </form>
    </div>
    <hr>
    {0}
</body>
</html>
""".format( body ))
    
def jump(url):
    print("Status: 301 Moved Permanently")
    print("Location: " + url)
    print("")
    print("<html><head>")
    print("<meta http-equiv='refresh' content='0';"+url+">")
    print("</html></head>")

def mode_write( form ):
    name = form.getvalue("name", "no name")
    body = form.getvalue("body", "")
    name = html.escape(name)
    body = html.escape(body)

    with open(FILE_LOG, "a+", encoding="utf-8") as f:
        f.write("<p>{0}: {1}</p><hr>\n".format(name,body))
    jump("chat.py")
def mode_read():
    log = ""
    if os.path.exists(FILE_LOG):
        with open(FILE_LOG, "r", encoding="utf-8") as f:
            log = f.read()
    print( log )
    print_html( log )


form = cgi.FieldStorage()
# for k in form.keys():
#     print( k, " = ", form.getvalue(k), "<br>" )

mode = form.getvalue("mode", "")
if mode == "write":
    mode_write( form )
else:
    mode_read()