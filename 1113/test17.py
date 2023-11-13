val = 100

def func():
    global val
    val = 20

func()
print("val = ", val)