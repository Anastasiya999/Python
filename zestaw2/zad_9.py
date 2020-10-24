def copy_file(infile_name, outfile_name):
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")
    while True:
        
        text = infile.readline()   
        if text == "":
            break
        if text.find("#")!=-1:
            text=text[:text.find("#")]
            if text!="":
                text+="\n"
            outfile.write(text)

        else:
            outfile.write(text)

    infile.close()
    outfile.close()
copy_file("sample.txt","text_without_comments.txt")