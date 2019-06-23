# ユーザーに入力させる
# input関数はユーザーの入力をstrデータ型で受け取る
age = input("Enter your age:")
# 整数に変換
int_age = int(age)
if int_age < 24:
    print("You are young!")
else:
    print("Wow, you are old!")
