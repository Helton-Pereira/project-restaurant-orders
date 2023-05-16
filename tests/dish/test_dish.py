from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    pao_com_ovo = Dish("pão com ovo", 4.50)

    assert pao_com_ovo.name == "pão com ovo"

    assert pao_com_ovo.__hash__() == hash("Dish('pão com ovo', R$4.50)")

    assert pao_com_ovo.__eq__(Dish("pão com ovo", 4.50))

    assert pao_com_ovo.__eq__(Dish("pão com queijo", 3.50)) is False

    assert pao_com_ovo.__repr__() == "Dish('pão com ovo', R$4.50)"

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("pizza", "x")

    valuer_error_message = "Dish price must be greater then zero."

    with pytest.raises(ValueError, match=valuer_error_message):
        Dish("sorvete", 0)

    pao_com_ovo.add_ingredient_dependency(Ingredient("ovo"), 1)
    assert pao_com_ovo.recipe == {Ingredient('ovo'): 1}

    assert pao_com_ovo.get_restrictions() == {Restriction.ANIMAL_DERIVED}

    assert pao_com_ovo.get_ingredients() == {Ingredient('ovo')}
