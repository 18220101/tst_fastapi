from fastapi import FastAPI

app = FastAPI()

listmahasiswa = {
    1: {
        "NIM" : "18220101",
        "Nama" : "Natasha"
    },
    2: {
        "NIM" : "18220014",
        "Nama" : "Pavita"
    },
    3: {
        "NIM" : "18220051",
        "Nama" : "Natanael"
    }
}

@app.get("/")
async def get_mahasiswa():
    return listmahasiswa

@app.post("/")
async def add_mahasiswa(nim: str, nama: str):
    obj = {"NIM": nim, "Nama": nama}
    key = len(listmahasiswa) + 1
    listmahasiswa[key] = obj
    return {"message": "Data added"}