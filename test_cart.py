from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


def test_cart():
    driver = webdriver.Chrome()

    try:
        # Abrir SauceDemo
        driver.get("https://www.saucedemo.com/")

        # Login
        usuario = driver.find_element(By.ID, "user-name")
        password = driver.find_element(By.ID, "password")
        boton_login = driver.find_element(By.ID, "login-button")

        usuario.send_keys("standard_user")
        password.send_keys("secret_sauce")

        boton_login.click()

        # Verificar que estamos en la página de productos
        assert driver.title == "Swag Labs"

        # Buscar el botón "Add to cart" del primer producto
        boton_agregar = driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack"
        )

        assert boton_agregar.is_displayed()

        # Agregar producto al carrito
        boton_agregar.click()

        # Verificar contador del carrito
        contador = driver.find_element(
            By.CLASS_NAME, "shopping_cart_badge"
        )

        assert contador.text == "1"

        # Ir al carrito
        carrito = driver.find_element(
            By.CLASS_NAME, "shopping_cart_link"
        )

        carrito.click()

        # Verificar que estamos en el carrito
        titulo = driver.find_element(
            By.CLASS_NAME, "title"
        )

        assert titulo.text == "Your Cart"

        # Buscar el producto dentro del carrito
        producto = driver.find_element(
            By.CLASS_NAME, "cart_item"
        )

        # Verificar nombre
        nombre_producto = producto.find_element(
            By.CLASS_NAME, "inventory_item_name"
        )

        assert nombre_producto.text == "Sauce Labs Backpack"

        # Verificar precio
        precio_producto = producto.find_element(
            By.CLASS_NAME, "inventory_item_price"
        )

        assert precio_producto.text == "$29.99"

        # Verificar botón Remove
        boton_remover = producto.find_element(
            By.CLASS_NAME, "cart_button"
        )

        assert boton_remover.is_displayed()

    finally:
        driver.quit()