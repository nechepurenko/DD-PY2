if __name__ == "__main__":
    class OperatingProfit:
        def __init__(self, net_sales_revenue: int, variable_costs: int, fixed_costs: int):
            """
            Базовый класс "Операуионная прибыль"

            :param net_sales_revenue: Чистая выручка от реализации, руб.
            :param variable_costs: Переменные затраты, руб.
            :param fixed_costs: Постоянные затраты, руб.
            """
            self.net_sales_revenue = net_sales_revenue
            self.variable_costs = variable_costs
            self.fixed_costs = fixed_costs

        def __str__(self):
            return f"Операционная прибыль предприятия составляет {self.get_operating_profit}"

        def __repr__(self):
            return f"{self.__class__.__name__}(net_sales_revenue={self.net_sales_revenue}, "\
                   f"variable_costs={self.variable_costs}, fixed_costs={self.fixed_costs})"

        def get_sales_revenue(self, vat_percentage: int | float = 20) -> int | float:
            """
            Определение выручки от реализации (до вычета НДС)

            :param vat_percentage: процентная ставка НДС, %
            :return: Величина выручки от реализации, руб.
            """
            return round((self.net_sales_revenue * (1 + (vat_percentage / 100))), 2)

        def profitability(self) -> str:
            """
            Определение рентабельности выручки (Приыбль полученная с рубля выручки предприятия)

            :return: Величина рентабельности выручки, %
            """
            return f"Рентабельность выручки: {round(((self.get_operating_profit / self.net_sales_revenue) * 100), 2)}"

        @property
        def get_margin_profit(self) -> int:
            """
            Определение суммы покрытия

            :return: Величина суммы покрытия, руб.
            """
            return self.net_sales_revenue - self.variable_costs

        @property
        def get_operating_profit(self) -> int:
            """
            Определение операционной прибыли (прибыли от реализации)

            :return: Величина операционной прибыли, руб.
            """
            return self.net_sales_revenue - (self.variable_costs + self.fixed_costs)

        @property
        def net_sales_revenue(self) -> int:
            return self._net_sales_revenue

        @net_sales_revenue.setter
        def net_sales_revenue(self, new_nsr: int) -> None:
            if not isinstance(new_nsr, int):
                raise TypeError("Чистая выручка от реализации должна быть типа int")
            if not new_nsr >= 0:
                raise ValueError("Чистая выручка от реализации не может быть отрицательным числом")
            self._net_sales_revenue = new_nsr

        @property
        def variable_costs(self) -> int:
            return self._variable_costs

        @variable_costs.setter
        def variable_costs(self, new_vc: int) -> None:
            if not isinstance(new_vc, int):
                raise TypeError("Переменные затраты должны быть типа int")
            if not new_vc >= 0:
                raise ValueError("Переменные затраты не могут быть отрицательным числом")
            self._variable_costs = new_vc

        @property
        def fixed_costs(self) -> int:
            return self._fixed_costs

        @fixed_costs.setter
        def fixed_costs(self, new_fc: int) -> None:
            if not isinstance(new_fc, int):
                raise TypeError("Постоянные затраты должны быть типа int")
            if not new_fc >= 0:
                raise ValueError("Постоянные затраты не могут быть отрицательным числом")
            self._fixed_costs = new_fc


    class GrossProfit(OperatingProfit):
        def __init__(self, net_sales_revenue: int, variable_costs: int, fixed_costs: int, non_op_prof: int, bpa: int):
            """
            Дочерний класс "Валовая прибыль" на основе базового "Операционная прибыль"

            :param non_op_prof: Внереализационная прибыль, руб.
            :param bpa: Продажа ОПФ, руб.
            """
            super().__init__(net_sales_revenue, variable_costs, fixed_costs)
            self.non_op_prof = non_op_prof
            self.bpa = bpa

        def __str__(self):
            return super().__str__() + f"\nВаловая прибыль предприятия составляет {self.get_gross_profit}"

        def __repr__(self):
            return f"{self.__class__.__name__}(net_sales_revenue={self.net_sales_revenue}, "\
                   f"variable_costs={self.variable_costs}, fixed_costs={self.fixed_costs}, "\
                   f"non_op_prof={self.non_op_prof}, bpa={self.bpa})"

        def profitability(self) -> str:
            """
            Определение рентабельности выручки и валовой рентабельности
            Даный метод перезаписывается, так как с появлением новых атрибутов появляется
            возможность расчета нового показателя рентабельности - валового

            :return: Величина рентабельности выручки, %. Величина валовой рентабельности, %.
            """
            return super().profitability() + f"\nВаловая рентабельность: "\
                                             f"{round(((self.get_gross_profit / self.net_sales_revenue) * 100), 2)}"

        @property
        def get_gross_profit(self) -> int:
            """
            Определение валовой прибыли

            :return: Величина валовой прибыли, руб.
            """
            return self.get_operating_profit + self.non_op_prof + self.bpa

        @property
        def non_op_prof(self) -> int:
            return self._non_op_prof

        @non_op_prof.setter
        def non_op_prof(self, new_nop: int) -> None:
            if not isinstance(new_nop, int):
                raise TypeError("Внереализационная прибыль должна быть типа int")
            self._non_op_prof = new_nop

        @property
        def bpa(self) -> int:
            return self._bpa

        @bpa.setter
        def bpa(self, new_bpa: int) -> None:
            if not isinstance(new_bpa, int):
                raise TypeError("Продажа ОПФ должна быть типа int")
            if not new_bpa >= 0:
                raise ValueError("Продажа ОПФ не может быть меньше нуля")
            self._bpa = new_bpa


    class NetProfit(GrossProfit):
        def __init__(self, net_sales_revenue: int, variable_costs: int, fixed_costs: int, non_op_prof: int,
                     bpa: int, income_tax: int | float, property_tax: int | float):
            """
            Дочерний класс "Чистая прибыль" на основе дочернего класса "Валовая прибыль"

            :param income_tax: Налог на прибыль, руб.
            :param property_tax: Налог на имущество, руб.
            """
            super().__init__(net_sales_revenue, variable_costs, fixed_costs, non_op_prof, bpa)
            self.income_tax = income_tax
            self.property_tax = property_tax

        def __str__(self):
            return super().__str__() + f"\nЧистая прибыль предприятия составляет {self.get_net_profit}"

        def __repr__(self):
            return f"{self.__class__.__name__}(net_sales_revenue={self.net_sales_revenue}, "\
                   f"variable_costs={self.variable_costs}, fixed_costs={self.fixed_costs}, "\
                   f"non_op_prof={self.non_op_prof}, bpa={self.bpa}, "\
                   f"income_tax={self.income_tax}, property_tax={self.property_tax})"

        def profitability(self) -> str:
            """
            Определение рентабельности выручки, валовой рентабельности и рентабельности чистой прибыли
            Даный метод перезаписывается, так как с появлением новых атрибутов появляется
            возможность расчета нового показателя рентабельности - рентабельности чистой прибыли

            :return: Величина рентабельности выручки, %. Величина валовой рентабельности, %.
            Величина рентабельности чистой прибыли, %.
            """
            return super().profitability() + f"\nЧистая рентабельность выручки: "\
                                             f"{round(((self.get_net_profit / self.net_sales_revenue) * 100), 2)}"

        @property
        def get_net_profit(self) -> int | float:
            """
            Определение чистой прибыли

            :return: Величина чистой прибыли, руб.
            """
            return self.get_gross_profit - (self.income_tax + self. property_tax)

        @property
        def income_tax(self) -> int | float:
            return self._income_tax

        @income_tax.setter
        def income_tax(self, new_it: int | float) -> None:
            if not isinstance(new_it, int | float):
                raise TypeError("Налог на прибыль должен быть типа int или float")
            if not new_it >= 0:
                raise ValueError("Налог на прибыль не может быть меньше нуля")
            self._income_tax = new_it

        @property
        def property_tax(self) -> int | float:
            return self._property_tax

        @property_tax.setter
        def property_tax(self, new_pt: int | float) -> None:
            if not isinstance(new_pt, int | float):
                raise TypeError("Налог на имущество должен быть типа int или float")
            if not new_pt >= 0:
                raise ValueError("Налог на имущество не может быть меньше нуля")
            self._property_tax = new_pt
    pass
