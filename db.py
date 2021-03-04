from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os


engine = create_engine(f'postgresql+psycopg2://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASS"]}@{os.environ["DB_URL"]}/{os.environ["DB_NAME"]}')
Base = declarative_base()



