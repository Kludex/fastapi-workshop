from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

engine = create_engine(
    "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_session():
    with SessionLocal() as session:
        yield session
