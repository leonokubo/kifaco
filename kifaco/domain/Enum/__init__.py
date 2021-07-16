from enum import Enum


class KindIngredients(Enum):
    CEREAIS = 1
    PAES = 2
    TUBERCULOS = 3
    HORTALICAS = 4
    FRUTAS = 5
    LEGUMINOSAS = 6
    CARNE = 7
    OVOS = 8
    DERIVADOS_DO_LEITE = 9
    OLEO = 10
    GORDURA = 11


class Measurement(Enum):
    GRAMAS = 1
    COLHER_SOPA = 2
    COPO_CHA = 3
    COLHER_SOBREMESA = 4
    COPO_CAFE = 5
    ML = 6
    KG = 7
    UNIDADE = 8
    XICARA = 9
