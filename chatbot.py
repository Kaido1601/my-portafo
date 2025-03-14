rules = {
    "hola": "¡Hola! ¿Cómo te puedo ayudar?",
    "adiós": "¡Hasta luego!",
    "¿cómo estás?": "Bien, que necesitas",
    "gracias": "De nada, ¡que tengas un bonito día!",
    "necesito un favor": "que necesitas, dime",
    "¿qué hora es?": "Lo siento, no tengo un reloj interno.",
    "¿quién eres?": "Soy un chatbot que responde preguntas básicas.",
    "¿cómo te llamas?": "No tengo nombre, pero estoy aquí para ayudarte.",
    "¿qué puedes hacer?": "Puedo responder preguntas básicas y ayudarte en lo que pueda.",
    "¿dónde estás?": "Estoy en la nube, accesible desde cualquier lugar con conexión a internet.",
    "¿por qué existes?": "Para ayudarte y responder tus preguntas.",
    "¿cuál es tu color favorito?": "Como soy un chatbot, no tengo preferencias personales.",
    "cuéntame un chiste": "¿Por qué el libro de matemáticas se deprimió? Porque tenía demasiados problemas.",
    "¿qué es python?": "Python es un lenguaje de programación muy popular y versátil.",
    "¿qué es la inteligencia artificial?": "La inteligencia artificial es la simulación de procesos de inteligencia humana por parte de máquinas.",
    "cuéntame un dato curioso": "Los flamencos son rosados debido a su dieta de crustáceos y algas.",
    "¿qué es el internet?": "El internet es una red global de computadoras interconectadas que permite el intercambio de información.",
    "¿cuál es la capital de Francia?": "La capital de Francia es París.",
    "¿quién descubrió América?": "Cristóbal Colón llegó a América en 1492, aunque ya estaba habitada por pueblos indígenas.",
    "¿cuándo empezó la Primera Guerra Mundial?": "La Primera Guerra Mundial comenzó en 1914.",
    "¿qué es la Revolución Industrial?": "La Revolución Industrial fue un periodo de grandes cambios tecnológicos y económicos que empezó en el siglo XVIII.",
    "¿cuál es el río más largo del mundo?": "El río Nilo es considerado el río más largo del mundo.",
    "¿cuál es la montaña más alta del mundo?": "El Monte Everest es la montaña más alta del mundo.",
    "¿cuántos continentes hay?": "Hay siete continentes: África, América del Norte, América del Sur, Antártida, Asia, Europa y Oceanía.",
    "¿cuál es el país más grande del mundo?": "Rusia es el país más grande del mundo en términos de superficie.",
    "¿cuál es la ciudad más poblada del mundo?": "Tokio, Japón, es la ciudad más poblada del mundo.",
    "¿en que año callo el imperio romano?": "El imperio romano cayo en el 476 d.c, hay comenzo la edad media",
    "¿en que año callo el impero bizantino": "El impero bizantino cayo en 1453, hay inicio la edad moderna",
    "¿cual es la persona mas rica de la historia?": "Fue masan muza un rey africano",
    "¿cual es la persona mas rica de la actualidad": "Es elon musk un sudafricano nacionalizado estadounidense",
    "¿En que año inicio la segunda guerra mundial?": "En el 1939",
    "¿cuál es el pais mas largo del mundo?": "Es chile el país mas largo del mundo",


        "¿Quién fue el primer presidente de los Estados Unidos?": "George Washington fue el primer presidente de los Estados Unidos, sirviendo de 1789 a 1797.",

        "¿Cuál es el río más largo del mundo?": "El río Nilo, con una longitud de aproximadamente 6,650 kilómetros, es considerado el río más largo del mundo.",

        "¿Qué es la fotosíntesis?": "La fotosíntesis es el proceso mediante el cual las plantas utilizan la luz solar para convertir el dióxido de carbono y el agua en glucosa y oxígeno.",


        "¿Quién escribió 'Cien años de soledad'?": "'Cien años de soledad' fue escrito por el autor colombiano Gabriel García Márquez y publicado en 1967.",

        "¿Quién pintó 'La última cena'?": "'La última cena' fue pintada por Leonardo da Vinci entre 1495 y 1498.",

        "¿Quién es conocido como el 'Rey del Rock and Roll'?": "Elvis Presley es conocido como el 'Rey del Rock and Roll'.",

        "¿En qué año se celebraron los primeros Juegos Olímpicos modernos?": "Los primeros Juegos Olímpicos modernos se celebraron en Atenas, Grecia, en 1896.",

        "¿Qué franquicia cinematográfica incluye personajes como Luke Skywalker y Darth Vader?": "La franquicia cinematográfica es 'Star Wars' (La Guerra de las Galaxias).",

        "¿Quién es el fundador de Microsoft?": "Microsoft fue fundada por Bill Gates y Paul Allen en 1975.",

}

def chatbot():
    print("Chatbot: ¡Bienvenido!")
    while True:
        user_input = input("Tú: ").strip().lower()
        if user_input == "salir":
            print("Chatbot: ¡Adiós!")
            break
        response = rules.get(user_input, "No entiendo.")
        print(f"Chatbot: {response}")

chatbot()
