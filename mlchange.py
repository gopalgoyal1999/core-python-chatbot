def transp():
    from googletrans import Translator
    import speech_recognition as sr
    import pyttsx3




    trans =Translator()
    en=pyttsx3.init('sapi5')
    voices=en.getProperty('voices')
    en.setProperty('voice',voices[1].id)



    def text_to_speech(a):
        en.say(a)
        en.runAndWait()
        print(a)

    def speech_to_text():
        device_id = None
        print("Listening")
        audio = r.listen(source)
        print("Waiting for connection")
        option = r.recognize_google((audio) ,language='hi-IN')
        option = trans.translate(option,dest='en')
        option = option.text
        option = option.lower()
        print("you said: " + option)
        text_to_speech(option)
        return option
    
    mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)"
    sample_rate = 48000
    chunk_size = 2048
    r = sr.Recognizer()
    mic_list = sr.Microphone.list_microphone_names()
    device_id = None
    
    for i, microphone_name in enumerate(mic_list):
        if microphone_name == mic_name:
            device_id = i

    with sr.Microphone(device_index = device_id, sample_rate = sample_rate,
                            chunk_size = chunk_size) as source:
        
            r.adjust_for_ambient_noise(source)

            try:

                a = 'speak in hindi'
                text_to_speech(a)
                lan=speech_to_text()
                a='in which language you want to translate french,german,spanish,italian,dutch'
                text_to_speech(a)
                ch=speech_to_text()
                if ch=='french':
                    a=trans.translate(lan,dest='fr')
                elif ch=='german':
                    a=trans.translate(lan,dest='de')
                elif ch=='spanish':
                    a=trans.translate(lan,dest='es')
                elif ch=='italian':
                    a=trans.translate(lan,dest='it')
                elif ch=='dutch':
                    a=trans.translate(lan,dest='nl')
                a = a.text
                print(a)
                text_to_speech(a)
            except BaseException as e:
                print(e)

