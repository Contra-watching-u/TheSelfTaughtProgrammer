answer = input("好きな映画は？")
with open("fav_movie.txt","w") as f:
    f.write(answer)
