**AI Debugging Tutor (Streamlit + Gemini)**

An interactive Streamlit app that turns Google’s Gemini model into a Socratic Python tutor.
Instead of giving full solutions, the tutor provides one hint at a time, encouraging students to debug their own code step by step.

**Features**

-Supports Gemini Flash 2.5 (Free) and Gemini Pro models

-Pedagogical prompt prevents the model from leaking full solutions

-Step-by-step hints with escalation only when the student is stuck

-Conversation memory to simulate a real tutoring session

-Pre-loaded buggy code examples for easy testing

-Streamlit UI for student-friendly interaction

**Quick Start**
  1. Clone the repo
        git clone https://github.com/yourusername/ai-debugging-tutor.git
        cd ai-debugging-tutor

  2. Install dependencies
        pip install -r requirements.txt
        
        
        requirements.txt
        
        streamlit
        requests

   3. Add your Gemini API key
    
      Create a .streamlit/secrets.toml file:
      
      GEMINI_API_KEY = "your_api_key_here"
      
      
      or export it as an environment variable:
      
      export GEMINI_API_KEY="your_api_key_here"

  4. Run the app
      streamlit run app.py
      
      Usage
      
      Select a model (Flash 2.5 is default).
      
      Paste student’s code and problem description, or pick one of the built-in examples.
      
      Click Get Hint → the tutor gives one step-by-step hint.
      
      Type your response, then click again to get the next hint.

**Example Debugging Scenarios**
  -Example 1: 
    Off-by-one in Loop
    numbers = [1, 2, 3, 4, 5]
    for i in range(len(numbers)):
        print(numbers[i+1])
    
    
    Problem: I want to print every element in the list numbers, but it gives me an error.

  -Example 2: Wrong Comparison Operator
    age = 20
    if age = 18:
        print("You are an adult")
    else:
        print("You are not an adult")
    
    
    Problem: The program should check if someone is 18, but I get a syntax error.

  -Example 3: Function Return Issue
    def add_numbers(a, b):
        result = a + b
     print(add_numbers(3, 4))
    
    
    Problem: I want the function to return the sum, but it prints None.

  -Example 4: Indentation Error
    def greet(name):
    print("Hello " + name)
    
    
    Problem: I want to greet the user, but it gives an indentation error.

  -Example 5: String Concatenation with Int
    name = "Alice"
    age = 25
    print("My name is " + name + " and I am " + age + " years old.")


    Problem: It should print my name and age, but crashes with a concatenation error.

 -Example 6: Logical Mistake
    for i in range(5):
        print("Number:", i)
        if i == 5:
            print("Found 5!")
    
    
    Problem: I want it to print “Found 5!” when the loop reaches 5, but it never happens.

**Prompt Design Philosophy**
      
      The AI prompt is structured to enforce educational guidance instead of spoon-feeding answers:
      
      Tutor persona: patient, encouraging, and non-authoritative
      
      Core rules: one hint at a time, progressively more specific
      
      Constraints: never reveal full code, never copy correct code, never give direct solutions
      
      Socratic method: hints escalate from conceptual → focused → specific
      
      This ensures students learn debugging skills instead of passively copying fixes.

**Repo Structure**
/FOSSEE_SUBMISSIONS_PARTH_JHA
│── app.py                # Streamlit app
│── requirements.txt      # Dependencies
│── README.md             # Documentation
