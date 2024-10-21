import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

while True:
    # Use the microphone as the source for input
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Adjusts the time the recognizer waits after detecting silence
        audio = r.listen(source)  # Listens for audio input

    try:
        # Recognize speech using Google Web Speech API
        recognized_text = r.recognize_google(audio)  # Converts audio to text
        print(f"User said: {recognized_text}")  # Print recognized text for user feedback

        # Write recognized text to draft.txt in chunks of 5 words
        filename = "draft.txt"
        with open(filename, "a+") as f:
            remainder = recognized_text.split()  # Split the recognized text into words
            while remainder:  # Continue until there are no words left
                line, remainder = remainder[:5], remainder[5:]  # Take 5 words at a time
                f.write(' '.join(line) + "\n")  # Write the 5 words to the file

        # Exit conditions
        if recognized_text.lower() == 'bye':
            print("Goodbye! Have a nice day!")  # Optional farewell message
            break
        elif recognized_text.lower() == 'stop':
            print("Goodbye! Have a nice day!")  # Optional farewell message
            break
        elif recognized_text.lower() == 'exit':
            print("Goodbye! Have a nice day!")  # Optional farewell message
            break

    except sr.UnknownValueError:
        print("Google could not understand audio")  # Handle case where audio isn't recognized
    except sr.RequestError as e:
        print(f"Google error: {e}")  # Handle errors with the Google API
