import subprocess


def generate(filename):
    
    proc = subprocess.Popen(
        "deepspeech --model models/output_graph.pbmm   --lm /home/udaram/Desktop/TCS_Internship/DeepspeechModel/models/lm.binary --trie /home/udaram/Desktop/TCS_Internship/DeepspeechModel/models/trie --audio "+filename,
        shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    print(output)

    return output

#post("static/img/chunk278.wav")

def generate_their(filename):
    
    proc = subprocess.Popen(
        "deepspeech --model models/output_graph.pbmm   --lm /home/udaram/Desktop/TCS_Internship/try-Kenlm/combined_corpus.binary --trie /home/udaram/Desktop/TCS_Internship/DeepspeechModel/trie --audio "+filename,
        shell=True, stdout=subprocess.PIPE, )
    output = proc.communicate()[0]
    print(output)

    return output


#
