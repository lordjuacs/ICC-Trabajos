def f():
    global s
    print(s)
    s = "ELectronica tambien"
    print(s)


s = "CS es la voz"
f()
print(s)
