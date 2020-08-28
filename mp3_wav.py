from pydub import AudioSegment

def preprocess_file(filename):
    src = "static/img/"+filename
    dst = "static/img/"+filename.split(".")[0]+".wav"
    sound = AudioSegment.from_mp3(src)
    sound.export(dst,format="wav")

    return filename.split(".")[0]+".wav"

preprocess_file("REC20200709191353.mp3")