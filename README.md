# qea
Simple interface to manage a library of questions, separated by themes and having place of origin and some keywords for searches. 
The system allows registering questions, their type, whether they have multiple choices or whether they are right/wrong, as well as registering comments for the answers.


```mermaid
classDiagram
    Theme <|-- Question
    class Theme{
      + theme CharField
    }  

    Question <|-- Answer
    class Question{
      - theme ForeignKey
      + asktext TextField 
      + answer_type PositiveIntegerField 
      + asksource CharField
      + date_created DateTimeField
    }

    class Answer{
      - question ForeignKey
      + answertext TextField 
      + iscorrect PositiveIntegerField 
      + date_created DateTimeField
    }

    Question <|-- Questiontag
    class Questiontag{
      - question ForeignKey
      + tag ForeignKey 
    } 

    Answer <|-- Note
    class Note{
      - answer ForeignKey
      + answernote CharField
      + revised PositiveSmallIntegerField
      + date_created DateTimeField
      + date_revised DateTimeField
    }  
        
    Questiontag <|-- Tag
    class Tag{
      + name CharField
    } 
```