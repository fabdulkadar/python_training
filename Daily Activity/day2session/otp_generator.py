import random

def gen_otp(length=6):
    otp=''
    for _ in range(length):
        otp+=str(random.randint(0,9))
    return otp

if __name__=="__main__":
    otp=gen_otp(4)
    print(f"Your OTP is : {otp}")
