def construir_perfil(nome: str, sobrenome: str, **kwargs):
    """Constroi perfis com quantidades de informacoes variadas"""
    kwargs["nome"] = nome
    kwargs["sobrenome"] = sobrenome
    return kwargs


perfil_usuario = construir_perfil(
    "nelson", "costa", localidade="curitiba", campo="data science"
)

print(perfil_usuario)
