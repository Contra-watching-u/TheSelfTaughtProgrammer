#1
kam="カミュ"
print(kam[0],kam[1],kam[2])
#2
x1 = input("何を書いた？:")
x2 = input("誰に送った？:")
sentence = "私は昨日{}を書いて{}に送った".format(x1,x2)
print(sentence)
#3
print("aldous Huxley was born in 1894.".capitalize())
#4
list = "どこで?だれが?いつ?".split("?")
print(list)
#5
print(" ".join(["The","fox","jumped","over","the","fance","."][0:-1])+".")
#6
print("A screaming comes across the sky".replace("s","$"))
#7
print("Hemingway".index("m"))
#8
phrase ="I'll be back."
#9
print("three"+" three"+" three")
print((" three"*3).strip())
#10
print("4月の晴れた寒い日で、時計がどれも十三時を打っていた"[:10])
