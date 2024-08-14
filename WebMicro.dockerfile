# Gunakan image Python 3.11.3 sebagai dasar
FROM python:3.11.3-slim

# Salin requirements dan install dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Salin semua kode sumber
COPY . .

# Jalankan aplikasi Flask
CMD ["python", "main.py"]
