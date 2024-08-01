# bhartyacoin-// script.js

// Get the HTML elements
const balanceElement = document.getElementById('balance');
const tapAndEarnButton = document.getElementById('tap-and-earn');
const collectComboCardButton = document.getElementById('collect-combo-card');
const collectMiningCardButton = document.getElementById('collect-mining-card');
const boostButton = document.getElementById('boost');
const dailyCheckInButton = document.getElementById('daily-check-in');

// Initialize the game state
let balance = 0;
let comboCardCount = 0;
let miningCardCount = 0;
let boostMultiplier = 1;

// Update the balance display
function updateBalance() {
  balanceElement.textContent = `Your current balance is: ${balance} coins`;
}

// Handle button clicks
tapAndEarnButton.addEventListener('click', () => {
  balance += 10 * boostMultiplier;
  updateBalance();
});

collectComboCardButton.addEventListener('click', () => {
  comboCardCount++;
  balance += 50 * boostMultiplier;
  updateBalance();
});

collectMiningCardButton.addEventListener('click', () => {
  miningCardCount++;
  balance += 100 * boostMultiplier;
  updateBalance();
});

boostButton.addEventListener('click', () => {
  boostMultiplier *= 2;
  updateBalance();
});

dailyCheckInButton.addEventListener('click', () => {
  balance += 1000 * boostMultiplier;
  updateBalance();
});

// Initialize the game
updateBalance();
