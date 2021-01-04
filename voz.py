import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    t_end = time.time() + 5
    while time.time() < t_end:
        print("karl: Listening...")
        audio=r.listen(source)
    try:    
        query = r.recognize_google(audio)
        print(f"user:{query}")
    except:
        print("Try Again")