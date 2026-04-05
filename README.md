# Clínica Backend

Backend da aplicação web desenvolvida para a gestão interna de pacientes de uma clínica de saúde integrativa.

O sistema foi criado para substituir o uso de planilhas e fichas físicas, centralizando os dados dos pacientes em uma API simples, funcional e organizada.

---

## 📌 Objetivo do projeto

O projeto foi desenvolvido com o objetivo de resolver problemas de organização e acesso às informações dos pacientes em clínicas que ainda utilizam planilhas e registros manuais, oferecendo uma solução digital centralizada, simples e eficiente.

---

---

## 🌐 Deploy

A API está disponível em:

👉 https://clinica-backend-3awl.onrender.com

---

## 📌 Funcionalidades

* Cadastro de pacientes
* Listagem de pacientes
* Atualização de dados cadastrais
* Exclusão de pacientes
* Armazenamento dos dados em MongoDB

---

## 🛠 Tecnologias utilizadas

* Python
* Flask
* Gunicorn
* Flask-CORS
* PyMongo
* MongoDB
* python-dotenv
* PyJWT

---

## ▶️ Como rodar o projeto localmente

### 1. Clonar o repositório

```bash
git clone <url-do-repositorio>
cd <nome-do-repositorio>
```

### 2. Criar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
MONGO_URI = string de conexao
SECRET_KEY = chave secreta
MONGO_DB_NAME = nome do banco
JWT_SECRET_KEY = chave secreta jwt
```

### 5. Rodar o servidor

```bash
python run.py
```

---

## 📡 Endpoints da API

### 🔹 GET /pacientes

Retorna a lista de todos os pacientes

### 🔹 POST /pacientes

Cria um novo paciente

### 🔹 PUT /pacientes/:id

Atualiza os dados de um paciente

### 🔹 DELETE /pacientes/:id

Remove um paciente

---

## 📄 Exemplo de requisição

### Criar paciente

```json
POST /pacientes

{
  "nome": "João Pedro",
  "data_nascimento": "2006-10-03",
  "contato": "(11)99999-9999",
  "especialidade": "Fisioterapia",
  "observacoes": "Paciente com dores na lombar"
}
```

---

## 🗂 Modelagem dos dados

### Paciente

```json
{
  "_id": "ObjectId",
  "nome": "string",
  "data_nascimento": "string",
  "contato": "string",
  "especialidade": "string",
  "observacoes": "string"
}
```

---

## 🏗 Estrutura do projeto

```
app/
├── routes/
├── services/
├── utils/
├── __init__.py
├── config.py
run.py
```



