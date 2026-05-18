import math

x = y = 10
base = 20
#Constantes
math.pi        # 3.141592653589793
math.e         # 2.718281828459045
math.tau       # 6.283185307179586 (2 * pi)
math.inf       # Infinito
math.nan       # Not a Number

#Funções Aritméticas e Básicas
math.ceil(x)       # Arredonda para cima
math.floor(x)      # Arredonda para baixo
math.trunc(x)      # Trunca (remove a parte decimal)
math.fabs(x)       # Valor absoluto (float)
math.factorial(x)  # Fatorial de x
math.fmod(x, y)    # Resto da divisão (float)
math.remainder(x, y) # Resto (com sinal do numerador)
math.gcd(x, y)     # Máximo divisor comum
math.lcm(x, y)     # Mínimo múltiplo comum (Python 3.9+)

#Funções Trigonométricas
math.sin(x)        # Seno (x em radianos)
math.cos(x)        # Cosseno
math.tan(x)        # Tangente
math.asin(x)       # Arco-seno
math.acos(x)       # Arco-cosseno
math.atan(x)       # Arco-tangente
math.atan2(y, x)   # Arco-tangente de y/x (ângulo em radianos)

#Conversão de Ângulos
math.degrees(x)    # Converte radianos → graus
math.radians(x)    # Converte graus → radianos

#Funções Exponenciais e Logarítmicas
math.exp(x)        # e elevado a x
math.expm1(x)      # exp(x) - 1 com mais precisão para x pequeno
math.log(x)        # Logaritmo natural (base e)
math.log(x, base)  # Logaritmo com base personalizada
math.log10(x)      # Logaritmo base 10
math.log2(x)       # Logaritmo base 2

#Funções de Potência e Raiz
math.pow(x, y)     # x elevado a y (sempre float)
math.sqrt(x)       # Raiz quadrada de x

#Funções de Precisão/Erros
math.isfinite(x)   # Verifica se x é finito
math.isinf(x)      # Verifica se x é infinito
math.isnan(x)      # Verifica se x é NaN

#Funções Hiperbólicas
math.sinh(x)       # Seno hiperbólico
math.cosh(x)       # Cosseno hiperbólico
math.tanh(x)       # Tangente hiperbólica
math.asinh(x)      # Arco-seno hiperbólico
math.acosh(x)      # Arco-cosseno hiperbólico
math.atanh(x)      # Arco-tangente hiperbólica