from app.database import engine
from app.models import Base

print("Borrando tablas viejas...")
Base.metadata.drop_all(bind=engine)
print("Creando tablas nuevas...")
Base.metadata.create_all(bind=engine)
print("¡Listo!")
