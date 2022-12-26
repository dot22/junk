

credit = 40e6
years = 5
procent = 6

koef = procent * ((1 + procent) ** years) / ((1 + procent) ** years - 1)
annuitet = koef * credit
print(annuitet)