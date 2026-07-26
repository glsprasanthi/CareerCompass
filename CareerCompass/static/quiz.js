const questions = document.querySelectorAll(".question");
const nextBtn = document.getElementById("nextBtn");
const submitBtn = document.getElementById("submitBtn");
const currentQuestion = document.getElementById("currentQuestion");
const form = document.querySelector(".quiz-container form");

let current = 0;

nextBtn.addEventListener("click", () => {

    const selected =
        questions[current].querySelector("input[type='radio']:checked");

    if (!selected) {
        alert("Please select an option.");
        return;
    }

    questions[current].classList.remove("active");

    current++;

    questions[current].classList.add("active");

    currentQuestion.textContent = current + 1;

    if (current === questions.length - 1) {
        nextBtn.style.display = "none";
        submitBtn.style.display = "inline-block";
    }
});

form.addEventListener("submit", (event) => {
    const selected = questions[current].querySelector("input[type='radio']:checked");

    if (!selected) {
        event.preventDefault();
        alert("Please select an option.");
    }
});
