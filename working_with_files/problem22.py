'''cut -    
             
            take line check if theres leftover and add them
            go word by word
            until if the length exceed size
            make chunks from it, ending at the last word before size exceeding

            if any left, save it as leftover

wrap
            call cut function for each line

'''

class TextWrapper:
    def __init__(self, size):
        self.size = size
        self.left_over = ""
        self.all_chunks = []

    def cut(self, line):
    
        if self.left_over:
            line = self.left_over + " " + line
        else:
            line = line

        words = line.split()
        self.left_over = ""   

        current_chunk = []
        current_len = 0

        for word in words:
            wlen = len(word)


            if current_len + wlen  > self.size:
             
                self.all_chunks.append(" ".join(current_chunk))
                current_chunk = [word]
                current_len = wlen
            else:
                current_chunk.append(word)
                current_len += wlen 
      
        self.left_over = " ".join(current_chunk)

    def wrap(self, file_name):
        with open(file_name) as f:
            for line in f:
                self.cut(line)

       
        if self.left_over:
            self.all_chunks.append(self.left_over)
            

        return self.all_chunks


tw = TextWrapper(30)
chunks = tw.wrap("lipsum.txt")

for c in chunks:
    print(c)