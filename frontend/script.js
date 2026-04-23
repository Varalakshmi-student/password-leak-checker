async function checkPassword() {
    const password = document.getElementById('passwordInput').value;
    const resultDiv = document.getElementById('result');

    if (!password) {
        resultDiv.innerHTML = '<span style="color:orange">Please enter a password.</span>';
        return;
    }

    resultDiv.innerHTML = 'Checking...';

    try {
        const response = await fetch('http://127.0.0.1:5000/check', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ password })
        });

        const data = await response.json();

        if (data.leaked) {
            resultDiv.innerHTML = '<span style="color:red">⚠️ LEAKED! Found in: ' + data.source + '</span>';
        } else {
            resultDiv.innerHTML = '<span style="color:green">✅ Safe! Not found in any breach.</span>';
        }
    } catch (error) {
        resultDiv.innerHTML = '<span style="color:red">Error connecting to server.</span>';
        console.error(error);
    }
}