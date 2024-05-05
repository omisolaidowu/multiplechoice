class MultipleChoice:
    def __init__(self) -> None:
        self.score: int = 0
        self.answer_input: str = ""

    def questions(self):

        self.questions_data = {
            1: {
                "Question":"What is Earth?",
                "Answer":"A planet"
                },
            2: {
                "Question":"What is a worm?",
                "Answer":"An animal"
                },
                
            3: {
                "Question":"What is a chair?",
                "Answer":"An object"
                },
            
            4: {
                "Question":"Where is Nigeria?",
                "Answer":"Africa"
                }, 
        }

        return self.questions_data

    def choices(self):
        self.choices_data = {
            1:{
                "A": "Non-habitable",
                "B": "A planet",
                "C": "A plain land",
                "D": "Just a place"
            },

            2:{
                "A": "A rope",
                "B": "An insect",
                "C": "An animal",
                "D": "An object"
            },

            3:{
                "A": "A thing",
                "B": "An object",
                "C": "An animal",
                "D": "An insect"
            },

            4:{
                "A": "Europe",
                "B": "Asia",
                "C": "Africa",
                "D": "America"
            },

        }

        return self.choices_data

    def current_question(self, question_number):
        question = self.questions()[question_number]["Question"]

        return question
    
    def current_choice(self, question_number):
        choices = self.choices()[question_number]

        for key, value in choices.items():
            yield f"{key}. {value}"

    def current_answer(self, question_number):
        answer = self.questions()[question_number]["Answer"]

        return answer
    
    def option_checker(self, question_number):
        choices= self.choices()[question_number]

        answer = self.current_answer(question_number)

        for key, value in choices.items():
            if value == answer:
                return key
    
    def check_answer(self, question_number):
        answer = self.option_checker(question_number)

        if self.answer_input == answer:
            self.score +=1

        return self.score
    
    def handle_questions(self, question_number):
        for i in range(1, len(self.questions()) + 1):
            print(self.current_question(i))

            for choice in self.current_choice(i):
                print(choice)
            
            self.answer_input = input()

            self.check_answer(i)

        print(f"Your total score is: {self.check_answer(question_number)}")


MultipleChoice().handle_questions(1)