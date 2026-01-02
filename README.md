# Portfolio Website - Lilavati Mhaske

A modern, interactive, and fully responsive portfolio website showcasing skills, projects, experience, and achievements.

## Features

### Advanced Interactivity
- **Dark/Light Mode Toggle** - Persistent theme switching with localStorage
- **Animated Particles Background** - Canvas-based interactive particle system in hero section
- **Typing Animation** - Rotating job titles with smooth typing effect
- **Project Filtering** - Filter projects by category (Cloud, ML, AI, Web)
- **Smooth Scroll Animations** - Elements fade in as you scroll
- **Progress Bars** - Animated skill level indicators
- **Counter Animation** - Stats counter with smooth number transitions
- **Back to Top Button** - Appears on scroll with smooth animation
- **Scroll Progress Indicator** - Visual progress bar at top of page
- **Scroll Indicator** - Animated mouse icon in hero section

### Modern UI/UX
- **Gradient Backgrounds** - Eye-catching color gradients
- **Glassmorphism** - Modern blur effects on navigation
- **Hover Effects** - Interactive animations on cards and buttons
- **Responsive Design** - Mobile-first approach, works on all devices
- **Custom Cursor** - Enhanced cursor follower (desktop only)
- **Smooth Transitions** - Professional animations throughout

### Sections
1. **Hero Section** - Introduction with animated particles and typing effect
2. **About Section** - Professional summary with animated statistics
3. **Experience Section** - Interactive timeline of work history
4. **Projects Section** - Filterable project showcase
5. **Skills Section** - Categorized skills with progress bars
6. **Education Section** - Academic background, certifications, and awards
7. **Contact Section** - Contact information and working email form

### Technical Highlights
- Pure HTML, CSS, and JavaScript (no frameworks)
- CSS Custom Properties for theming
- Canvas API for particle animation
- Intersection Observer for scroll animations
- localStorage for theme persistence
- Responsive breakpoints for mobile/tablet/desktop
- Performance optimized with debouncing
- SEO-friendly semantic HTML

## File Structure

```
Portfolio-website/
├── index.html              # Main HTML file
├── styles-enhanced.css     # Enhanced CSS with all styling
├── script-enhanced.js      # Enhanced JavaScript with all features
├── styles.css              # Original CSS (legacy)
├── script.js               # Original JavaScript (legacy)
└── README.md               # This file
```

## How to Use

1. **Open the website**: Simply open `index.html` in any modern web browser
2. **Customize content**: Edit `index.html` to update your information
3. **Adjust colors**: Modify CSS variables in `styles-enhanced.css` `:root` section
4. **Add your CV**: Replace the download CV link with your actual PDF file

## Customization

### Change Color Scheme

Edit the CSS variables in `styles-enhanced.css`:

```css
:root {
    --primary-color: #2563eb;    /* Main brand color */
    --secondary-color: #1e40af;  /* Secondary color */
    --accent-color: #3b82f6;     /* Accent highlights */
}
```

### Add Projects

Add new project cards in `index.html`:

```html
<div class="project-card" data-category="your-category">
    <div class="project-header">
        <h3>Your Project Name</h3>
        <div class="project-links">
            <a href="#" class="project-link"><i class="fab fa-github"></i></a>
        </div>
    </div>
    <p class="project-description">Description here...</p>
    <div class="project-tech">
        <span class="tech-tag">Technology</span>
    </div>
</div>
```

### Modify Typing Effect

Edit the phrases array in `script-enhanced.js`:

```javascript
const phrases = [
    'Software Engineer',
    'Your Custom Title',
    // Add more...
];
```

### Enable CV Download

In `script-enhanced.js`, replace the notification with:

```javascript
downloadCV.addEventListener('click', (e) => {
    e.preventDefault();
    window.open('path-to-your-cv.pdf', '_blank');
});
```

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

- Lightweight (~50KB total uncompressed)
- No external dependencies except Font Awesome icons
- Optimized animations with requestAnimationFrame
- Debounced scroll events for better performance
- Lazy-loaded animations using Intersection Observer

## Features Breakdown

### Dark Mode
- Toggle between light and dark themes
- Persists across browser sessions
- Smooth transition animations
- Optimized color schemes for both modes

### Particle Animation
- 80 interactive particles
- Connected with dynamic lines
- Responsive to screen size
- Optimized canvas rendering

### Project Filtering
- Filter by All, Cloud, ML, AI, Web
- Smooth fade in/out transitions
- Maintains responsive grid layout

### Skill Progress Bars
- Animates on scroll into view
- Customizable percentages
- Gradient progress fills
- Only animates once for performance

### Contact Form
- Client-side validation
- Opens default email client with pre-filled data
- Success notification
- Responsive layout

## Easter Eggs

Try the Konami Code: ↑ ↑ ↓ ↓ ← → ← → B A

## License

Personal portfolio website. Feel free to use as inspiration but please don't copy directly.

## Author

**Lilavati Mhaske**
- Email: mhaskelilavati4545@gmail.com
- LinkedIn: [linkedin.com/in/lilavati-mhaske](https://www.linkedin.com/in/lilavati-mhaske/)
- Location: Leicester, UK

---

Built with ❤️ using HTML, CSS, and JavaScript
