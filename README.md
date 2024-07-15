# TDD-dio
Este repositório contém uma suíte completa de testes para a API de produtos da aplicação Store, abrangendo testes de controller, schema e casos de uso (use cases).

# Em andamento...
projeto em andamento tendo que implementar mais os desafio propostos e fazer melhora

## Recursos Testados
### Controlador:
Criação de Produto (POST): Verifica se um novo produto é criado com sucesso e retornado com o status HTTP 201.
Obtenção de Produto por ID (GET): Testa a busca de um produto existente por seu ID, retornando o status HTTP 200 e os detalhes do produto.
Listagem de Produtos (GET): Verifica se a listagem de produtos retorna uma lista com todos os produtos cadastrados e o status HTTP 200.
Atualização de Produto (PATCH): Testa a atualização parcial de um produto existente, retornando o status HTTP 200 e os detalhes atualizados.
Exclusão de Produto (DELETE): Verifica se um produto é excluído com sucesso, retornando o status HTTP 204 (No Content).

### Schema:
Validação do Schema de Produto: Garante que o schema de entrada para criação e atualização de produtos está validando os dados corretamente, incluindo campos obrigatórios e tipos de dados.

### Casos de Uso (Use Cases):
Criação de Produto: Testa a lógica de criação de um produto, incluindo a validação dos dados e a persistência no banco de dados.
Obtenção de Produto por ID: Testa a lógica de busca de um produto por ID, incluindo o tratamento de casos em que o produto não é encontrado.
Consulta de Produtos: Testa a lógica de consulta de produtos, retornando uma lista de produtos que atendem aos critérios de filtro.
Atualização de Produto: Testa a lógica de atualização de um produto, incluindo a validação dos dados e a atualização no banco de dados.
Exclusão de Produto: Testa a lógica de exclusão de um produto, incluindo o tratamento de casos em que o produto não é encontrado.

## Estrutura do Projeto
![image](https://github.com/user-attachments/assets/d663abc7-dfe0-4bab-9387-345cd7e2ecf1)
