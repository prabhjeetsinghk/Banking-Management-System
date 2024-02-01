from cryptography.fernet import Fernet

class encdec:     
   def __init__(self,key):
      self.fernet = Fernet(key) 
      
   def strEncoder(self, text):
      fern = self.fernet
      encText = fern.encrypt(text.encode())
      return encText

   def strDecorder(self, text):
      fern = self.fernet
      decTxt = fern.decrypt(text).decode()
      return decTxt