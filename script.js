/* 
   Param Setu - Income Protection
   Interaction Logic
*/

// Screen Navigation
function navigateTo(targetScreenId) {
    const screens = document.querySelectorAll('.screen');
    const targetScreen = document.getElementById(targetScreenId);
    
    // Find currently active screen
    const currentScreen = document.querySelector('.screen.active');
    
    if (currentScreen && currentScreen.id !== targetScreenId) {
        // Handle transitions
        const isBack = 
            (currentScreen.id === 'screen-plans' && targetScreenId === 'screen-home') ||
            (currentScreen.id === 'screen-claim' && targetScreenId === 'screen-plans') || 
            (currentScreen.id === 'screen-claim' && targetScreenId === 'screen-home');

        if (isBack) {
            // Animating backwards
            currentScreen.style.transform = 'translateX(100%)';
            currentScreen.style.opacity = '0';
            
            targetScreen.style.transform = 'translateX(0)';
            targetScreen.style.opacity = '1';
        } else {
            // Animating forwards
            currentScreen.style.transform = 'translateX(-30%)';
            currentScreen.style.opacity = '0';
            
            targetScreen.style.transform = 'translateX(0)';
            targetScreen.style.opacity = '1';
        }
        
        // Wait for animation to finish before removing/adding active classes
        setTimeout(() => {
            currentScreen.classList.remove('active');
            targetScreen.classList.add('active');
            
            // Reset transforms so CSS can take over again properly
            currentScreen.style.transform = '';
            currentScreen.style.opacity = '';
            targetScreen.style.transform = '';
            targetScreen.style.opacity = '';
        }, 50); // Small delay to ensure CSS transition triggers
    }
}

// Plan Selection
function selectPlan(selectedCard) {
    // Remove active class from all plans
    document.querySelectorAll('.plan-card').forEach(card => {
        card.classList.remove('active');
    });
    
    // Add active class to selected plan
    selectedCard.classList.add('active');
}

// Ensure the first screen is properly initialized on load
document.addEventListener('DOMContentLoaded', () => {
    // Optional: Add some entry animations for home screen
    const homeElements = document.querySelectorAll('#screen-home .hero-section, #screen-home .info-card, #screen-home .disclaimer');
    
    homeElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = `all 0.5s cubic-bezier(0.16, 1, 0.3, 1) ${0.1 * index}s`;
        
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'translateY(0)';
        }, 100);
    });
});
