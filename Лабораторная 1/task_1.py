import doctest
from typing import Union


class Costs:
    def __init__(self, variable_costs: Union[int, float], fixed_costs: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Затраты"

        :param variable_costs: Переменные затраты, руб.
        :param fixed_costs: Постоянные затраты, руб.

        Примеры:
        >>> costs = Costs(4000, 6000)
        """
        if not isinstance(variable_costs, (int, float)):
            raise TypeError("Переменные затраты должны быть типа int и float")
        if not variable_costs >= 0:
            raise ValueError("Переменные затраты не могут быть отрицательным числом")
        self.variable_costs = variable_costs

        if not isinstance(fixed_costs, (int, float)):
            raise TypeError("Постоянные затраты должны быть типа int и float")
        if not fixed_costs >= 0:
            raise ValueError("Постоянные затраты не могут быть отрицательным числом")
        self.fixed_costs = fixed_costs

    def margin_profit(self, net_sales_revenue: Union[int, float]) -> Union[int, float]:
        """
        Определение суммы покрытия

        :param net_sales_revenue: Чистая выручка от реализации, руб.
        :raise TypeError: Если чистая выручка от реализации не соответствует типу int или float, то возвращается ошибка
        :raise ValueError: Если величина чистой выручки от реализации число отрицательное, то возвращается ошибка

        :return: Величина суммы покрытия

        Примеры:
        >>> costs = Costs(4000, 6000)
        >>> costs.margin_profit(15400)
        """
        ...

    def share_of_costs(self) -> Union[int, float]:
        """
        Определение доли затрат в их общем объеме

        :return: Доля переменных и постоянных затрат в их общем объеме

        Примеры:
        >>> costs = Costs(4000, 6000)
        >>> costs.share_of_costs()
        """
        ...


class GrossProfit:
    def __init__(self, op_prof: Union[int, float], non_op_prof: Union[int, float], bpa: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Валовая прибыль"

        :param op_prof: Прибыль от реализации, руб.
        :param non_op_prof: Внереализационная прибыль, руб.
        :param bpa: Продажа ОПФ, руб.

        Примеры:
        >>> gross_profit = GrossProfit(10000, 3000, 3000)
        """
        if not isinstance(op_prof, (int, float)):
            raise TypeError("Операционная прибыль должна быть типа int и float")
        self.op_prof = op_prof

        if not isinstance(non_op_prof, (int, float)):
            raise TypeError("Внереализационная прибыль должна быть типа int и float")
        self.non_op_prof = non_op_prof

        if not isinstance(bpa, (int, float)):
            raise TypeError("Продажа ОПФ должна быть типа int и float")
        if not bpa >= 0:
            raise ValueError("Продажа ОПФ не может быть отрицательным числом")
        self.bpa = bpa

    def value_of_gp(self) -> Union[int, float]:
        """
        Определение величины валовой прибыли

        :return: Величина валовой прибыли

        Примеры:
        >>> gross_profit = GrossProfit(10000, 3000, 3000)
        >>> gross_profit.value_of_gp()
        """
        ...

    def net_profit(self, income_tax: Union[int, float], property_tax: Union[int, float]) -> Union[int, float]:
        """
        Определениче чистой прибыли

        :param income_tax: Налог на прибыль, %
        :raise TypeError: Если налог на прибыль не соответствует типу int или float, то возвращается ошибка
        :raise ValueError: Если величина налога на прибыль число отрицательное, то возвращается ошибка

        :param property_tax: Налог на имущество, %
        :raise TypeError: Если налог на имущество не соответствует типу int или float, то возвращается ошибка
        :raise ValueError: Если величина налога на имущество число отрицательное, то возвращается ошибка

        :return: Величина чистой прибыли

        Примеры:
        >>> gross_profit = GrossProfit(10000, 3000, 3000)
        >>> gross_profit.net_profit(20, 2.2)
        """
        ...


class Gdp:
    def __init__(self, value_of_gdp: Union[int, float], population: Union[int, float]):
        """
        Создание и подготовка к работе объекта "ВВП"

        :param value_of_gdp: Величина ВВП, млн. руб.
        :param population: Население, млн. чел.

        Примеры:
        >>> gdp = Gdp(130000000, 146.24)
        """
        if not isinstance(value_of_gdp, (int, float)):
            raise TypeError("Величина ВВП должна быть типа int и float")
        if not value_of_gdp > 0:
            raise ValueError("Величина ВВП не может быть отрицательным числом и не может равняться 0")
        self.value_of_gdp = value_of_gdp

        if not isinstance(population, (int, float)):
            raise TypeError("Население должно быть типа int и float")
        if not population > 0:
            raise ValueError("Население не может быть отрицательным числом")
        self.population = population

    def gdp_per_capita(self) -> Union[int, float]:
        """
        Определение ВВП на душу населения

        :return: ВВП на душу населения

        Примеры:
        >>> gdp = Gdp(130000000, 146.24)
        >>> gdp.gdp_per_capita()
        """
        ...

    def gdp_per_ppp(self, exchange_rate: Union[int, float]) -> Union[int, float]:
        """
        Определение ВВП по ППС

        :param exchange_rate: Обменный курс, цена д.е.
        :raise TypeError: Если обменный курс не соответствует типу int или float, то возвращается ошибка
        :raise ValueError: Если обменный курс число отрицательное, то возвращается ошибка

        :return: величина ВВП по ППС

        Примеры:
        >>> gdp = Gdp(130000000, 146.24)
        >>> gdp.gdp_per_ppp(64.61)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
    pass
