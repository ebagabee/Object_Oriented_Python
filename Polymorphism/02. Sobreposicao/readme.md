# Sobreposição

![](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/cVTThOL-530x400.png)

Hora de escrever a lógica que determina se dois retângulos se sobrepõem!

## Atribuição

**Complete o `overlaps()`método** . Ele deve verificar se o retângulo atual ( `self`) se sobrepõe a um retângulo fornecido ( `rect`).

Retorna `True`se `self`sobrepõe a qualquer parte de `rect`, incluindo apenas tocar as laterais. Retorna `False`caso contrário.

## Pontas

Todas as condições a seguir devem existir `True`para que os retângulos (vamos chamá-los `A`de e `B`) se sobreponham:

- O lado esquerdo de A está no lado direito de B ou à esquerda dele
- O lado direito de A está à direita ou à direita do lado esquerdo de B
- O lado superior de A está sobre ou acima do lado inferior de B
- O lado inferior de A está sobre ou abaixo do lado superior de B
