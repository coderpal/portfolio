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

document.querySelectorAll('section').forEach(section => {
  observer.observe(section);
});

// ============================================
// Blog Category Filter
// ============================================
const filterButtons = document.querySelectorAll('.filter-btn');
const blogCards = document.querySelectorAll('.blog-card');
const emptyState = document.getElementById('empty-state');

if (filterButtons.length > 0) {
  filterButtons.forEach(button => {
    button.addEventListener('click', () => {
      // Update active button
      filterButtons.forEach(btn => btn.classList.remove('active'));
      button.classList.add('active');
      
      const category = button.getAttribute('data-category');
      let visibleCount = 0;
      
      // Filter blog cards
      blogCards.forEach(card => {
        const cardCategories = card.getAttribute('data-categories') || '';
        const categoriesList = cardCategories.split(' ').filter(c => c.length > 0);
        
        if (category === 'all' || categoriesList.includes(category)) {
          card.style.display = 'block';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });
      
      // Show/hide empty state message
      if (emptyState) {
        if (visibleCount === 0) {
          emptyState.style.display = 'flex';
          // Update the category name in the message
          const categoryName = button.textContent.trim();
          const categorySpan = emptyState.querySelector('.empty-category-name');
          if (categorySpan) {
            categorySpan.textContent = categoryName;
          }
        } else {
          emptyState.style.display = 'none';
        }
      }
    });
  });
}

// ============================================
// Console Easter Egg
// ============================================
console.log('%c👋 Hey there, fellow developer!', 'font-size: 20px; color: #F97316;');
console.log('%cThanks for checking out my portfolio.', 'font-size: 14px; color: #CBD5E1;');
console.log('%cFeel free to reach out: rahul.r.pal@outlook.in', 'font-size: 12px; color: #94A3B8;');