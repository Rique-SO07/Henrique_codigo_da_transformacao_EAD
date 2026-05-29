from django.test import TestCase
from django.urls import reverse
from .models import Produto

class ProdutoCRUDTestCase(TestCase):

    def setUp(self):
        # Cria um produto de exemplo antes de iniciar os testes
        self.produto = Produto.objects.create(
            nome="Teclado Mecânico",
            descricao="Teclado RGB Switch Blue",
            preco=199.90,
            quantidade=10
        )

    def test_modelo_produto_criado_com_sucesso(self):
        """Garante que os dados foram gravados corretamente no modelo"""
        self.assertEqual(self.produto.nome, "Teclado Mecânico")
        self.assertEqual(self.produto.quantidade, 10)

    def test_rota_listagem_produtos(self):
        """Garante que a página inicial carrega a lista com sucesso (Status 200)"""
        resposta = self.client.get(reverse('listar_produtos'))
        self.assertEqual(resposta.status_code, 200)
        self.assertContains(resposta, "Teclado Mecânico")

    def test_rota_cadastro_produto_via_post(self):
        """Garante que enviar dados via POST cria um novo produto de verdade"""
        dados_novos = {
            "nome": "Mouse Gamer",
            "descricao": "Mouse 10000 DPI",
            "preco": "89.90",
            "quantidade": 5
        }
        resposta = self.client.post(reverse('cadastrar_produto'), data=dados_novos)
        # Verifica se o sistema redireciona de volta após salvar (Status 302)
        self.assertEqual(resposta.status_code, 302)
        # Confirma se o item foi pro banco de dados
        self.assertTrue(Produto.objects.filter(nome="Mouse Gamer").exists())