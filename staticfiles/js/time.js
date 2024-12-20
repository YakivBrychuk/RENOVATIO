function updateClock() {
    const clockElement = document.getElementById('clock');
    const now = new Date();

    // Formatting date and time with leading zero
    const day = String(now.getDate()).padStart(2, '0');
    const month = String(now.getMonth() + 1).padStart(2, '0');
    const year = now.getFullYear();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');

    // Creating the clock string with dots as separators
    const formattedTime = `${day}·${month}·${year}·${hours}·${minutes}·${seconds}`;

    // Set the text content to the formatted string
    clockElement.textContent = formattedTime;
}

// Update clock every second
setInterval(updateClock, 1000);
// Initial call to set the clock immediately when the page loads
updateClock();
