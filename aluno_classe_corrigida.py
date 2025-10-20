from pymongo import MongoClient

class AlunoClass:
    def __init__(self, nome, sobrenome, nota, aluno_id=None):    
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota
        self.aluno_id = aluno_id       

    def mostrarAluno(self):
        return f'Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota}'

    def salvar(self, conexao, colecao):
        dados_aluno = {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'nota': self.nota
        }

        if self.aluno_id is not None:
            dados_aluno['aluno_id'] = self.aluno_id

  
        resultado = conexao[colecao].insert_one(dados_aluno)
        print(f'Aluno salvo com o ID: {resultado.inserted_id}')

if __name__ == "__main__":
    # Conectando ao MongoDB
    cliente = MongoClient('mongodb://localhost:27017/')
    db = cliente['sua_banco_de_dados']  
    
    aluno = AlunoClass(nome='João', sobrenome='Silva', nota=9.5)
    aluno.salvar(conexao=db, colecao='alunos') 
