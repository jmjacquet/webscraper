import PyPDF2
import pyttsx3

def extract_text(filename):
	pdfFile = open(filename,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFile)

	text =""

	for pageNum in range(pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		text += pageObj.extractText()

	pdfFile.close()
	return text

def speak(text):
	engine = pyttsx3.init()
	voices = engine.getProperty('voices')
	engine.setProperty('rate',2000)
	engine.setProperty('voice',voices[1].id)
	engine.say(text)
	engine.runAndWait()


if __name__=='__main__'	:
	text = "Hola mundo soy Juanma!"
	speak(text)

	sample = open('sample.txt','w')
	sample.write(text)
	sample.close()

#sudo apt-get install espeak