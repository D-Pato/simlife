# Simulador de Vida Real Financiera - MVP en Streamlit

import streamlit as st
import random

# Inicializar estado si no existe
if "juego_iniciado" not in st.session_state:
    st.session_state.juego_iniciado = False
    st.session_state.patrimonio = 0
    st.session_state.felicidad = 50
    st.session_state.estres = 30
    st.session_state.ahorros = random.randint(100000, 500000)
    st.session_state.ingresos_pasivos = 0
    st.session_state.avatar_creado = False

st.title("🧠 Simulador de Vida Real Financiera - DON’T PATO")

if not st.session_state.avatar_creado:
    st.subheader("Crea tu personaje")
    nombre = st.text_input("Nombre")
    edad = st.slider("Edad", 18, 30, 24)
    ciudad = st.selectbox("Ciudad", ["Antofagasta", "Santiago", "Concepción"])
    estilo_vida = st.radio("Estilo de vida", ["Austero", "Normal", "Me lo merezco"])

    if st.button("Iniciar Simulación"):
        st.session_state.nombre = nombre
        st.session_state.edad = edad
        st.session_state.ciudad = ciudad
        st.session_state.estilo_vida = estilo_vida
        st.session_state.avatar_creado = True
        st.session_state.juego_iniciado = True
        st.rerun()

if st.session_state.avatar_creado:
    st.success(f"¡Bienvenido/a {st.session_state.nombre}!")
    st.write(f"Edad: {st.session_state.edad}, Ciudad: {st.session_state.ciudad}, Estilo de vida: {st.session_state.estilo_vida}")

    if "decision1" not in st.session_state:
        st.header("🔀 Primera decisión")
        decision1 = st.radio("¿Qué quieres hacer ahora?", [
            "Estudiar una carrera",
            "Buscar trabajo",
            "Emprender con bajo capital"], key="d1")

        if st.button("Confirmar decisión 1"):
            if decision1 == "Estudiar una carrera":
                st.session_state.patrimonio -= 3000000
                st.session_state.estres += 10
                st.session_state.felicidad += 5
            elif decision1 == "Buscar trabajo":
                st.session_state.patrimonio += 1000000
                st.session_state.estres += 20
                st.session_state.felicidad -= 5
            elif decision1 == "Emprender con bajo capital":
                resultado = random.choice(["éxito", "fracaso"])
                if resultado == "éxito":
                    st.session_state.patrimonio += 2000000
                    st.session_state.felicidad += 10
                else:
                    st.session_state.patrimonio -= 500000
                    st.session_state.estres += 10

            evento = random.choice([
                ("Te enfermaste y tuviste que pagar $200.000 en salud", -200000, 10),
                ("Recibiste una herencia de $1.000.000", 1000000, -5),
                ("Perdiste dinero en una inversión arriesgada", -500000, 15)
            ])
            st.session_state.patrimonio += evento[1]
            st.session_state.estres += evento[2]
            st.session_state.evento1 = evento[0]
            st.session_state.decision1 = decision1
            st.rerun()

    elif "decision2" not in st.session_state:
        st.header("🔀 Primera decisión tomada")
        st.write(f"Decisión: {st.session_state.decision1}")
        st.warning(f"⚠️ Evento aleatorio: {st.session_state.evento1}")

        st.header("🔄 Segunda decisión")
        decision2 = st.radio("¿Cómo quieres manejar tus finanzas ahora?", [
            "Invertir en criptomonedas",
            "Ahorrar en un fondo seguro",
            "Gastar en un viaje para despejarte"], key="d2")

        if st.button("Confirmar decisión 2"):
            if decision2 == "Invertir en criptomonedas":
                resultado = random.choice(["ganancia", "pérdida"])
                if resultado == "ganancia":
                    st.session_state.patrimonio += 1000000
                    st.session_state.ingresos_pasivos += 50000
                    st.session_state.felicidad += 5
                else:
                    st.session_state.patrimonio -= 700000
                    st.session_state.estres += 10
            elif decision2 == "Ahorrar en un fondo seguro":
                st.session_state.patrimonio += 300000
                st.session_state.ingresos_pasivos += 20000
                st.session_state.felicidad += 3
            elif decision2 == "Gastar en un viaje para despejarte":
                st.session_state.patrimonio -= 500000
                st.session_state.felicidad += 15
                st.session_state.estres -= 10

            evento2 = random.choice([
                ("Te ascendieron en el trabajo y ganas más", 800000, -5),
                ("Se rompió tu celular y tuviste que comprar otro", -300000, 5),
                ("Tu arriendo subió inesperadamente", -400000, 10)
            ])
            st.session_state.patrimonio += evento2[1]
            st.session_state.estres += evento2[2]
            st.session_state.evento2 = evento2[0]
            st.session_state.decision2 = decision2
            st.rerun()

    else:
        st.header("🔄 Segunda decisión tomada")
        st.write(f"Decisión: {st.session_state.decision2}")
        st.warning(f"⚠️ Evento aleatorio: {st.session_state.evento2}")

        st.header("📊 Resultados Finales")
        st.metric("💰 Patrimonio", f"${st.session_state.patrimonio:,.0f}")
        st.metric("😊 Felicidad", f"{st.session_state.felicidad}%")
        st.metric("😰 Estrés", f"{st.session_state.estres}%")
        st.metric("🏦 Ahorros", f"${st.session_state.ahorros:,.0f}")
        st.metric("📈 Ingresos Pasivos", f"${st.session_state.ingresos_pasivos:,.0f}")

        st.info("🦆 Consejo de DON’T PATO: Las decisiones más sabias no siempre son las más populares. ¡Planea tu vida como si fuera un juego, pero juega en serio!")

        if st.button("🔁 Reiniciar simulador"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
# Simulador de Vida Real Financiera - Versión Avanzada Estilo Juego

import streamlit as st
import random

# Inicializar estado si no existe
if "estado" not in st.session_state:
    st.session_state.estado = {
        "juego_iniciado": False,
        "avatar_creado": False,
        "patrimonio": 0,
        "felicidad": 50,
        "estres": 30,
        "ahorros": random.randint(100000, 500000),
        "ingresos_pasivos": 0,
        "edad": 18,
        "activos": [],
        "trayectoria": "",
        "situacion": ""
    }

st.title("🧠 Simulador de Vida Real Financiera - DON’T PATO")

estado = st.session_state.estado

if not estado["avatar_creado"]:
    st.subheader("🧍‍♂️ Crea tu personaje")
    nombre = st.text_input("Nombre")
    ciudad = st.selectbox("Ciudad", ["Antofagasta", "Santiago", "Concepción"])
    estilo_vida = st.radio("Estilo de vida", ["Austero", "Normal", "Me lo merezco"])
    trayectoria = st.radio("¿Qué camino quieres seguir?", [
        "Estudiante universitario",
        "Trabajador asalariado",
        "Emprendedor",
        "Freelancer"
    ])

    if st.button("Iniciar Simulación"):
        estado["nombre"] = nombre
        estado["ciudad"] = ciudad
        estado["estilo_vida"] = estilo_vida
        estado["trayectoria"] = trayectoria

        if trayectoria == "Estudiante universitario":
            estado["patrimonio"] = -1000000
            estado["situacion"] = "Estás estudiando y tu ingreso mensual es $200.000 CLP."
        elif trayectoria == "Trabajador asalariado":
            estado["patrimonio"] = 500000
            estado["situacion"] = "Tienes un empleo formal y ganas $500.000 CLP al mes."
        elif trayectoria == "Emprendedor":
            estado["patrimonio"] = 300000
            estado["situacion"] = "Estás comenzando un negocio propio, tus ingresos son variables."
        elif trayectoria == "Freelancer":
            estado["patrimonio"] = 400000
            estado["situacion"] = "Trabajas por cuenta propia y tus ingresos mensuales rondan los $450.000 CLP."

        estado["avatar_creado"] = True
        st.rerun()

if estado["avatar_creado"]:
    st.success(f"¡Bienvenido/a {estado['nombre']}!")
    st.write(f"🌆 Ciudad: {estado['ciudad']} | 🧭 Estilo de vida: {estado['estilo_vida']} | 🎯 Trayectoria: {estado['trayectoria']}")
    st.info(f"📌 {estado['situacion']}")

    # Primera decisión según trayectoria
    if "decision1" not in estado:
        st.header("🔀 Primera gran decisión")
        if estado['trayectoria'] == "Estudiante universitario":
            opciones = ["Buscar trabajo part-time", "Pedir un crédito estudiantil", "Enfocarte solo en estudiar"]
        elif estado['trayectoria'] == "Trabajador asalariado":
            opciones = ["Postular a un ascenso", "Iniciar un emprendimiento paralelo", "Seguir en el mismo puesto"]
        elif estado['trayectoria'] == "Emprendedor":
            opciones = ["Invertir más en el negocio", "Buscar socio inversor", "Diversificar con un nuevo producto"]
        else:  # Freelancer
            opciones = ["Tomar más clientes", "Subir tus tarifas", "Aprender una nueva habilidad"]

        decision1 = st.radio("¿Qué eliges?", opciones, key="d1")

        if st.button("Confirmar decisión 1"):
            efecto = random.choice(["positivo", "negativo"])
            if efecto == "positivo":
                estado["patrimonio"] += 500000
                estado["felicidad"] += 10
                estado["estres"] += 5
            else:
                estado["patrimonio"] -= 300000
                estado["felicidad"] -= 5
                estado["estres"] += 15
            evento1 = random.choice([
                ("Recibiste una beca sorpresa de $300.000", 300000, -5),
                ("Se rompió tu notebook y tuviste que repararlo", -200000, 10),
                ("Ganaste un concurso de innovación y recibiste $500.000", 500000, -3)
            ])
            estado["patrimonio"] += evento1[1]
            estado["estres"] += evento1[2]
            estado["evento1"] = evento1[0]
            estado["decision1"] = decision1
            st.rerun()

    elif "decision2" not in estado:
        st.header("🔁 Segunda decisión")
        st.write(f"📌 Decisión anterior: {estado['decision1']}")
        st.warning(f"⚠️ Evento aleatorio: {estado['evento1']}")

        decision2 = st.radio("¿Cómo manejas tus finanzas ahora?", [
            "Invertir en criptomonedas",
            "Ahorrar en un fondo seguro",
            "Comprar un pequeño activo (ej: notebook, bicicleta)"
        ], key="d2")

        if st.button("Confirmar decisión 2"):
            if decision2 == "Invertir en criptomonedas":
                resultado = random.choice(["ganancia", "pérdida"])
                if resultado == "ganancia":
                    estado["patrimonio"] += 800000
                    estado["ingresos_pasivos"] += 50000
                else:
                    estado["patrimonio"] -= 600000
                    estado["estres"] += 10
            elif decision2 == "Ahorrar en un fondo seguro":
                estado["patrimonio"] += 200000
                estado["ingresos_pasivos"] += 15000
            elif decision2 == "Comprar un pequeño activo (ej: notebook, bicicleta)":
                estado["activos"].append("Notebook/Bicicleta")
                estado["patrimonio"] -= 400000
                estado["felicidad"] += 8

            evento2 = random.choice([
                ("Te ofrecieron un trabajo freelance extra por $250.000", 250000, -2),
                ("Te multaron por no pagar el TAG: -$150.000", -150000, 5),
                ("Subió el arriendo y pagas $100.000 más al mes", -300000, 8)
            ])
            estado["patrimonio"] += evento2[1]
            estado["estres"] += evento2[2]
            estado["evento2"] = evento2[0]
            estado["decision2"] = decision2
            st.rerun()

    else:
        st.header("🏁 Resultados Finales")
        st.write(f"🎓 Trayectoria: {estado['trayectoria']}")
        st.write(f"🎒 Activos comprados: {', '.join(estado['activos']) if estado['activos'] else 'Ninguno'}")
        st.write(f"⚠️ Evento 1: {estado['evento1']}")
        st.write(f"⚠️ Evento 2: {estado['evento2']}")

        st.metric("💰 Patrimonio", f"${estado['patrimonio']:,.0f}")
        st.metric("😊 Felicidad", f"{estado['felicidad']}%")
        st.metric("😰 Estrés", f"{estado['estres']}%")
        st.metric("🏦 Ahorros", f"${estado['ahorros']:,.0f}")
        st.metric("📈 Ingresos Pasivos", f"${estado['ingresos_pasivos']:,.0f}")

        st.info("🦆 Consejo de DON’T PATO: Las decisiones inteligentes no siempre son fáciles, pero siempre enseñan algo. ¡Sigue jugando la vida con estrategia!")

        if st.button("🔁 Reiniciar simulador"):
            del st.session_state.estado
            st.rerun()
