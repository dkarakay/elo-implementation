from trueskill import Rating, quality_1vs1, rate_1vs1

alice, bob = Rating(1200), Rating(1000)
print(f"Alice: {alice}")
print(f"Bob: {bob}")
# assign Alice and Bob's ratings
if quality_1vs1(alice, bob) < 0.50:
    print('This match seems to be not so fair')
alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match

print(f"Alice: {alice}")
print(f"Bob: {bob}")


alice, bob = rate_1vs1(alice, bob)  # update the ratings after the match
print(f"Alice: {alice}")
print(f"Bob: {bob}")