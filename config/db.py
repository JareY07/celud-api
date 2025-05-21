from sqlalchemy import create_engine, MetaData

DATABASE_URL = "mysql+pymysql://sql5780309:AusnA15wXD@sql5.freesqldatabase.com/sql5780309"

engine = create_engine(DATABASE_URL)

meta = MetaData()
