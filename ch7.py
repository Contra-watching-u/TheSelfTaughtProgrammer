#1
dramas =["ウォーキング・デッド","アントラージュ","ザ・ソプラノズ","ヴァンパイア・ダイアリーズ"]
for drama in dramas:
     print(drama)
#2
for i in range(25,51):
    print(i)
#3
for index, show in enumerate(dramas):
    print(index)
    print(show)
#4
answers = ["3","9"]
while True :
    inpt =input("数字を入力してください。qを入力すると終了します。")
    if inpt in answers:
        print("当たり！")
    elif inpt == "q":
        print("ゲームを終了します")
        break
    else:
        print("数字を入力するか、qで終了します。")

#5
lst1 = [8,19,148,4]
lst2 = [9,1,33,83]
mix_lst = []
for i in lst1:
    for j in lst2:
#i,jはinの次のリスト内の数字なので[i]としてはならない。i、jこそがリストの中身。 mix_lst.append(lst1[i]*lst2[j])
#この下正解
        mix_lst.append(i*j)        
print(mix_lst)
