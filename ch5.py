#challange1
Musicians = ["Aqours","μ's"]
#challenge2
Numazu = (35,138)
Shirakawago = (36,137)
Locations = [Numazu,Shirakawago]
#challange3
my_body = {"height":172,"favorite song":"I'm watch dog"}
#challange4
key = input("keyを入力")
if key in my_body:
    print(my_body[key])
else:
    print("値が存在しない")
#challange5
aqours_songs = ["未熟DREAMER","想いよひとつになれ"]
muse_songs = ["Snow halation","僕らはいまの中で"]
music_dic = {"aqours":aqours_songs,"muse":muse_songs}
print(music_dic)
