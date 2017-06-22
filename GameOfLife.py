#-------------------------------------------------------------------------------
# Name:        Game Of Life
# Purpose:     Interview - ThoughtWorks
#
# Author:      Maurya
#
# Created:     01/10/2012
# Copyright:   No copyright
# Licence:     <No Licence>
#-------------------------------------------------------------------------------

import copy
import validate
import sys

# Main class of cells
class Seed:
   ''' This class has the process and the things to do which John Horton Conway
       has defined'''
   def __init__(self,baseList,newList,rows,cols):
      self.baseList = baseList
      self.newList = newList
      self.rows= rows + 2
      self.cols = cols + 2
   def process(self):
      i=0;j=0;
      while(i < self.rows):
         j=0
         while(j < self.cols):
         #check conditions for each cell
         #. check property 1,2,3
            self.newList[i][j] = self.ifAlive(i,j) or self.newList[i][j]
         #. check property 4
            self.newList[i][j] = self.ifDead(i,j) or self.newList[i][j]
            j=j+1
         i=i+1
   def printNewList(self):
      self.process()
      print "The ouptut is below"
      i=0
      while(i<self.rows):
         print self.newList[i]
         i=i+1
   def ifDead(self,i,j):
      if self.baseList[i][j] == '-':
         if self.liveNeighbours(i,j) == 3:
            return '*'
         else:
            return '-'

   def ifAlive(self,i,j):
      if self.baseList[i][j] == '*' :
         if (self.liveNeighbours(i,j) > 3 or self.liveNeighbours(i,j) <=1):
            return '-'
         else:
            return '*'

   def liveNeighbours(self,i,j):
       neighbourCount=0
       if (i-1) >= 0:
           if (j-1)>=0 and self.baseList[i-1][j-1] == '*':
              neighbourCount=neighbourCount+1
           if self.baseList[i-1][j] == '*':
              neighbourCount=neighbourCount+1
           if (j+1) < self.cols and self.baseList[i-1][j+1] == '*':
              neighbourCount=neighbourCount+1
       if (i+1) < self.rows:
           if (j-1)>=0 and self.baseList[i+1][j-1] == '*':
              neighbourCount=neighbourCount+1
           if self.baseList[i+1][j] == '*':
              neighbourCount=neighbourCount+1
           if (j+1) < self.cols and self.baseList[i+1][j+1] == '*':
              neighbourCount=neighbourCount+1
       if (j-1)>= 0 and self.baseList[i][j-1] == '*':
           neighbourCount=neighbourCount+1
       if (j+1) < self.cols and self.baseList[i][j+1] == '*':
           neighbourCount=neighbourCount+1
       return neighbourCount;


if __name__ == "__main__":
   #read the input
   try:
       rows=input("enter the number of rows >")
       cols=input("enter the number of cols >")
   except Exception,e:
      print "Enter valid input in integers",e
   else:
       if validate.is_integer(rows) and validate.is_integer(cols):
           #if rows
           baseTupleList = [['-' for x in xrange(cols + 2)] \
                                for x in xrange(rows + 2)]
           i=1;
           while(i <= rows):
              j=1
              while( j <= cols):
                 while True:
                   x = str(raw_input('''enter the %dth row %dth col values >'''\
                        %(i,j) ))
                   if not validate.is_seed(x):
                      print "Please enter '*' and '-' meaning live and death" \
                        + "resp",x
                   else:
                      break;
                 baseTupleList[i][j] = x
                 j = j + 1
              i = i + 1
           newList = copy.deepcopy(baseTupleList)
           print "The input is below"
           i=0
           while(i<rows+2):
              print baseTupleList[i]
              i=i+1
           objseed = Seed(baseTupleList,newList,rows,cols)
           objseed.printNewList()
       else:
          print "Enter proper row and column in integers not float", rows,cols
