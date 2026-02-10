line = input().split()

pi = 3.14159

A = float(line[0])
B = float(line[1])
C = float(line[2])


TriangleA = (A * C)/2
RadiuscircleA = pi*C**2
TrapeziumA = ((A+B) * C)/2
SquareA = B**2
RectangleA = A * B


print("TRIANGULO: %.3f"% TriangleA)
print("CIRCULO: %.3f"% RadiuscircleA)
print("TRAPEZIO: %.3f"% TrapeziumA)
print("QUADRADO: %.3f"% SquareA)
print("RETANGULO: %.3f"% RectangleA)