colors = ["czerwony", "zółty", "zielony", "niebieski", "czarny"]
i = 0
while i < len(colors):
    print("Kiedy miałem %d lat, moim ulubionym kolorem był %s." % (i, colors[i]))
    i = i + 1

for x in colors[:]:
    print("Kolory", x)
