const addExpenseButton = document.getElementById('addExpenseButton');
const submitExpense = document.getElementById('submitExpense');
const expenseList = document.querySelector('.expense-list');

addExpenseButton.addEventListener('click', () => {
    document.querySelector('.expense-form').style.display = 'block';
});

submitExpense.addEventListener('click', () => {
    const date = document.getElementById('date').value;
    const category = document.getElementById('category').value;
    const amount = document.getElementById('amount').value;
    const description = document.getElementById('description').value;

    const expenseItem = document.createElement('div');
    expenseItem.innerHTML = `
        <p><strong>Date:</strong> ${date}</p>
        <p><strong>Category:</strong> ${category}</p>
        <p><strong>Amount:</strong> ${amount}</p>
        <p><strong>Description:</strong> ${description}</p>
        <hr>
    `;
    expenseList.appendChild(expenseItem);

    // Clear form inputs
    document.getElementById('date').value = '';
    document.getElementById('category').value = 'transport';
    document.getElementById('amount').value = '';
    document.getElementById('description').value = '';
    document.querySelector('.expense-form').style.display = 'none';
});
