import pandas as pd
import numpy as np

chat_id = 712647540 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # вычитаем измерения случайной величины с распределением -11 + exp(1)
    x = x - np.random.uniform(-11, np.exp(1), size=len(x))
    return x.mean() # Ваш ответ
