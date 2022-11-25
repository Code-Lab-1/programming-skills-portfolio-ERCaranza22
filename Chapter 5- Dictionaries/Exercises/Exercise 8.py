# Students with their talents

students = {
    'Kyoko Kirigiri': 'Detective',
    'Peko Pekoyama': 'Swordswoman',
    'Tenko Chabashira': 'Neo Aikido',
    'Kazuichi Souda': 'Mechanic',
    'Kaito Momota': 'Astronaut',
    }

for student, talent in students.items():
    print(f"{student.title()} is an Ultimate {talent.title()}.")

print("\nThe following students are in this list:")
for student in students.keys():
    print(f"- {student.title()}")

print("\nThe following talents in this list:")
for talent in students.values():
    print(f"- {talent.title()}")