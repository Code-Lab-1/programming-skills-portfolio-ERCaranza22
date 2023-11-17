# Test Score

marks = {}.fromkeys(['Code Lab I', 'Digital Storytelling', 'Digital Visual Design'], 100)

print(marks)

for item in marks.items():
    print(item)

print(list(sorted(marks.keys())))