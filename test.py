from sortbyquery import sort_by_query as sbq

# corpus example with the name of many european football clubs and their city
docs = [["titulo 1","real madrid barcelona atletico de madrid manchester united ac milan paris saint germain bayern munchen"],
        ["titulo 2","real madrid barcelona atletico nacional manchester city inter psg leverkusen madird unido"],
        ["titulo 3","real sociedad aston villa atletico de madrid newcastle inter psg leverkusen"],
        ["titulo 4","real madrid madrid madrid atletico de madrid manchester united internacionale madrid madrid madrid marseilla dormunt"],
        ["titulo 5","real valladolid barcelona real oviedo real sociedad panatinaikos chelsea milan"]]

# query to compare
query = "madrid"
new_doc = sbq(query,docs)

for doc in new_doc:
    print("doc: ",doc[0]," ratio: ", doc[2])