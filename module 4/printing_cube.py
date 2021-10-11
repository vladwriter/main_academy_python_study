default_number = int(input("Input your number:"))
string_form = []

for x in range(1, default_number + 1):
    string_form.append(x)
    count = 0
for x in range(1, default_number + 1):
    print(' '.join(map(str, string_form)))
    count += 1
    for i in string_form:
        string_form[i-count] += 1
