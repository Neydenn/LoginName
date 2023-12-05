document.addEventListener('DOMContentLoaded', function() {
    const mainScreen = document.querySelector('.main-screen');
    const numberButtons = document.querySelectorAll('.wrapper button:not(.button-clear):not(.button-result)');
    const clearButton = document.querySelector('.button-clear');

    numberButtons.forEach(button => {
        button.addEventListener('click', () => {
            appendNumber(button.textContent);
        });
    });

    clearButton.addEventListener('click', clearScreen);

    function appendNumber(number) {
        mainScreen.textContent += number;
    }

    function clearScreen() {
        mainScreen.textContent = '';
    }
});