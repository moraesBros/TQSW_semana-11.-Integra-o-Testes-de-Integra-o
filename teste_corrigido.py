import unittest
from aluno import AlunoClass
from turma import TurmaClass
from conexao import ConexaoClass
import mongomock

class alunoTest(unittest.TestCase):
    @mongomock.patch(servers=(('localhost.com', 27017),))
    def setUp(self):
        print('Teste', self._testMethodName, 'sendo executado...')
        self.aluno = AlunoClass('Fabio', 'Teixeira', 10)
        self.turma = TurmaClass()
        self.turma.cadastrarAlunos([self.aluno])
        self.conexao = mongomock.MongoClient().faculdade  # Usar mongomock para criar um banco de dados temporário

    def test_salvarAluno(self):
        resultado = self.aluno.salvar(self.conexao, 'alunos')  # Coleção 'alunos'
        self.assertTrue(resultado, 'Aluno não foi salvo corretamente!')

    def test_salvarTurma(self):
        resposta = self.turma.salvar(self.conexao, 'turma')
        self.assertEqual(True, resposta, 'Turma cadastrada incorretamente!')

if __name__ == "__main__":
    unittest.main()
