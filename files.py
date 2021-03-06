import errno

#This class takes care of files needed in discordbot
class Files():

  def __init__(self, filename):
    self.filename = filename
#Read a file line by line and store it to list & return
  def readFile(self):
    try:
      s = open(self.filename, "rt")
      questions = s.readlines()
      s.close()
    except Exception as exc:
        if exc.errno == errno.ENOENT:
            print("The file doesn't exist.")
        elif exc.errno == errno.EMFILE:
            print("You've opened too many files.")
        else:
            print("The error number is:", exc.errno)
    return questions
