let count = 0;

/**
 * Simulates updating the display by logging the current count value to the console.
 */
function updateDisplay() {
    console.log(`Current Count: ${count}`);
    
    // Logic for color/state feedback
    if (count > 0) {
        console.log("Status: Positive");
    } else if (count < 0) {
        console.log("Status: Negative");
    } else {
        console.log("Status: Neutral (Zero)");
    }
}


function handleIncrement() {
    try {
        count++; // Increase the count by one
        updateDisplay();
        showMessage('Value increased!');
    } catch (error) {
        // In a real application, you'd handle the error here.
        console.error("Error during increment:", error);
        showMessage('An error occurred!');
    }
}


function handleReset() {
    if (count !== 0) {
        count = 0; 
        updateDisplay();
        showMessage('Counter reset to 0.');
    } else {
        showMessage('Counter is already at 0.');
    }
}


function showMessage(message) {
    console.log(`Message: ${message}`);
}



console.log("--- Counter App Start ---");
updateDisplay(); 

handleIncrement(); 
handleIncrement(); 

handleReset();
handleReset();
