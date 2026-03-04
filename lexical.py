import re

keywords = [
"auto","break","case","char","const","continue","default","do","double",
"else","enum","extern","float","for","goto","if","int","long","register",
"return","short","signed","sizeof","static","struct","switch","typedef",
"union","unsigned","void","volatile","while"
]

operators = ['+','-','*','/','%','=']

def lexical_analyzer(code):

    tokens = re.findall(r'\w+|[+\-*/%=]', code)

    for token in tokens:

        if token in keywords:
            print(token,"is keyword")

        elif token in operators:
            print(token,"is operator")

        elif token.isdigit():
            print(token,"is number")

        else:
            print(token,"is identifier")


with open("program.txt","r") as file:
    code = file.read()

lexical_analyzer(code)