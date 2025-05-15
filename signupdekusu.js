// Toggle dark mode
const darkModeToggle = document.getElementById('darkModeToggle');
const body = document.body;

darkModeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-mode');
    
    const Logo = document.getElementById('Logo');

    if (body.classList.contains('dark-mode')) {
        darkModeToggle.textContent = '☾';
        Logo.src = '/dekusu logo(Dark).png'
        
    } else {
        darkModeToggle.textContent = '☀︎';
        Logo.src = '/dekusu logo.png'
    }
});

document.getElementById('visitorform').addEventListener('submit', function(e) {
    e.preventDefault();

    const form = document.getElementById('Purpose').value;
    if (form){
        window.location.href = '/dashboard(guest).html';
    }
});

// Handle form submission
document.getElementById('loginForm').addEventListener('submit', (e) => {
    e.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email === 'admin@adnu.edu.ph' && password === 'password123') {
        alert('Login successful! Redirecting...');
        window.location.href = '/dashboard.html';
    } 
    else {
        alert('Invalid email or password. Please try again.');
    }
});

//VisitorForm
const overlay = document.getElementById("overlay");
const visitorBtn = document.getElementById("visitor");

// Show overlay
visitorBtn.addEventListener("click", () => {
    overlay.classList.add("show");
    document.querySelector(".overlay-content").classList.add("show");
});

// Close overlay
function closeOverlay() {
    overlay.classList.remove("show");
    document.querySelector(".overlay-content").classList.remove("show");
}



// Close when clicking outside the form
overlay.addEventListener("click", (e) => {
    if (e.target === overlay) {
        closeOverlay();
    }
});

document.querySelector('select').addEventListener('click', function() {
    this.style.position = 'relative';
    this.style.top = 'auto';
});
