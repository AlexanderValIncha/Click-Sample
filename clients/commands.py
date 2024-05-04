##Interfaz que nos permite definir como interactuar con los servicios
##Corresponde simplemente al front end que permite hacer la llamada 
'''Utilizamos Click como framework para la construcción de un comando de CLI en terminal.
Para ello es importante tener en cuenta que para una app tiene que dividirse en los siguientes componentes: 
    i)   Interfaz          : Cómo interactua nuestro software con el exterior.
        i.1  App CLI          : Commandos como es nuestro caso 
        ii.2 App API servidor : Endpoints
    ii)  Lógica de Negocio : Lógica específica de nuestro software, definida como servicios 
    iii) Abstracciones     : Objetos sobre los que camos a interactuar, en nustro caso el Cliente     
'''


import click

from clients.services import ClientService
from clients.models import Client


#Para convertir estas tareas en commandos lo hacemos a través de los commandos

#Group -> convertimos una función en otro decorador, en este caso client
@click.group() 
def clients():
    """Manages the clients lifecycle"""
    pass 

## Comandos básicos 

#Definimos un comando de client y pasamos contexto 
@clients.command()
@click.option('-n','--name',          #Ayuda a pedirle inputs al usuario a través del usuario o a través del comando pv en CLI
              type=str,               #Tipo string
              prompt=True,            #Si no nos dan el nombre vía patron abreviado en el comando se lo pedimos al usuario via input
              help='The client name')
@click.option('-n','--company',
              type=str,
              prompt=True,
              help='The client company')
@click.option('-n','--email',
              type=str,
              prompt=True,
              help='The client email')
@click.option('-n','--position',
              type=str,
              prompt=True,
              help='The client position')
@click.pass_context
def create(ctx,name,company,email,position):
    """Creates a new client"""
    client = Client(name, company, email, position)             #Inicializamos al cliente 
    client_service = ClientService(ctx.obj['clients_table'])    #Inicializamos el servcio cogiendo del contexto el nombre de la tabla (revisar nomenclatura de Click y el decorador pass_context)
    
    client_service.create_client(client)                        #Pasamos la referencia de nuestro cliente concreto 


@clients.command()
@click.pass_context
def list(ctx):
    """List all clients"""
    client_service = ClientService(ctx.obj['clients_table'])

    client_list = client_service.list_clients()
    
    click.echo(' ID  |  Name  |  Company  |  Email  |  Position')
    click.echo('*'*100)
    
    for client in client_list: 
        click.echo('{uid} | {name} | {company} | {email} | {position}'.format(
            uid = client['uid'],
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']
        ))


@clients.command()
@click.argument('client_uid', type=str)
@click.pass_context
def update(ctx, client_uid):
    """Updates a Client"""
    client_service = ClientService(ctx.obj['clients_table'])
    
    client_list = client_service.list_clients()
    
    client = [client for client in client_list if client['uid'] == client_uid]

    if client:
        client = _update_client_flow(Client(**client[0]))
        client_service.update_client(client)
        click.echo('Client updated')
    else:
        click.echo('Client not found')  

def _update_client_flow(client):
    click.echo('Leave empty if you dont want to modify the value')
    
    client.name = click.prompt('New name', type=str, default=client.name)
    client.company = click.prompt('New company', type=str, default=client.company)
    client.email = click.prompt('New email', type=str, default=client.email)
    client.position = click.prompt('New position', type=str, default=client.position)
    
    return client 

@clients.command()
@click.pass_context
def delete(ctx,client_id):
    """Deletes a Client"""
    pass 


#Definimos un alias para apuntar a mi función clients, más facil de invocar después 
all = clients
