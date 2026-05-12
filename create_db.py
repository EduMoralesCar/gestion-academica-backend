from app.database import engine
from app.models import Base

print("Creando las tablas en la base de datos...")
Base.metadata.create_all(bind=engine)
print("¡Tablas creadas exitosamente!")
