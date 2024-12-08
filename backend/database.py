from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from google.cloud import bigquery
import os

# Muat variabel dari file .env
load_dotenv()

# # Load variabel lingkungan dari file .env
# load_dotenv()

# # Konfigurasi database
# DB_USERNAME = os.getenv("DB_USERNAME")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_HOST = os.getenv("DB_HOST", "localhost")
# DB_NAME = os.getenv("DB_NAME")
# DB_PORT = os.getenv("DB_PORT", "3306")

# # String koneksi MySQL
# DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# # Konfigurasi SQLAlchemy
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

# # Dependency untuk mendapatkan sesi database
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



# Inisialisasi klien BigQuery
client = bigquery.Client()

def get_data_from_bigquery(query: str):
    """
    Menjalankan query BigQuery dan mengembalikan hasilnya sebagai list of dictionaries.
    """
    query_job = client.query(query)  # Jalankan query
    results = query_job.result()    # Ambil hasil query

    # Konversi hasil ke list of dictionaries
    data = [dict(row) for row in results]
    return data