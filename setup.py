from setuptools import setup


setup(
    name='pv',              #Como invocar a nuestra linea de comandos 
    version='0.1',          #Version 
    py_modules=['pv'],      #Modulo se va a llamar pv
    install_requires=[      #Necesitamos como requisito de aplicación el modulo Click
        'Click',
    ],
    entry_points='''       
        [console_scripts]
        pv=pv:cli
    ''',                    #Cual es el punto de entrada de nuestra aplicación 
)