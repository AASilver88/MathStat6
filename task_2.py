from math import sqrt

# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью,
# получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 Предполагая, что результаты
# измерений подчинены нормальному закону распределения вероятностей, оценить истинное значение величины X при
# помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95.

sample = [6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1]
# Z для 97.5% (2.5 + 95%) равна 1.96
Z = 1.96

M = sum(sample ) / len(sample)
std = sqrt(sum((x - sum(sample ) / len(sample)) ** 2 for x in sample) / (len(sample)))


confidence_interval_a = M - Z * (std / sqrt(len(sample)))
confidence_interval_b = M + Z * (std / sqrt(len(sample)))
# Ответ: (6.32;6.85)
print(f"Ответ: Интервал покрывающий значение Х с доверительной вероятностью 0,95 ({confidence_interval_a}, {confidence_interval_b}).")