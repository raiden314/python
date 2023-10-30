tag = '<a href="javascript:void(0)" id="ids" class="cls" alt="python" target="_blank">'
ll={}
x=tag.split(" ")
del x[0]
x[-1] = x[-1].split(">")[0]
for i,tag in enumerate(x):
    tag=tag.split("=")
    x=tag[1].replace("\"","")
    # print(i,x)

    ll[tag[0]]=x

print("課題１：",ll)

print(" ")




dict ={'ele': 'a', 'text': 'テキストリンク', 'attr': {'href': 'javascript:void(0)',
'id': 'ids', 'class': 'cls', 'alt': 'alt', 'target': '_blank'}}
html = "<"

# print(dict)

attr = dict["attr"]
# print(attr)

html = html + dict["ele"] + " href=\"" + attr["href"] + "\"" + " id=\"" + attr["id"] + "\""
html = html + " class=\"" + attr["class"] + "\"" + " alt=\"" + attr["alt"] + "\""
html = html + " target=\"" + attr["target"] + "\">" + dict["text"] + "</" + dict["ele"] + ">"
print("課題２(0)：",html)

print(" ")


yyy={}
html = "<"
a=list(dict.items())
for count,i in enumerate(a):
    yyy[count]=i
# print(yyy)
html = html + yyy[0][1] + " href=\""  + yyy[2][1]["href"] + "\"" + " id=\"" + yyy[2][1]["id"] + "\""
html = html + " class=\"" + yyy[2][1]["class"] + "\"" + " alt=\"" + yyy[2][1]["alt"] + "\""
html = html + " target=\"" + yyy[2][1]["target"] + "\">" + yyy[1][1] + "</" + yyy[0][1] + ">"
print("課題２(1)：",html)