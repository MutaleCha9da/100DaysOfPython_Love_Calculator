# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
both_names = name1 + name2
lower_case_string = both_names.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true_total = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("l")
e = lower_case_string.count("e")
love_total = l + o + v + e

total = str(true_total) + str(love_total)

final_total = int(total)

if final_total < 10 or final_total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif final_total >= 40 and final_total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")