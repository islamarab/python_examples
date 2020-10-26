try:
    a = 5/1
    b = a+""
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("everything is fine")
finally:
    print("cleaning up...")

# --------------------------------------------------------


class ValueTooHighError(Exception):
    pass
