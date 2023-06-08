from django.test import TestCase, Client
from django.urls import reverse
from core.models import Presenca

class PresencaViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.cadastrar_url = reverse('cadastrar_presenca')
        self.listar_url = reverse('listar_presencas')

    def test_cadastrar_aluno_post_status_code(self):
        response = self.client.post(self.cadastrar_url, {'nome_professor': 'Orlando'})
        self.assertEqual(response.status_code, 200)  

    def test_cadastrar_aluno_post_objetos_presenca(self):
        response = self.client.post(self.cadastrar_url, {'nome_professor': 'Orlando'})
        self.assertEqual(Presenca.objects.count(), 0)                

    def test_cadastrar_aluno_get_status_code(self):
        response = self.client.get(self.cadastrar_url)
        self.assertEqual(response.status_code, 200)  

    def test_cadastrar_aluno_get_response(self):
        response = self.client.get(self.cadastrar_url)
        self.assertTemplateUsed(response, 'cadastrar_presenca.html')         

    def test_listar_alunos_status_code(self):        
        response = self.client.get(self.listar_url)
        self.assertEqual(response.status_code, 200) 

    def test_listar_alunos_response(self):        
        response = self.client.get(self.listar_url)
        self.assertTemplateUsed(response, 'listar_presencas.html')          

    def test_listar_alunos_registro(self):
        Presenca.objects.create(nome_professor='Orlando')
        response = self.client.get(self.listar_url)     
        self.assertEqual(len(response.context['registros']), 1)  

    def test_status_code_cadastrar_presenca(self):
        response = self.client.get(self.cadastrar_url)
        self.assertEqual(response.status_code, 200)  

    def test_status_code_listar_presencas(self):
        response = self.client.get(self.listar_url)
        self.assertEqual(response.status_code, 200) 

    def test_template_cadastrar_presenca(self):
        response = self.client.get(self.cadastrar_url)
        self.assertTemplateUsed(response, 'cadastrar_presenca.html')  

    def test_template_listar_presencas(self):
        response = self.client.get(self.listar_url)
        self.assertTemplateUsed(response, 'listar_presencas.html')

    def test_text_listar_nome_professor(self):
        response = self.client.get(self.listar_url)
        self.assertContains(response, 'Nome do Professor')

    def test_text_listar_nome_aluno(self):
        response = self.client.get(self.listar_url)   
        self.assertContains(response, 'Nome do Aluno')

    def test_text_nome_cadastro_professor(self):
        response = self.client.get(self.cadastrar_url)
        self.assertContains(response, 'nome_professor')

    def test_text_nome_cadastro_aluno(self):
        response = self.client.get(self.cadastrar_url)   
        self.assertContains(response, 'nome_aluno')        
