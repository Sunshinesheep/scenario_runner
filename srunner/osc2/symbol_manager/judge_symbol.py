from srunner.osc2.symbol_manager.base_symbol import BaseSymbol

class JudgeSymbol(BaseSymbol):
    def __init__(self, judge_name, mode_value, scope):
        self.mode_value = mode_value
        super().__init__(judge_name, scope)

    def __str__(self):
        buf = self.name
        buf += "=="
        buf += self.mode_value
        return buf
