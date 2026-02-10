document.addEventListener('DOMContentLoaded', () => {
    console.log("Electronic Textbook Loaded");

    const tocLinks = document.querySelectorAll('aside ul li a');
    const sections = [];

    // Map links to sections
    tocLinks.forEach(link => {
        const id = link.getAttribute('href').substring(1);
        const section = document.getElementById(id);
        if (section) {
            sections.push({
                id: id,
                link: link,
                offset: section.offsetTop
            });
        }
    });

    // Add scroll listener
    window.addEventListener('scroll', () => {
        // Offset for header/padding. Increased to 300 to highlight sections earlier.
        const scrollPosition = window.scrollY + 350;

        let currentSection = null;

        for (const section of sections) {
            // Update offset dynamically in case layout changes (e.g., images loading)
            const element = document.getElementById(section.id);
            if (element && element.offsetTop <= scrollPosition) {
                currentSection = section;
            }
        }

        tocLinks.forEach(link => link.classList.remove('active'));

        if (currentSection) {
            currentSection.link.classList.add('active');
        } else if (sections.length > 0 && window.scrollY < sections[0].offset) {
            // Optional: highlight first item if near top, or none
            // sections[0].link.classList.add('active'); 
        }
    });
});
