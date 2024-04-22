string = "a_abc_de_f_ghi"
template = []
for i in string:
    if i == "_":
        template.append("_")
    else:
        template.append(" ")

templateIdx = 0
for i in string[::-1]:
    if i == "_":
        continue
    if template[templateIdx] == " ":
        template[templateIdx] = i
    else:
        while template[templateIdx] != " ":
            templateIdx = templateIdx + 1
        template[templateIdx] = i
print("".join(template))
