class Receita(models.Model):
    
    titulo = models.CharField(max_length=100)  # Título da receita
    ingredientes = models.TextField()          # Ingredientes em formato de texto
    instrucoes = models.TextField()            # Instruções de preparo
    criado_em = models.DateTimeField(auto_now_add=True)  # Data de criação
