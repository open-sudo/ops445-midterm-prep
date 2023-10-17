!/usr/bin/python3

import sys

def compute_stats(sourceFile: str, statsFile:str):
  data =open(sourceFile,'r')
  lines=data.readlines()

  gradeLines=lines[1:]
  grades={}
  for grade in gradeLines:
      if len(grade.strip())> 0 :
         parts=grade.split(',')
         grades[parts[0].strip()]=int(parts[1].strip())

  gradeValues=list(grades.values())

  gradeMin=100
  for gradeValue in gradeValues:
     if gradeValue < gradeMin :
        gradeMin=gradeValue

  gradeMax=0
  for gradeValue in gradeValues:
     if gradeValue > gradeMax :
        gradeMax=gradeValue

  average=0
  for gradeValue in gradeValues:
        average=average+gradeValue
  average = int(average / len(gradeValues))

  tops=[]
  gradeIds=grades.keys()
  for gradeId in gradeIds :
     if grades[gradeId] == gradeMax :
         tops.append(gradeId)

  gradeValues.sort()
  median=0;
  numberOfStudents=len(gradeValues)
  if numberOfStudents % 2 == 1 :
     median=gradeValues[int(numberOfStudents/2)]
  else:
     median=(gradeValues[int(numberOfStudents/2)-1]+gradeValues[int(numberOfStudents/2)])/2

  output=open(statsFile,'w')
  output.write('Minimum Grade:'+str(gradeMin)+'\n')
  output.write('Maximum Grade:'+str(gradeMax)+'\n')
  output.write('Average Grade:'+str(average)+'\n')
  output.write('Top Students:'+(", ".join(tops))+'\n')
  output.write('Median Grade:'+str(median)+'\n')
  data.close()
  output.close()

    
def compute_median(grades: list) -> int:
  return 0
  
def compute_min(grades: list) -> int:
  return 0
  
def compute_max(grades: list) -> int:
  return 0
  
def compute_top_students(grades: dict, gradeMax) -> list:
  return []
         
def compute_average(grades: list) -> float:
  return 0
  
def read_grades(sourceFile: str) -> dict:
  return {}
     
def write_grades(min: int, max: int, med: int, avg: int, tops: list, statsFile:str):
    return None

if __name__ == '__main__' : 
  compute_stats(sys.argv[1],sys.argv[2])
