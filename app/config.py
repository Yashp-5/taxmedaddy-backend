import os
DB_URL= os.getenv("DATABASE_URL", "postgresql://user:password@localhost/tax_db")
SECRET_KEY=os.getenv("SECRET_KEY","supersecretkey")
ALGORITHM="H256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
