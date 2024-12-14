from django.shortcuts import render

QUESTIONS = [
    {'question': 'Which of the following is a supervised learning algorithm?', 'options': ['K-means', 'Linear Regression', 'DBSCAN', 'PCA'], 'answer': 'Linear Regression'},
    {'question': 'Which function is commonly used as an activation function in neural networks?', 'options': ['ReLU', 'Sigmoid', 'Tanh', 'All of the above'], 'answer': 'All of the above'},
    {'question': 'Which metric is used to evaluate classification models?', 'options': ['Mean Squared Error', 'Confusion Matrix', 'R-squared', 'Silhouette Score'], 'answer': 'Confusion Matrix'},
    {'question': 'Which of the following is a type of unsupervised learning?', 'options': ['Classification', 'Regression', 'Clustering', 'None of the above'], 'answer': 'Clustering'},
    {'question': 'Which of the following is used to prevent overfitting in machine learning models?', 'options': ['Dropout', 'L2 Regularization', 'Cross-validation', 'All of the above'], 'answer': 'All of the above'},
    {'question': 'Which library is most commonly used for deep learning?', 'options': ['Pandas', 'NumPy', 'TensorFlow', 'Matplotlib'], 'answer': 'TensorFlow'},
    {'question': 'Which method is used to reduce the dimensionality of data?', 'options': ['Principal Component Analysis (PCA)', 'K-means Clustering', 'Decision Trees', 'Random Forest'], 'answer': 'Principal Component Analysis (PCA)'},
    {'question': 'What is the main objective of gradient descent?', 'options': ['Maximize the loss function', 'Minimize the loss function', 'Normalize the data', 'Increase the number of features'], 'answer': 'Minimize the loss function'},
    {'question': 'Which type of learning involves rewards and punishments?', 'options': ['Supervised Learning', 'Unsupervised Learning', 'Reinforcement Learning', 'Semi-supervised Learning'], 'answer': 'Reinforcement Learning'},
    {'question': 'Which of the following is a loss function used in regression?', 'options': ['Cross-Entropy Loss', 'Hinge Loss', 'Mean Squared Error', 'Categorical Cross-Entropy'], 'answer': 'Mean Squared Error'},
    {'question': 'Which of the following is an ensemble learning method?', 'options': ['Decision Tree', 'K-Nearest Neighbors', 'Random Forest', 'Logistic Regression'], 'answer': 'Random Forest'},
    {'question': 'What is overfitting in machine learning?', 'options': ['Model performs well on both training and test data', 'Model performs well on training data but poorly on test data', 'Model performs poorly on training data but well on test data', 'None of the above'], 'answer': 'Model performs well on training data but poorly on test data'},
    {'question': 'Which of the following is a feature scaling technique?', 'options': ['One-Hot Encoding', 'Label Encoding', 'Normalization', 'Bagging'], 'answer': 'Normalization'},
]


def index(request):
    return render(request, 'index.html')


def quiz(request):
    if request.method == 'POST':
        selected_answers = [request.POST.get(f'question_{i + 1}') for i in range(len(QUESTIONS))]
        correct_answers = [q['answer'] for q in QUESTIONS]
        score = sum(1 for i in range(len(selected_answers)) if selected_answers[i] == correct_answers[i])
        return render(request, 'result.html', {'score': score, 'total': len(QUESTIONS)})

    return render(request, 'quiz.html', {'questions': QUESTIONS})
