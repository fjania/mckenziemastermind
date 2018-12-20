from font import letters

message = ['coming', 'soon']
message = ['abc']
longest = max(len(w) for w in message)

output = ""
for word in message:
    output += "<div class='word'>\n"
    for letter in word:
        output += "\t<div class='letter'>\n"
        #for bit in letters[letter]:
        for bit in letters['a']:
            state = "on" if bit else "off"
            output += "\t\t<div class='peg {}'></div>\n".format(state)
        output += "\t</div>\n"
        output += "\t<div class='spacer'></div>\n"
    output += "</div>\n"
print(output)
