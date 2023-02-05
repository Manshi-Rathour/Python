sci = int(input("science marks : "))
maths = int(input("maths marks : "))
eng = int(input("english marks : "))

req_marks = (sci + maths + eng)/300 * 100

if sci >= 33 and maths >= 33 and eng >= 33 and req_marks >= 40:
    print("Pass!")
else:
    print("Fail!")
