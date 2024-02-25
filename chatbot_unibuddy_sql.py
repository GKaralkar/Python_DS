import sqlite3
import re


con=sqlite3.connect("chatbotunibuddy_db")
print('Connection Established')
cur = con.cursor() 
cur.executescript('drop table if exists unibuddy_qa;')






con.execute('''
   CREATE TABLE  IF NOT EXISTS unibuddy_qa(
    q_id INTEGER AUTO_INCREMENT,
    question TEXT NOT NULL,
    answer TEXT NOT NULL 
    );
    ''')



cur.execute("INSERT INTO unibuddy_qa (q_id,question,answer)values(?,?,?)",(1,"where is the fees office","The fees office is located in the Blue building on camp lane "));
cur.execute("INSERT INTO unibuddy_qa (q_id,question,answer)values(?,?,?)",(2,"who can help me with the curriculum form"," You can speak to your course advisor or an Orientation Leader "));
cur.execute("INSERT INTO unibuddy_qa (q_id,question,answer)values(?,?,?)",(3,"what clubs does the university offer"," The university has a cricket, art and a football club for which you have to apply for membership "));
cur.execute("INSERT INTO unibuddy_qa (q_id,question,answer)values(?,?,?)",(4,"who is the student support rep"," Joshua Lee is the student support rep and you can get in touch with him via email joshualee@universityname.com "));
cur.execute("INSERT INTO unibuddy_qa (q_id,question,answer)values(?,?,?)",(5,"where can i find out more about student accomodation"," The student accomodation information is available on the university website, just look for student support services "));
cur.execute("INSERT INTO unibuddy_qa (q_id,question,answer)values(?,?,?)",(6,"where can i find out more about the nhs centre"," The nearest nhs centre is 0.3 miles away "));



cur.execute("SELECT * FROM unibuddy_qa")

rows = cur.fetchall() 

for row in rows:

     print(row)


con.commit()



print("Hi it's UNIBUDDY : YOUR FRIENDLY ADVISOR :) ")

name=input("Please enter your name :")
print(f"Hi {name} nice to meet you...")
print("I am here to help you ! ... Here's a list of questions you can ask me about the university ..\n")
print("QUESTIONS : where is the fees office,where can i find out  about the nhs centre,")
print("\n who can help me with my curriculum form,what clubs does the university offer,")
print("\n who is the student support rep,where can i find out more about student accomodation.")
    
done=False

while not done:

    
    question_num=-1
    
    
    user_question=str(input("\n Your question :"))
    user_question=user_question.casefold()
    user_question=user_question.strip(" ")
    user_question=user_question.strip("?")
    
    
    print(user_question)

 
    

    #question=(cur.fetchone()[0])    

    #print(re.fullmatch(user_question,question))
     
     #if user_question!="bye":

    try:
  
            cur.execute("SELECT q_id FROM  unibuddy_qa WHERE question =? ",(user_question,))

            qid=(cur.fetchone()[0])    
            print(qid)

    except TypeError:
            qid=-1
            if user_question!="bye":
                
               print("This is an incorrect value.")

    
            
               
    question_num=int(qid)

                
    
    if (question_num>=0):
            
            
            cur.execute("SELECT answer FROM  unibuddy_qa WHERE q_id =? ", (question_num,))
          
            answer=(cur.fetchone()[0])
   
            print(f" \n {answer}")


    elif (user_question=="bye"):

            done=True

            print("Thankyou for your chatting with me !")

    else:
            print("\n I don't understand your response,please try again")

   
