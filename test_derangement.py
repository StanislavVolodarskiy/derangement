import random

import derangement


def is_deragement(a):
    return all(i != ai for i, ai in enumerate(a))


class TestDerangementMartinezPanholzerProdinger1:
    def test(self):
        a = derangement.derangementMartinezPanholzerProdinger1(
            30,
            random.Random(42)
        )
        assert len(a) == 30
        assert is_deragement(a)


class TestDerangementMartinezPanholzerProdinger2:
    def test(self):
        a = derangement.derangementMartinezPanholzerProdinger2(
            30,
            random.Random(42)
        )
        assert len(a) == 30
        assert is_deragement(a)


class TestDerangementFisherYates1:
    def test(self):
        a = derangement.derangementFisherYates1(30, random.Random(42))
        assert len(a) == 30
        assert is_deragement(a)


class TestDerangementFisherYates2:
    def test(self):
        a = derangement.derangementFisherYates2(30, random.Random(42))
        assert len(a) == 30
        assert is_deragement(a)
