nota=int(input("ingresa tu nota: "))

if nota==20:
    regalo="Iphone"
elif nota>=18:
    regalo="Samsung"
elif nota>=16:
    regalo="Nokia"
elif nota>=14:
    regalo="Chocolate"
else:
    regalo="nada"

print(f"te ganaste un {regalo} como premio.")
    
