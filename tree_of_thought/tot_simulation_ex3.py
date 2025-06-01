domain = """Theaters have a location, and they can play any play, which can be musicals or operas. 
 Plays have a name and can be played either at day or night. 
 Plays are written by one or more authors, who have a name. 
 There are many participants who act in a play, participants also have a name. 
 A particular participant acts in a particular session of a play, where each session begins and ends at a specific time. 
 Both authors and participants are persons."""

level1 = []
level1.append(
"""
**Classes and enumerations:**  
- Theater (concrete) (Confidence: 95)  
  - Attributes:  
    - location (Confidence: 90)  

- Play (concrete) (Confidence: 95)  
  - Attributes:  
    - name (Confidence: 92)  
    - PerformanceTime (Confidence: 85)  

- Musical (concrete) (Confidence: 90)  
  - Attributes: None  

- Opera (concrete) (Confidence: 90)  
  - Attributes: None  

- Participant (concrete) (Confidence: 93)  
  - Attributes:  
    - name (Confidence: 91)  

- Session (concrete) (Confidence: 92)  
  - Attributes:  
    - startTime (Confidence: 90)  
    - endTime (Confidence: 90)  

- Author (concrete) (Confidence: 93)  
  - Attributes:  
    - name (Confidence: 91)  

- Person (abstract) (Confidence: 95)  
  - Attributes:  
    - name (Confidence: 95)  

- PerformanceTime (enumeration) (Confidence: 85)  
  - Literals:  
    - Day (Confidence: 85)  
    - Night (Confidence: 85)  

""")
level1.append(
"""
**Classes, abstract classes, and enumerations:**  

- **Theater (concrete) (Confidence: 100)**  
  - Attributes:  
    - location (Confidence: 100)  

- **Play (concrete) (Confidence: 95)**  
  - Attributes:  
    - name (Confidence: 100)  
    - performanceTime (Confidence: 90)  

- **Musical (concrete) (Confidence: 90)** (subclass of Play)

- **Opera (concrete) (Confidence: 90)** (subclass of Play)  

- **Person (abstract) (Confidence: 100)**  
  - Attributes:  
    - name (Confidence: 100)  

- **Author (concrete) (Confidence: 95)** (subclass of Person)

- **Participant (concrete) (Confidence: 95)** (subclass of Person)

- **Session (concrete) (Confidence: 95)**  
  - Attributes:  
    - startTime (Confidence: 100)  
    - endTime (Confidence: 100)  

- **PerformanceTime (enumeration) (Confidence: 90)**  
  - Literals:  
    - Day (Confidence: 100)  
    - Night (Confidence: 100)  

""")
level1.append(
"""
### Classes, Abstract Classes, and Enumerations:

- **Theater (concrete) (Confidence: 100)**  
  - Attributes:  
    - location (Confidence: 100)  

- **Play (abstract) (Confidence: 100)**  
  - Attributes:  
    - name (Confidence: 100)  
    - PerformanceTime (Confidence: 100)  

- **Author (abstract) (Confidence: 90)**  
  - Attributes:  
    - name (Confidence: 100)  

- **Participant (abstract) (Confidence: 90)**  
  - Attributes:  
    - name (Confidence: 100)  

- **Person (abstract) (Confidence: 95)**  
  - Attributes:  
    - name (Confidence: 100)  

- **Session (concrete) (Confidence: 100)**  
  - Attributes:  
    - startTime (Confidence: 100)  
    - endTime (Confidence: 100)  

- **PlayType (enumeration) (Confidence: 90)**  
  - Literals:  
    - Musical (Confidence: 100)  
    - Opera (Confidence: 100)  

- **PerformanceTime (enumeration) (Confidence: 90)**  
  - Literals:  
    - Day (Confidence: 100)  
    - Night (Confidence: 100) 
""")


level1_selected = 2
'''
INFO:tree_of_thought.search:Thought 1: 0 votes
INFO:tree_of_thought.search:Thought 2: 5 votes
INFO:tree_of_thought.search:Thought 3: 0 votes
'''

level2 = []
level2.append(
""" 
### Classes, abstract classes, and enumerations:
- **Theater (concrete) (Confidence: 100)**  
  - Attributes:  
    - location (Confidence: 100)  

- **Play (abstract) (Confidence: 95)**  
  - Attributes:  
    - name (Confidence: 100)  
    - performanceTime (Confidence: 90)  

- **Musical (concrete) (Confidence: 90)** (subclass of Play)

- **Opera (concrete) (Confidence: 90)** (subclass of Play)  

- **Person (abstract) (Confidence: 100)**  
  - Attributes:  
    - name (Confidence: 100)  

- **Author (concrete) (Confidence: 95)** (subclass of Person)

- **Participant (concrete) (Confidence: 95)** (subclass of Person)
  - New Attribute:  
    - role (Confidence: 90)  

- **Session (concrete) (Confidence: 95)**  
  - Attributes:  
    - startTime (Confidence: 100)  
    - endTime (Confidence: 100)  

- **PerformanceTime (enumeration) (Confidence: 90)**  
  - Literals:  
    - Day (Confidence: 100)  
    - Night (Confidence: 100)  

### Relationships:

#### **Association:**
- **Theater — Play** (Confidence: 90)  
  - Cardinality:  
    - Theater: 1 (Confidence: 90)  
    - Play: 0..* (Confidence: 95)  

- **Play — Author** (Confidence: 95)  
  - Cardinality:  
    - Play: 1..* (Confidence: 95)  
    - Author: 1..* (Confidence: 95)  

- **Play — Participant** (Confidence: 90)  
  - Cardinality:  
    - Play: 1..* (Confidence: 90)  
    - Participant: 1..* (Confidence: 95)  

- **Participant — Session** (Confidence: 95)  
  - Cardinality:  
    - Participant: 1..* (Confidence: 90)  
    - Session: 1 (Confidence: 95)  

#### **Containment:**
- **Session — Play** (Confidence: 85)  
  - Cardinality:  
    - Session: 1..* (Confidence: 85)  
    - Play: 1 (Confidence: 90)  

#### **Inheritance:**
- **Play — Musical** (Confidence: 95)  
  - Cardinality:  
    - Play: 1 (Confidence: 95)  
    - Musical: 1 (Confidence: 95)  

- **Play — Opera** (Confidence: 95)  
  - Cardinality:  
    - Play: 1 (Confidence: 95)  
    - Opera: 1 (Confidence: 95)  

- **Person — Author** (Confidence: 95)  
  - Cardinality:  
    - Person: 1 (Confidence: 100)  
    - Author: 1 (Confidence: 95)  

- **Person — Participant** (Confidence: 95)  
  - Cardinality:  
    - Person: 1 (Confidence: 100)  
    - Participant: 1 (Confidence: 95)  

""")

level2.append(
"""  
#### Classes, Abstract Classes, and Enumerations:  

- **Theater (concrete) (Confidence: 100)**  
  - Attributes:  
    - location (Confidence: 100)  

- **Play (abstract) (Confidence: 95)**  
  - Attributes:  
    - name (Confidence: 100)  
    - performanceTime (Confidence: 90)  

- **Musical (concrete) (Confidence: 90)** (subclass of Play)  

- **Opera (concrete) (Confidence: 90)** (subclass of Play)  

- **Person (abstract) (Confidence: 100)**  
  - Attributes:  
    - name (Confidence: 100)  

- **Author (concrete) (Confidence: 95)** (subclass of Person)  

- **Participant (concrete) (Confidence: 95)** (subclass of Person)  

- **Session (concrete) (Confidence: 95)**  
  - Attributes:  
    - startTime (Confidence: 100)  
    - endTime (Confidence: 100)  

- **PerformanceTime (enumeration) (Confidence: 90)**  
  - Literals:  
    - Day (Confidence: 100)  
    - Night (Confidence: 100)  

---

#### Relationships:

##### Associations:  
- **Theater — Play (Confidence: 95)**  
  - Cardinality:  
    - Theater: 1..* (Confidence: 90)  
    - Play: 0..* (Confidence: 85)  

- **Play — Author (Confidence: 95)**  
  - Cardinality:  
    - Play: 1..* (Confidence: 95)  
    - Author: 1..* (Confidence: 95)  

- **Play — Participant (Confidence: 90)**  
  - Cardinality:  
    - Play: 1..* (Confidence: 90)  
    - Participant: 0..* (Confidence: 85)  

- **Participant — Session (Confidence: 90)**  
  - Cardinality:  
    - Participant: 1 (Confidence: 90)  
    - Session: 1 (Confidence: 90)  

##### Containments:  
- **Play — Session (Confidence: 95)**  
  - Cardinality:  
    - Play: 1..* (Confidence: 95)  
    - Session: 1..* (Confidence: 95)  

##### Inheritances:  
- **Play — Musical (Confidence: 90)**  
  - Inheritance: Musical inherits from Play  

- **Play — Opera (Confidence: 90)**  
  - Inheritance: Opera inherits from Play  

- **Person — Author (Confidence: 95)**  
  - Inheritance: Author inherits from Person  

- **Person — Participant (Confidence: 95)**  
  - Inheritance: Participant inherits from Person  
""")
level2.append(
"""
#### **Classes, abstract classes, and enumerations:**

- **Theater (concrete) (Confidence: 100)**  
  - Attributes:  
    - location (Confidence: 100)  

- **Play (abstract) (Confidence: 95)**  
  - Attributes:  
    - name (Confidence: 100)  
    - performanceTime (Confidence: 90)  

- **Musical (concrete) (Confidence: 90)** (subclass of Play)  

- **Opera (concrete) (Confidence: 90)** (subclass of Play)  

- **Person (abstract) (Confidence: 100)**  
  - Attributes:  
    - name (Confidence: 100)  

- **Author (concrete) (Confidence: 95)** (subclass of Person)  

- **Participant (concrete) (Confidence: 95)** (subclass of Person)  
  - **Modified:** Added attribute:  
    - role (Confidence: 85)  

- **Session (concrete) (Confidence: 95)**  
  - Attributes:  
    - startTime (Confidence: 100)  
    - endTime (Confidence: 100)  

- **PerformanceTime (enumeration) (Confidence: 90)**  
  - Literals:  
    - Day (Confidence: 100)  
    - Night (Confidence: 100)  

---

#### **Relationships:**

1. **Associate:**  
   - **Play — Theater (Confidence: 90)**  
     - Cardinality:  
       - Play: 0..* (Confidence: 90)  
       - Theater: 1 (Confidence: 90)  

2. **Associate:**  
   - **Play — Author (Confidence: 95)**  
     - Cardinality:  
       - Play: 1..* (Confidence: 95)  
       - Author: 1..* (Confidence: 95)  

3. **Associate:**  
   - **Play — Participant (Confidence: 90)**  
     - Cardinality:  
       - Play: 1..* (Confidence: 90)  
       - Participant: 1..* (Confidence: 90)  

4. **Associate:**  
   - **Session — Participant (Confidence: 95)**  
     - Cardinality:  
       - Session: 1 (Confidence: 95)  
       - Participant: 1..* (Confidence: 95)  


6. **Containment:**  
   - **Session — Play**  
     - Cardinality: Session `1`, Play `1`  
     - **Confidence: 95**

7. **Inheritance:**  
   - **Musical — Play**  
     - **Confidence: 90**

8. **Inheritance:**  
   - **Opera — Play**  
     - **Confidence: 90**

9. **Inheritance:**  
   - **Author — Person**  
     - **Confidence: 95**

10. **Inheritance:**  
    - **Participant — Person**  
      - **Confidence: 95**


""")


level2_selected = 3
'''
INFO:tree_of_thought.search:Thought 1: 0 votes
INFO:tree_of_thought.search:Thought 2: 0 votes
INFO:tree_of_thought.search:Thought 3: 5 votes
'''

puml = """
@startuml
Enum Time{
  Day
  Night
}
abstract class Person {
  String name
}
class Author {
}
class Participant {
}
class Session {
  int timeBegin
  int timeEnd
}
class Theater {
  String Location
}
abstract class Play {
  String name
  Time time
}
class Musical {
}
class Opera {
}

Play "*" -- "*" Theater : plays
Author "1..*"  -- "*" Play : writes
Participant "*" -- "*" Play : acts

Person <|-- Author
Person <|-- Participant
Play <|-- Musical
Play <|-- Opera

(Play , Participant) .. Session
@enduml
"""