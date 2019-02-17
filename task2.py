# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый
# сдвиг вправо и влево на два знака. Объяснить полученный результат.

print(f'5 OR 6 = {5|6}')
print(f'5 AND 6 = {5&6}')
print(f'5 XOR 6 = {5^6}')
print(f'Сдвиг вправо 5 = {5>>1}')
print(f'Сдвиг влево 5 = {5<<1}')

# Двоичные операции. 5 это 0b0101, 6 это 0b0110
# Сдвиг вправо это по сути деление на 2 (последняя цифра выпадает): 0b0010
# Сдвиг влево по сути умножение на 2 (дописывается ноль в конце): 0b1010
# OR (если хотя бы один бит из двух 1, то резуьтат бита 1): 0b0101 | 0b0110 = 0b0111 (7)
# AND (результат 1, если оба бита из двух 1): 0b0101 & 0b0110 = 0b0100 (4)
# XOR (если биты одинаковые то результат 0, разные - 1): 0b0101 | 0b0110 = 0b0011 (3)