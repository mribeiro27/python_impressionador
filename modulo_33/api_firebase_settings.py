import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Replace 'path/to/your/serviceAccountKey.json' with the actual path to your downloaded JSON file
cred = credentials.Certificate(r'C:\Users\322070\OneDrive - OPEN LABS S.A\Área de Trabalho\python_impressionador\modulo_33\chave_firebase.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

# Criar novos itens no BD
'''doc_ref = db.collection('vendas').document('vendas-hashtag')
doc_ref.update({
    'Funcionarios': {
        "IDF2": {
        'nome': 'Ana',
        'idade': 33,
        'filial': 'MG'
        }
    }
})'''

# Ler informações no BD
'''doc_ref = db.collection('vendas').document('vendas-hashtag')
doc = doc_ref.get()
if doc.exists:
    print(f'Document data: {doc.to_dict()}')
else:
    print('No such document!')'''

# Atualizar informações no BD
doc_ref = db.collection('vendas').document('vendas-hashtag')
doc_ref.update({'preco': 400})