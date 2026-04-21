from contextlib import contextmanager

from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})

Base = declarative_base()
class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    personal = Column(Integer)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    with get_db() as db:
        dept = Department(name="임베디드 소프트웨어과", personal=64)
        db.add(dept)
        db.commit()