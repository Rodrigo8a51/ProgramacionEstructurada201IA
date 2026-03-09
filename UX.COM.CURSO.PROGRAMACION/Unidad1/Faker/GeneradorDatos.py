#importar libreria faker

from faker import Faker
faker = Faker("es_MX")

print("Generando datos Dumpy con Faker")
print(f"Nombre:{faker.name()}")
print(f"Direccion:{faker.address()}")
print(f"Telefono:{faker.phone_number()}")
print(f"Correo:{faker.email()}")