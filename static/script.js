document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide Icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Confirmation for leaving the quiz
    const quizForm = document.getElementById('quizForm');
    if (quizForm) {
        window.onbeforeunload = () => "Are you sure you want to leave? Progress will be lost.";
        quizForm.onsubmit = () => {
            window.onbeforeunload = null;
        };
    }
});