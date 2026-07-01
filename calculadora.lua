local calc = {}

function calc.doy_formateado(y, m, d)
    local time1 = os.time{year=y, month=1, day=1}
    local time2 = os.time{year=y, month=m, day=d}
    local day_num = math.floor(os.difftime(time2, time1) / 86400) + 1
    return string.format("%d%03d", y, day_num)
end

function calc.diferencia_dias(y1, m1, d1, y2, m2, d2)
    local t1 = os.time{year=y1, month=m1, day=d1}
    local t2 = os.time{year=y2, month=m2, day=d2}
    local diff_segundos = os.difftime(t2, t1)
    local dias = math.floor(diff_segundos / 86400)
    return math.abs(dias)
end

function calc.semisuma_formateada(n1, n2)
    -- Convertimos el texto a números reales
    local num1 = tonumber(n1)
    local num2 = tonumber(n2)

    -- Calculamos la semisuma
    local resultado = (num1 + num2) / 2

    -- Separamos la parte entera para formatear los miles con comas
    -- (Por si el resultado da decimal, ej. .5, usamos math.floor)
    local entero = math.floor(math.abs(resultado))
    local decimal = (math.abs(resultado) - entero) * 10 -- Captura el .5 si existe

    -- Formateamos los miles con comas usando expresiones regulares de Lua
    local entero_formateado = tostring(entero):reverse():gsub("(%d%d%d)", "%1,"):reverse():gsub("^,", "")

    -- Reconstruimos el número final con su decimal si no es cero
    local numero_final = entero_formateado
    if decimal > 0 then
        numero_final = entero_formateado .. "." .. string.format("%.0f", decimal)
    end

    -- Determinamos el signo al principio
    if resultado > 0 then
        return "+" .. numero_final
    elseif resultado < 0 then
        return "-" .. numero_final
    else
        return numero_final
    end
end

function calc.diferencia_formateada(n1, n2)
    -- Convertimos el texto a números reales
    local num1 = tonumber(n1)
    local num2 = tonumber(n2)

    -- Calculamos la diferencia (num1 - num2)
    local resultado = num1 - num2

    -- Separamos la parte entera para formatear los miles con comas
    local entero = math.floor(math.abs(resultado))
    local decimal = (math.abs(resultado) - entero) * 10

    -- Formateamos los miles con comas
    local entero_formateado = tostring(entero):reverse():gsub("(%d%d%d)", "%1,"):reverse():gsub("^,", "")

    -- Reconstruimos el número final con su decimal si existe
    local numero_final = entero_formateado
    if decimal > 0 then
        numero_final = entero_formateado .. "." .. string.format("%.0f", decimal)
    end

    -- Determinamos el signo al principio
    if resultado > 0 then
        return "+" .. numero_final
    elseif resultado < 0 then
        return "-" .. numero_final
    else
        return numero_final
    end
end

function calc.porcentaje_memoria_usada(usada, total)

    local usada = tonumber(usada)
    local total = tonumber(total)

    if not usada or not total then
        return "Error"
    end

    local uso = usada / total * 100

    return string.format("%.2f", uso)

end

function calc.porcentaje_memoria_libre(usada, total)

    local usada = tonumber(usada)
    local total = tonumber(total)

    if not usada or not total then
        return "Error"
    end

    local libre = total - usada
    local libre_porcentaje = libre / total * 100

    return string.format("%.2f", libre_porcentaje)

end

return calc
