class CSVUnPadPlugin:
   def input(self, filename):
      f = open(filename, 'r')
      self.contents = f.read()

   def run(self):
      self.alldata = self.contents.split(',')
      self.alldata = self.alldata[1:]
      #self.contents = ""
      #for i in range(0, len(self.alldata)):
      #   print(i)
      #   self.contents += self.alldata[i]
      #   if (i != len(self.alldata)-1):
      #       self.contents += ','

   def output(self, filename):
      g = open(filename, 'w')
      for i in range(0, len(self.alldata)):
         g.write(self.alldata[i])
         if (i != len(self.alldata)-1):
             g.write(',')
         #self.contents += self.alldata[i]
         #if (i != len(self.alldata)-1):
         #    self.contents += ','
         #g.write(self.contents)
