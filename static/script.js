// Smart Lender JavaScript

document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");

    if (form) {
        form.addEventListener("submit", function () {

            const button = document.querySelector("button");

            button.innerHTML = "Predicting...";
            button.disabled = true;

        });
    }

});