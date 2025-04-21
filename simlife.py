
# Simulador corregido con claves únicas - DON’T PATO

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
    nombre = st.text_input("Nombre", key="input_nombre")
    ciudad = st.selectbox("Ciudad", ["Antofagasta", "Santiago", "Concepción"], key="select_ciudad")
    estilo_vida = st.radio("Estilo de vida", ["Austero", "Normal", "Me lo merezco"], key="radio_estilo")
    trayectoria = st.radio("¿Qué camino quieres seguir?", [
        "Estudiante universitario",
        "Trabajador asalariado",
        "Emprendedor",
        "Freelancer"
    ], key="radio_trayectoria")

    if st.button("Iniciar Simulación", key="btn_iniciar"):
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

    if "decision1" not in estado:
        st.header("🔀 Primera gran decisión")
        if estado['trayectoria'] == "Estudiante universitario":
            opciones = ["Buscar trabajo part-time", "Pedir un crédito estudiantil", "Enfocarte solo en estudiar"]
        elif estado['trayectoria'] == "Trabajador asalariado":
            opciones = ["Postular a un ascenso", "Iniciar un emprendimiento paralelo", "Seguir en el mismo puesto"]
        elif estado['trayectoria'] == "Emprendedor":
            opciones = ["Invertir más en el negocio", "Buscar socio inversor", "Diversificar con un nuevo producto"]
        else:
            opciones = ["Tomar más clientes", "Subir tus tarifas", "Aprender una nueva habilidad"]

        decision1 = st.radio("¿Qué eliges?", opciones, key="radio_decision1")

        if st.button("Confirmar decisión 1", key="btn_decision1"):
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
        ], key="radio_decision2")

        if st.button("Confirmar decisión 2", key="btn_decision2"):
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
            elif decision2 == "Comprar un pequeño activo (ej: notebook, bicicleta)"):
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

        if st.button("🔁 Reiniciar simulador", key="btn_reiniciar"):
            del st.session_state.estado
            st.rerun()

