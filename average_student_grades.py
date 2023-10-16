#!/usr/bin/python3

import sys

def compute_averages(students: list) -> list:
  result=[]
  for student in students:
     parts =student.split(',')
     average=compute_average(parts[1:])
     result.append((cleanup_name(parts[0]),parts[1:],average))
  return result

def compute_average(parts: list) -> float:
    sum=0
    for part in parts:
        sum=sum+float(part)
    return sum / len(parts)

def read_content(fileName: str) -> list:
  data =open(fileName,'r')
  lines=data.readlines()
  return lines

def cleanup_name(content: str) -> str:
    parts=content.split(' ')
    fullName=""
    for part in parts:     
        clean=part.strip()
        if len(clean) > 0 :
           fullName=fullName+' '+part.strip().lower().capitalize()
    return fullName.strip()

def write_content(content: list,fileName: str):
   file=open(fileName,'a')
   for line in content:
      output=line[0]
      for grade in line[1]: 
        output = output+','+grade.strip()
      output=output+','+str(line[2])+'\n'
      file.write(output)  
        
def get_average(user):
     return user[2]


def sort_content(result: list) -> list :
   print('Sorting list:'+str(result))
   result.sort(reverse=True,key=get_average)
   return result
   
def write_header(content: list, fileOut:str):
   file=open(fileOut,'w')
   file.write(content[0])  
        
if __name__ == '__main__' :
  lines=read_content(sys.argv[1])
  result=compute_averages(lines[1:])
  result=sort_content(result)
  write_header(lines,sys.argv[2])
  write_content(result,sys.argv[2])
   
