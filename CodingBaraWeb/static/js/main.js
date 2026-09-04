const minDisplay = document.getElementById('minutes');
const secDisplay = document.getElementById('seconds');
const startBtn = document.getElementById('start');
const pauseBtn = document.getElementById('pause');
const resetBtn = document.getElementById('reset');

const DEFAULT_DURATION = 25 * 60; // 25 minutes in seconds
let timeLeft = DEFAULT_DURATION;
let timerId = null;

// Formats numbers with a leading zero (e.g. 5 -> "05")
function updateDisplay() {
    const minutes = Math.floor(timeLeft / 60);
    const seconds = timeLeft % 60;

    minDisplay.textContent = String(minutes).padStart(2, '0');
    secDisplay.textContent = String(seconds).padStart(2, '0');
}

function startTimer() {
    // Prevent multiple intervals running simultaneously
    if (timerId !== null) return;

    timerId = setInterval(() => {
        if (timeLeft > 0) {
            timeLeft--;
            updateDisplay();
        } else {
            clearInterval(timerId);
            timerId = null;
            // Add optional alert, sound, or notification here
        }
    }, 1000);
}

function pauseTimer() {
    clearInterval(timerId);
    timerId = null;
}

function resetTimer() {
    pauseTimer();
    timeLeft = DEFAULT_DURATION;
    updateDisplay();
}

// Event Listeners
startBtn.addEventListener('click', startTimer);
pauseBtn.addEventListener('click', pauseTimer);
resetBtn.addEventListener('click', resetTimer);

// Initialize display on load
updateDisplay();