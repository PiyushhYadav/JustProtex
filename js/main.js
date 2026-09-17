window.initHeaderJS = function() {
  // Desktop Dropdown
  const desktopTrigger = document.querySelector('.dropdown-trigger');
  const desktopMenu = document.getElementById('solutions-menu');

  if (desktopTrigger && desktopMenu) {
    desktopTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isExpanded = desktopTrigger.getAttribute('aria-expanded') === 'true';
      
      desktopTrigger.setAttribute('aria-expanded', !isExpanded);
      if (!isExpanded) {
        desktopMenu.classList.add('show');
      } else {
        desktopMenu.classList.remove('show');
      }
    });
  }

  // Mobile Hamburger Toggle
  const hamburger = document.querySelector('.hamburger');
  const mobileNavPanel = document.getElementById('mobile-nav-panel');

  if (hamburger && mobileNavPanel) {
    hamburger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';
      
      hamburger.setAttribute('aria-expanded', !isExpanded);
      
      if (!isExpanded) {
        mobileNavPanel.classList.add('open');
        // Calculate the height of the inner content
        const inner = mobileNavPanel.querySelector('.mobile-nav-inner');
        mobileNavPanel.style.maxHeight = inner.scrollHeight + 'px';
      } else {
        mobileNavPanel.classList.remove('open');
        mobileNavPanel.style.maxHeight = '0px';
      }
    });
  }

  // Mobile Dropdown Toggle
  const mobileTrigger = document.querySelector('.mobile-dropdown-trigger');
  const mobileSubmenu = document.getElementById('mobile-solutions');

  if (mobileTrigger && mobileSubmenu) {
    mobileTrigger.addEventListener('click', (e) => {
      e.stopPropagation();
      const isExpanded = mobileTrigger.getAttribute('aria-expanded') === 'true';
      
      mobileTrigger.setAttribute('aria-expanded', !isExpanded);
      
      if (!isExpanded) {
        mobileSubmenu.style.maxHeight = mobileSubmenu.scrollHeight + 'px';
        // Adjust the parent panel's max-height to accommodate the submenu
        if (mobileNavPanel && mobileNavPanel.classList.contains('open')) {
          const inner = mobileNavPanel.querySelector('.mobile-nav-inner');
          mobileNavPanel.style.maxHeight = (inner.scrollHeight + mobileSubmenu.scrollHeight) + 'px';
        }
      } else {
        mobileSubmenu.style.maxHeight = '0px';
        // Re-adjust parent panel height
        if (mobileNavPanel && mobileNavPanel.classList.contains('open')) {
          const inner = mobileNavPanel.querySelector('.mobile-nav-inner');
          mobileNavPanel.style.maxHeight = inner.scrollHeight + 'px';
        }
      }
    });
  }

  // Close dropdowns when clicking outside
  document.addEventListener('click', (e) => {
    // Close Desktop Menu
    if (desktopTrigger && desktopMenu) {
      if (!desktopTrigger.contains(e.target) && !desktopMenu.contains(e.target)) {
        desktopTrigger.setAttribute('aria-expanded', 'false');
        desktopMenu.classList.remove('show');
      }
    }
  });

  // Handle window resize to reset mobile states
  window.addEventListener('resize', () => {
    if (window.innerWidth >= 860) {
      if (hamburger && hamburger.getAttribute('aria-expanded') === 'true') {
        hamburger.setAttribute('aria-expanded', 'false');
        mobileNavPanel.style.maxHeight = '0px';
        mobileNavPanel.classList.remove('open');
      }
      if (mobileTrigger && mobileTrigger.getAttribute('aria-expanded') === 'true') {
        mobileTrigger.setAttribute('aria-expanded', 'false');
        mobileSubmenu.style.maxHeight = '0px';
      }
    }
  });

  // Dynamic header height for scroll anchoring
  function updateHeaderHeight() {
    const header = document.querySelector('header');
    if (header) {
      const rect = header.getBoundingClientRect();
      const topOffset = parseInt(window.getComputedStyle(header).top, 10) || 0;
      const totalHeight = rect.height + topOffset;
      document.documentElement.style.setProperty('--header-height', totalHeight + 'px');
    }
  }
  updateHeaderHeight();
  window.addEventListener('resize', updateHeaderHeight);

};
document.addEventListener('DOMContentLoaded', window.initHeaderJS);
