import psycopg2

# Konfigurasi koneksi ke database PostgreSQL
try:
    koneksi = psycopg2.connect(
        host="192.168.0.170",       # Sesuaikan dengan alamat server PostgreSQL
        dbname="latihan1",          # Nama database
        user="steven",              # Username PostgreSQL
        password="kucing",          # Password
        port=5432                   # Port default PostgreSQL
    )

    kursor = koneksi.cursor()

    # Perintah ALTER TABLE
    perintah_sql = """
    ALTER TABLE printer.bagians
    ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ADD COLUMN IF NOT EXISTS updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
    """

    # Eksekusi perintah SQL
    kursor.execute(perintah_sql)
    koneksi.commit()

    print("Kolom created_at dan updated_at berhasil ditambahkan ke printer.bagians")

except Exception as e:
    print("Terjadi kesalahan:", e)
    if koneksi:
        koneksi.rollback()

finally:
    if 'kursor' in locals(): kursor.close()
    if 'koneksi' in locals(): koneksi.close()

