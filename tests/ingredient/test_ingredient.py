from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    presunto = Ingredient("presunto")

    assert presunto.name == "presunto"

    assert presunto.__hash__() == hash("presunto")

    assert presunto.__repr__() == "Ingredient('presunto')"

    assert presunto.__eq__("salmão") is False

    assert presunto == Ingredient("presunto")

    ham_restrictions = {Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}

    assert presunto.restrictions == ham_restrictions
