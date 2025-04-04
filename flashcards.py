import random

# Dictionary of flashcards,  i.e. variable donde se guarda la correspondencia entre el término preguntado y la respuesta correcta. Habrá que llamarla cuando se quiera comprobar la veracidad de la respuesta del user

flashcards = {
"Apfel":"apple",
"Haus": "house",
"Katze": "cat"
}

# Take a random word from the list contained in flashcards
german_word = random.choice(list(flashcards.keys()))

# Now we interact w user. Ask user for word in English
answer = input(f"What is the English translation of '{german_word}'?").strip().lower()

# Llama a donde están guardadas las equivalencias para ver si se corresponde
if  answer == flashcards[german_word].lower(): #equivalencia de la lista es la misma
    print("Correct")
else:
    print(f"Wrong. The correct answer is '{flashcards[german_word]}'") #la función te devuelve la equivalencia almacenada en flashcards de la palabara german_word en concreto que manejamos en este run del prog
