

from tools.src.problems.domain.value_object.slug import Slug


def test_slug_create():
    list_name = "lista 01"
    slug = Slug(list_name=list_name)

    assert slug.get_slug() == "lista-01"