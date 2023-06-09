import string

# put your code here

model = string.Template("Dear $username! "
                        "It was really nice to meet you. "
                        "Hopefully, you have a nice day! "
                        "See you soon, $username!"
                        )

name = input()

message = model.substitute(username=name)

print(message)
