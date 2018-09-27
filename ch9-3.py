import csv
mylist = [["Top Gun","Risky Business","Minority Report"],["Titanic","The Revenant","Inception"],["Training Day","Man on Fire","Flight"]]
with open("movies.csv","w") as f:
    w = csv.writer(f,delimiter=",")
    for row in mylist:
        w.writerow(row)
