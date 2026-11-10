/*
==============================================
PORTFOLIO DIRECTORY STRUCTURE
==============================================
portfolio/
├── index.html              
├── blog.html               
├── style.css               
├── script.js               ← YOU ARE HERE
├── images/                 
│   └── blog/               
│       └── lists/          
│           └── list.png    
└── blog/                   
    └── blog-lists.html     
==============================================
FILE: script.js
DESCRIPTION: JavaScript for interactivity and animations
==============================================
*/

// ============================================
// Smooth scroll for anchor links
// ============================================
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    e.preventDefault();
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      target.scrollIntoView({
        behavior: 'smooth',
        block: 'start'
      });
    }
  });
});

// ============================================
// Fade-in animation on scroll
// ============================================
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('fade-in');
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

// Observe all sections for animation
document.querySelectorAll('section').forEach(section => {
  observer.observe(section);
});

// ============================================
// Add hover effect to skill cards
// ============================================
document.querySelectorAll('.skill-card').forEach(card => {
  card.addEventListener('mouseenter', function() {
    this.style.transform = 'translateY(-8px)';
  });
  
  card.addEventListener('mouseleave', function() {
    this.style.transform = 'translateY(0)';
  });
});

// ============================================
// Console Easter Egg
// ============================================
console.log('%c👋 Hey there, fellow developer!', 'font-size: 20px; color: #F97316;');
console.log('%cThanks for checking out my portfolio.', 'font-size: 14px; color: #CBD5E1;');
console.log('%cFeel free to reach out: rahul.r.pal@outlook.in', 'font-size: 12px; color: #94A3B8;');