from contextlib import contextmanager

from sqlalchemy import *
from sqlalchemy.orm import *

engine = create_engine('sqlite:///school.db', connect_args={'check_same_thread': False})

Base = declarative_base()

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = Session()
    try:
        yield db
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()