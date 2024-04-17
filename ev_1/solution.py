def pregunta_1(numVuelosDeIDa: int, numVuelosDeRegreso:
int) -> float:
    # Tu solución inicia aquí
        cantidad = (numVuelosDeIDa * 180 * 22.5) + (numVuelosDeRegreso * 180 * 22.5)
        return cantidad
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.

def pregunta_2(anguloEnRadianes: float) -> float:
    # Tu solución inicia aquí
    PI=3.1415
    anguloEnSexagesimales = (anguloEnRadianes * 180) / PI
    anguloEnSexagesimales = round(anguloEnSexagesimales, 2)
    return anguloEnSexagesimales
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.    

def pregunta_3(magnitud: float) -> str:
    # Tu solución inicia aquí
    tipoDeSismo = ""
    if magnitud < 2:
        tipoDeSismo = "Micro"
    elif magnitud >= 2 and magnitud < 3:
        tipoDeSismo = "Muy Menor"
    elif magnitud >= 3 and magnitud < 4:
        tipoDeSismo = "Menor"
    elif magnitud >= 4 and magnitud < 5:
        tipoDeSismo = "Ligero"
    elif magnitud >= 5 and magnitud < 6:
        tipoDeSismo = "Moderado"
    elif magnitud >= 6 and magnitud < 7:
        tipoDeSismo = "Fuerte"
    elif magnitud >= 7 and magnitud < 8:
        tipoDeSismo = "Mayor"
    elif magnitud >= 8 and magnitud < 10:
        tipoDeSismo = "Cataclismo"
    elif magnitud >= 10:
        tipoDeSismo = "Meteorico"
    return "El sismo es " + tipoDeSismo
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.

def pregunta_4(peso: float, altura: float) -> str:
    # Tu solución inicia aquí
    tipoDePeso = ""
    imc = peso / (pow(altura, 2))
    if imc < 18.5:
        tipoDePeso = "Bajo Peso"
    elif imc >= 18.5 and imc < 25:
        tipoDePeso = "un peso normal"
    elif imc >= 25 and imc < 30:
        tipoDePeso = "Sobrepeso"
    elif imc >= 30 and imc < 35:
        tipoDePeso = "Obesidad Leve"
    elif imc >= 35 and imc < 40:
        tipoDePeso = "Obesidad Media"
    else:
        tipoDePeso = "Obesidad Morbida"
    return "Ud tiene " + tipoDePeso
    # Tu solución termina aquí. Recuerda retornar lo que hayas calculado.