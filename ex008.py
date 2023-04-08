"""
Questão 14: Peça para o usuário digitar uma velocidade inicial (em m/s), 
uma posição inicial (em m) e um instante de tempo (em s) e imprima a posição de um projétil nesse instante de tempo. 
Use a fórmula matemática: y(t) = y(0) + v(0)*t + (g*(t**2)/2) Onde, g é a aceleração da gravidade (-10m/s²), 
y(t) é a posição final, y(0) é a posição inicial, v(0) é a velocidade inicial e t é o instante de tempo.
"""

v0 = float(input("Digite uma velocidade inicial em m/s\n"))
y0 = float(input("Digite uma posicao inicial em m\n"))
t = float(input("Digite um instante de tempo em s\n"))


y = y0 + v0*t + (10*(t**2)/2)

print("A posição final do projétil no instante de tempo", t, "s é", y, "m.")

