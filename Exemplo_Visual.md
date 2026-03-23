## complexidade

| Caso         | Complexidade | Situação                                     |
|--------------|-------------|-----------------------------------------------|
| Melhor caso  | O(n)        | Lista já está ordenada (com flag de parada)   |
| Caso médio   | O(n²)       | Elementos em ordem aleatória                  |
| Pior caso    | O(n²)       | Lista em ordem inversa (ex: [5, 4, 3, 2, 1])  |
| Espaço       | O(1)        | Não usa memória extra, ordena no próprio lugar|
| Estável?     | ✅ Sim      | Elementos iguais mantêm a ordem original      |


## exemplo visual passo a passo

Lista inicial: `[5, 3, 8, 4, 2]`

```
Passagem 1:
[5, 3, 8, 4, 2] → troca 5 e 3 → [3, 5, 8, 4, 2]
[3, 5, 8, 4, 2] → troca 8 e 4 → [3, 5, 4, 8, 2]
[3, 5, 4, 8, 2] → troca 8 e 2 → [3, 5, 4, 2, 8] ✅ 8 no lugar

Passagem 2:
[3, 5, 4, 2, 8] → troca 5 e 4 → [3, 4, 5, 2, 8]
[3, 4, 5, 2, 8] → troca 5 e 2 → [3, 4, 2, 5, 8] ✅ 5 no lugar

Passagem 3:
[3, 4, 2, 5, 8] → troca 4 e 2 → [3, 2, 4, 5, 8] ✅ 4 no lugar

Passagem 4:
[3, 2, 4, 5, 8] → troca 3 e 2 → [2, 3, 4, 5, 8] ✅ ordenada!
```


## vantagens

- **simples de entender e implementar** — ideal para aprendizado
- **estável** — preserva a ordem de elementos iguais
- **in-place** — não precisa de memória extra (O(1))
- **detecta lista já ordenada** — com a otimização da flag, para cedo no melhor caso


## desvantagens

- **lento para listas grandes** — O(n²) no caso médio e pior caso
- **muitas trocas desnecessárias** — pode fazer O(n²) trocas, enquanto outros algoritmos fazem bem menos
- **superado pelo Insertion Sort** — mesma complexidade, mas mais rápido na prática
- **nunca usado em produção** — linguagens modernas usam algoritmos híbridos como Timsort (Python) e Introsort (C++)

