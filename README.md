# Freitas Supermarket Cashier

Postgresql 15 (Compose) + Django 5.0 + Python 3.12

- Vendas
- Cadastrar cliente
- Usuários
- Caixa
- Controle de estoque


Criar Baseview herdando variável NEXT por contexto:

context['NEXT'] = f'?next={request.path}'

context['NEXT'] = f'?next={self.request.path}'

?next={{request.path}}