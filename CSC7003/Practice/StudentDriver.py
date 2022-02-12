from Student import *
def print_transcript(s):
  print("\nTranscript for ",s.name,"\n")
  for c in s.courses:
    print("%6s  %.1f  %3s"%(c[0],c[1],c[2]))
  print("\nGPA: ",s.gpa(),"\n")

def main():
  s1 = Student("Tommy Jones")
  s1.add_course('CSc7003',1.5,'A')
  s1.add_course('CSc6710',4,'B')
  s1.add_course('CSc3320',3,'C')
  print_transcript(s1)

  s2 = Student("Hilary Smith")
  s2.add_course('CSc 1301',4,'A')
  s2.add_course('CSc 1302',4,'A')
  s2.add_course('CSc 2510',3,'B')
  s2.add_course('CSc 2720',3,'A')
  s2.add_course('CSc 3210',3,'C')
  s2.add_course('CSc 3320',3,'A')
  print_transcript(s2)

main()
