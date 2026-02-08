// Button loading animation
const form = document.querySelector("form");
const button = document.querySelector("button");

if (form) {
    form.addEventListener("submit", () => {
        button.innerText = "Predicting...";
        button.disabled = true;
        button.classList.add("loading");
    });
}

// Result animation (smooth pop)
const resultBox = document.querySelector(".result-box");
if (resultBox) {
    resultBox.style.opacity = 0;
    resultBox.style.transform = "scale(0.9)";

    setTimeout(() => {
        resultBox.style.transition = "all 0.6s ease";
        resultBox.style.opacity = 1;
        resultBox.style.transform = "scale(1)";
    }, 200);
}

// Input focus glow
const inputs = document.querySelectorAll("input");
inputs.forEach(input => {
    input.addEventListener("focus", () => {
        input.style.boxShadow = "0 0 12px rgba(139, 90, 43, 0.4)";
    });

    input.addEventListener("blur", () => {
        input.style.boxShadow = "none";
    });
});
