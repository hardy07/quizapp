from django.shortcuts import render, redirect
from .models import Question  # Make sure to use the correct model name

# Home view to display the quiz
def home(request):
    context = {}
    question_list = Question.objects.all()  # Fetch all questions from the database
    
    # Initialize session variables if they don't exist
    if 'qnumber' not in request.session.keys():
        request.session['qnumber'] = 0
        request.session['score'] = 0
    
    # Get the current question based on qnumber
    qs = question_list[request.session['qnumber']]
    
    # Pass the question and options to the context
    context['question'] = qs.question_text
    context['op1'] = qs.option_1
    context['op2'] = qs.option_2
    context['op3'] = qs.option_3
    context['op4'] = qs.option_4
    
    # Handle the POST request when the user selects an answer
    if request.method == "POST":
        target = request.POST.get('target')
        
        if target == "optionclick":
            answervalue = request.POST.get('answervalue')
            
            # Check if the answer is correct
            if answervalue == qs.option_1 or answervalue == qs.option_2 or answervalue == qs.option_3 or answervalue == qs.option_4:
                if answervalue == qs.answer:
                    request.session['score'] += 1

            
            # Move to the next question
            request.session['qnumber'] += 1
            if request.session['qnumber'] > len(question_list) - 1:
                return redirect('leaderboard')  # Redirect to the leaderboard if all questions are answered
            
            # Get the next question
            qs = question_list[request.session['qnumber']]
            context['question'] = qs.question_text
            context['op1'] = qs.option_1
            context['op2'] = qs.option_2
            context['op3'] = qs.option_3
            context['op4'] = qs.option_4
    
    # Pass the current score to the template
    context['score'] = request.session['score']
    
    return render(request, 'index.html', context)

# Admin panel to add new questions
def adminpanel(request):
    if request.method == "POST":
        target = request.POST.get("target")
        if target == "add_question":
            # Get form data
            question_text = request.POST.get('question', '')
            op1 = request.POST.get('op1', '')
            op2 = request.POST.get('op2', '')
            op3 = request.POST.get('op3', '')
            answer = request.POST.get('answer', '')

            # Validate if all fields are provided
            if not question_text or not op1 or not op2 or not op3 or not answer:
                return render(request, 'admin.html', {'error': 'All fields are required!'})

            # Save the new question to the database
            new_question = Question(
                question_text=question_text,
                option_1=op1,
                option_2=op2,
                option_3=op3,
                answer=answer
            )
            new_question.save()
        
    return render(request, 'admin.html')
