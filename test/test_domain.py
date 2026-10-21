import pytest
from decimal import Decimal
from app.domain import Money, Customer, Order, OrderItem, OrderItemLimitExceeded

def test_suma_de_dinero_correcta():
    precio1 = Money(Decimal("100.00"), "MXN")
    precio2 = Money(Decimal("50.00"), "MXN")
    total = precio1.add(precio2)
    assert total.amount == Decimal("150.00")

def test_limite_de_20_unidades_rechaza_excedentes():
    cliente = Customer(id="C01")
    pedido = Order(id="0001", customer=cliente)
    
    
    item_permitido = OrderItem("TV", 15, Money(Decimal("5000.00")))
    pedido.add_item(item_permitido)
    
    
    item_excedente = OrderItem("CABLE", 6, Money(Decimal("200.00")))
    
    with pytest.raises(OrderItemLimitExceeded):
        pedido.add_item(item_excedente)