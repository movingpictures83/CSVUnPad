class CSVUnPadPlugin:
   def input(self, filename):
      f = open(filename, 'r')
      self.contents = f.read()

   def run(self):
      alldata = self.contents.split(',')
      alldata = alldata[1:]
      self.contents = ""
      for i in range(0, len(alldata)):
         self.contents += alldata[i]
         if (i != len(alldata)-1):
             self.contents += ','

   def output(self, filename):
      g = open(filename, 'w')
      g.write(self.contents)
