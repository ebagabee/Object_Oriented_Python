# Obtenha vantagens

No último capítulo, verificamos se o `(x, y)` **ponto** de uma unidade estava dentro de um retângulo (o sopro do dragão). Mas unidades não são realmente pontos — elas têm suas próprias áreas.

Então, vamos verificar se o corpo de um dragão (um retângulo) está dentro do fogo (também um retângulo). A imagem abaixo contém um exemplo de sopro de fogo atingindo um dragão.

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/cVTThOL-530x400.png)

Mais tarde escreveremos o `overlap`método, mas primeiro escreveremos um método para encontrar as arestas de um retângulo.

## Atribuição

Alteramos as coordenadas para privadas adicionando dois sublinhados a elas. Agora precisamos escrever `getter`métodos para acessá-las.

**Complete os seguintes métodos** :

1. [ ] `get_left_x()`: Retorna o valor x mais à esquerda (menor)
2. [ ] `get_right_x()`: Retorna o valor x mais à direita (maior)
3. [ ] `get_top_y()`: Retorna o valor y mais alto (maior)
4. [ ] `get_bottom_y()`: Retorna o menor valor y (menor valor)

Lembre-se de que estamos trabalhando com um [plano cartesiano](https://en.wikipedia.org/wiki/Cartesian_coordinate_system) padrão .

Explicaremos o `__repr__`método mais tarde, não se preocupe muito com isso.

## Pontas

[Você pode achar úteis as funções min](https://docs.python.org/3/library/functions.html#min) e [max](https://docs.python.org/3/library/functions.html#max) integradas do Python .
