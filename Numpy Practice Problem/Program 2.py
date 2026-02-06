#Election voting system

votes = [0, 0, 0, 0, 0]
spoilt = 0

for i in range(10):   # assume 10 voters
    v = int(input("Enter candidate number (1-5): "))

    if v >= 1 and v <= 5:
        votes[v-1] += 1
    else:
        print("Spoilt Ballot")
        spoilt += 1

print("Votes for candidates:")
for i in range(5):
    print("Candidate", i+1, ":", votes[i])

print("Number of Spoilt Ballots:", spoilt)