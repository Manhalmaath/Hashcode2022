file = open('a_an_example.in.txt', 'r')
file = file.readlines()
print(file)
without_newline = []
for i in file:
    without_newline.append(i.rstrip('\n'))
number_of_contributors = int(file[0].split(' ')[0])
number_of_projects = int(file[0].split(' ')[1])
skills = []
print(without_newline)
for contributor in range(1, number_of_contributors):
    for skill in range(1,without_newline[contributor].split(' ')[1]):
        skills.append(skill)
print(skills)