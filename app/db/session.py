from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# SQLite en el propio directorio del proyecto
SQLALCHEMY_DATABASE_URL = "sqlite:///./app.db"

# connect_args sólo para SQLite
engine = create_engine(SQLALCHEMY_DATABASE_URL,
                       connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False,
                            autoflush=False,
                            bind=engine)
