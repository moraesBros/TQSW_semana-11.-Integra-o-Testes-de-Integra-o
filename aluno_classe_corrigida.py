from pymongo import MongoClient
import unittest
from unittest.mock import MagicMock

class AlunoClass:
    def __init__(self, nome, sobrenome, nota, aluno_id=None):    
        self.nome = nome
        self.sobrenome = sobrenome
        self.nota = nota
        self.aluno_id = aluno_id  # ID único para o aluno        

    def mostrarAluno(self):
        return f'Aluno: {self.nome} {self.sobrenome} - Nota: {self.nota}'

    def salvar(self, conexao, colecao):
        # Cria dados do aluno
        dados_aluno = {
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'nota': self.nota
        }

        
        if self.aluno_id is not None:
            dados_aluno['aluno_id'] = self.aluno_id

        # Inserir dados no MongoDB
        resultado = conexao[colecao].insert_one(dados_aluno)
        print(f'Aluno salvo com o ID: {resultado.inserted_id}')

# Classe para testes
class AlunoTest(unittest.TestCase):
    def test_salvarAluno(self):
        
        aluno = AlunoClass(nome='João', sobrenome='Silva', nota=9.5)

        # Stub para a conexão MongoDB
        conexao_stub = MagicMock()
        colecao_stub = conexao_stub['alunos']
        colecao_stub.insert_one.return_value.inserted_id = '123456'

        # Chamando o método salvar
        aluno.salvar(conexao=conexao_stub, colecao='alunos')

        # Verifica o chamado com os dados corretos
        colecao_stub.insert_one.assert_called_once_with({
            'nome': 'João',
            'sobrenome': 'Silva',
            'nota': 9.5
        })

        # Testa se simula a inserção
        print(f'ID do aluno salvo: {colecao_stub.insert_one.return_value.inserted_id}')


if __name__ == '__main__':
    unittest.main()
