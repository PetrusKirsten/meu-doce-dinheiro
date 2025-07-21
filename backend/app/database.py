from pathlib        import Path
from sqlalchemy     import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


BASE_DIR = Path(__file__).resolve().parent.parent

(Path(BASE_DIR) / "data").mkdir(exist_ok=True)

DATABASE_PATH = BASE_DIR / "data" / "financas.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DATABASE_PATH}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
