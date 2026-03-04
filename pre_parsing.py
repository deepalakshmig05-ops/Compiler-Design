table = {
('E','i'):"E->TR",
('E','('):"E->TR",
('R','+'):"R->+TR",
('R',')'):"R->e",
('R','$'):"R->e"
}

for key,value in table.items():
    print(key,"=>",value)