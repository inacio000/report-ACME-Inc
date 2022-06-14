file = open("users.txt", "r")
lines = file.readlines()
file.close()

users = []
spaces = []
total = 0

for l in lines:
    line = l.split()
    users.append(line[0])
    spaces.append(int(line[1]))
total = sum(spaces)

report = open("report", "w")
report.write("ACME Inc.                           Disk space usage by users\n")
report.write("-------------------------------------------------------------\n")
report.write("Nr.      User                Usage space                % of use\n")

for c in range(0, len(users)):
    space_in_MB = spaces[c] / float(1024 ** 2)
    percentage_of_use = spaces[c] / total
    two_digits = f'{space_in_MB:.2f}'
    report.write(f"{c+1:<8} {users[c]:<15} {two_digits:>10} MB\t\t\t\t\t{(percentage_of_use * 100):.2f}\n")

float(report.write('\nTotal space occupied: %.2f\n' %(total / (1024 ** 2))))
float(report.write(f"Avarage space occupied: %.2f" %(total / len(users) / (1024 ** 2))))

report.close()
