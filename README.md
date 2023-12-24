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


print(request.resolver_match.view_name) # my_app1:index

print(request.resolver_match.app_name) # my_app1

print(request.resolver_match.url_name) # index