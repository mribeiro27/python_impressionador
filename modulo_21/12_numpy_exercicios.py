import numpy as np

# considere os seguintes dados aleatórios como início
rng = np.random.default_rng(seed=42)
respostas = rng.integers(low=0, high=10, size=210, endpoint=True)
# print(respostas)

respostas_reshape = np.reshape(respostas, (7, 30))
print(respostas_reshape)

media_geral = np.mean(respostas)
print(f"A média geral de notas é: {media_geral}")

media_diaria = np.mean(respostas_reshape, axis=1)
print(f"A média diária de notas é: {media_diaria}")

