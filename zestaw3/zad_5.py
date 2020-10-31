
miarka="....".join("|" for x in range(13))
miarka=miarka+"\n"+"".join("{:5d}".format(x) for x in range(13)).lstrip()
print(miarka)