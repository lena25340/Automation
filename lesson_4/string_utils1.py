class StringUtils:
    def capitilize(self, string: str) -> str:

        """
        Принимает на вход тексти возвращает этот же текст
        Пример: `capitilize("Butterfly") -> "Butterfly"
        Пример: 'capitilize("%?№")->"%?№"
        Пример: 'capitilize("0")->"0"
        """
        return string.capitalize()
        
        
    def end_with(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка заканчивается
        заданным символом и `False` - если нет \n
        Параметры: \n
        Пример: `end_with("", "0") -> "" ->False`
        Пример: `end_with("🤗🤗🤗")->"🤗🤗🤗"->False`
        Пример: `end_with("لائكت")->"لائكت->False`
        """
        return string.endswith(symbol)
