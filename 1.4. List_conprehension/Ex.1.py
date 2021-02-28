words = input().split()
print(*[word for word in words if len(word) % 2 == 0], sep='\n')
# * разопакова листа, separator-a преминава на нов ред
