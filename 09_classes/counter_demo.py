from counter import Counter

tally = Counter()

tally.reset()
tally.setLimit(2)

tally.click()
tally.click()
tally.click()
tally.click()
tally.click()

result = tally.getString()
print(result)