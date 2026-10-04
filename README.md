# Automatizacion QA - Saucedemo

Proyecto de automatizacion de pruebas funcionales  realizado con Python, Selenium y Pytest  para el curso de Talento Tech

Las pruebas se ejecutan sobre la aplicacion web SauceDemo

## Tecnologias usadas
- Python (Lenguaje utilizado para desarrollar las pruebas)
- Selenium (Automatizacion e interaccion con el navegador)
- Pytest (Framework utilizado para ejecutar y organizar las pruebas)
- Pytest-HTML ( Generacion de reportes de ejecucion)
- Git (Control de versiones)
- Github (Repositorio y gestion del proyecto)

## Estructura del proyecto

Automatizacion-QA-Saucedemo

- test_login.py
- test_inventory.py
- test_cart.py
- reporte.html
- README.md

## Instalacion

Se requiere tener instalado Python

Instalar las dependencias ejecutando:

    ```python
    pip install selenium
    ```

    ```python
    pip install pytest
    ```

    ```python
    pip install pytest-html
    ```

## Ejecutar las pruebas

Para ejecutar todos los casos de prueba:

    ```python
    pytest
    ```

Para ejecutar un archivo especifico:

pytest test_login.py
pytest test_inventory.py
pytest test_cart.py

## Generacion del reporte HTML
Para generar un reporte HTML de las pruebas:

pytest --html=reporte.html --self-containes-html

Luego se puede abrir el archivo reporte.html en un navegador para consultar los resultados de la ejecucion

## Casos de prueba
Login exitoso

Verifica que:
- Se pueda acceder a Saucedemo
- Se ingrese un usuario valido
- Se ingrese una contraseña valida
- El inicio de sesion sea exitoso
- Se acceda correctamente a la pagina de productos
- Se muestre el logo "Swag Labs"
- Se muestre el titulo "Products"

Inventario

Verifica que:
- Se muestre la pagina de productos
- Existan productos disponibles
- El primer producto sea Sauce Labs Backpack
- El precio del producto de $29.99
- Se muestre el menu de navegacion
- Se muestre el filtro de productos

Carrito

Verifica que:
- Se pueda agregar productos al carrito
- El contador del carrito se actualice correctamente
- Se pueda acceder al carrito
- El producto agregado aparezca correctamente
- El nombre del producto sea correcto
- El precio del producto sea correcto
Se muestre la opcion para eliminar el producto

## Objetivo del proyecto 

El objetivo es aplicar conceptos basicos de QA Automation, utilizando Selenium y Pytest para automatizar pruebas fi¿uncionales sobre la aplicacion web

## Autora

Proyecto realizado como parte del curso de Talento Tech - Automatizacion QA




