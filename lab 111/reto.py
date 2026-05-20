# Crear una estructura llamada:
# infraestructura
# Debe contener:
# • nombre empresa 
# • región 
# • administrador 
# • lista de instancias 
# Mostrar únicamente:
# • nombre empresa 
# •	segunda instancia 

infraestructura={

"empresa":"AWS",
"region":"us-east-1",
"administrador":"Victor",
"instancias":["EC2-Web","EC2-DB","EC2-Test"]

}

print(infraestructura["empresa"])
print(infraestructura["instancias"][1])
