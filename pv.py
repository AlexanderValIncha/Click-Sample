# pv.py

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import click
from clients import commands as clients_commands

#print(sys.path)

CLIENTS_TABLE = '.clients.csv'

@click.group()        #Define nuestro punto de entrada a través de click
@click.pass_context   #Nos va a dar un objeto contexto 
def cli(ctx):         #Inicializamos un objeto con un diccionario vacío 
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE

#Regitramos estos comandos a la función CLI a través de add_command
cli.add_command(clients_commands.all)
