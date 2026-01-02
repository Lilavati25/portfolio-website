# Quick Setup Guide

## Getting Started

Your enhanced portfolio website is ready to use! Here's what you need to know:

## What's New?

### 🌟 Major Enhancements

1. **Dark/Light Mode** - Click the moon/sun icon in the navbar
2. **Animated Particles** - Interactive background in the hero section
3. **Typing Effect** - Watch your titles rotate automatically
4. **Project Filters** - Click category buttons to filter projects
5. **Skill Progress Bars** - Visual representation of your skill levels
6. **Smooth Animations** - Everything animates beautifully as you scroll
7. **Back to Top Button** - Appears when you scroll down
8. **Scroll Progress** - See your reading progress at the top

### Files to Use

✅ **Main Files** (Use these):
- `index.html`
- `styles-enhanced.css`
- `script-enhanced.js`

📦 **Legacy Files** (Backup):
- `styles.css`
- `script.js`

## Step-by-Step Customization

### 1. Update Your Information

Edit `index.html` and find these sections:

**GitHub Profile Link** (Line 44, 57, 485, 639):
```html
<a href="https://github.com/YOUR-USERNAME" target="_blank">
```

**Project Links** (Lines 190-191, 214-215, 237):
```html
<a href="https://github.com/YOUR-USERNAME/project-repo" class="project-link">
```

### 2. Add Your CV

1. Place your CV PDF file in the same folder as `index.html`
2. Name it something like `Lilavati-Mhaske-CV.pdf`
3. Edit `script-enhanced.js` (around line 264):

```javascript
downloadCV.addEventListener('click', (e) => {
    e.preventDefault();
    window.open('Lilavati-Mhaske-CV.pdf', '_blank');  // Update this line
});
```

### 3. Adjust Skill Percentages

In `index.html`, find skill progress bars (around lines 265-300):

```html
<div class="progress" data-progress="90"></div>
```

Change `data-progress="90"` to your desired percentage (0-100).

### 4. Add More Projects

Copy this template and add it to the projects section:

```html
<div class="project-card" data-category="ml ai">
    <div class="project-header">
        <h3>Your Project Title</h3>
        <div class="project-links">
            <a href="https://github.com/..." class="project-link"><i class="fab fa-github"></i></a>
            <a href="https://..." class="project-link"><i class="fas fa-external-link-alt"></i></a>
        </div>
    </div>
    <p class="project-description">Describe your project here...</p>
    <div class="project-tech">
        <span class="tech-tag">Python</span>
        <span class="tech-tag">TensorFlow</span>
    </div>
    <ul class="project-highlights">
        <li>Key achievement 1</li>
        <li>Key achievement 2</li>
    </ul>
</div>
```

**Categories** (data-category):
- `cloud` - Cloud computing projects
- `ml` - Machine Learning projects
- `ai` - AI projects
- `web` - Web development projects
- Multiple: `cloud web` or `ml ai`

### 5. Change Color Theme

Edit `styles-enhanced.css` (lines 8-20):

```css
:root {
    --primary-color: #2563eb;      /* Blue - change to your brand color */
    --secondary-color: #1e40af;    /* Dark blue */
    --accent-color: #3b82f6;       /* Light blue */
}
```

Try these color combinations:

**Purple Theme**:
```css
--primary-color: #8b5cf6;
--secondary-color: #7c3aed;
--accent-color: #a78bfa;
```

**Green Theme**:
```css
--primary-color: #10b981;
--secondary-color: #059669;
--accent-color: #34d399;
```

**Red Theme**:
```css
--primary-color: #ef4444;
--secondary-color: #dc2626;
--accent-color: #f87171;
```

### 6. Modify Typing Effect

Edit `script-enhanced.js` (around line 138):

```javascript
const phrases = [
    'Software Engineer',        // Edit these
    'Data Scientist',          // Add more
    'Your Custom Title',       // Or remove some
];
```

### 7. Update Statistics

Edit `index.html` (lines 61-76):

```html
<div class="stat-item">
    <h3>50+</h3>
    <p>Critical Defects Identified</p>
</div>
```

Change the numbers and descriptions to match your achievements.

## Testing

### 1. Open the Website

Double-click `index.html` to open it in your browser.

### 2. Test All Features

✅ **Navigation**: Click all menu items
✅ **Dark Mode**: Toggle the theme
✅ **Project Filter**: Click filter buttons
✅ **Scroll Animations**: Scroll through all sections
✅ **Contact Form**: Try submitting the form
✅ **Mobile View**: Resize browser window
✅ **Back to Top**: Scroll down and click the button

### 3. Check on Mobile

- Use browser dev tools (F12)
- Click the mobile device icon
- Test on different screen sizes

## Deployment Options

### Option 1: GitHub Pages (Free)

1. Create a GitHub repository
2. Upload all files
3. Go to Settings → Pages
4. Select main branch
5. Your site will be live at `https://username.github.io/repository-name`

### Option 2: Netlify (Free)

1. Sign up at netlify.com
2. Drag and drop your folder
3. Get instant hosting with SSL

### Option 3: Vercel (Free)

1. Sign up at vercel.com
2. Import from GitHub or upload files
3. Automatic deployments on updates

## Troubleshooting

### Dark Mode Not Working?

- Check browser console for errors (F12)
- Clear browser cache
- Make sure `script-enhanced.js` is loaded

### Animations Not Playing?

- Check if you're using `styles-enhanced.css`
- Ensure JavaScript is enabled
- Try a different browser

### Particles Not Showing?

- Canvas element may not be supported
- Check browser compatibility
- Try Chrome or Firefox

### Project Filter Not Working?

- Verify `data-category` attributes match filter buttons
- Check console for JavaScript errors
- Ensure `script-enhanced.js` is linked

## Quick Fixes

### Links Not Working?
Replace all `#` placeholders with actual URLs:
```bash
# Find in index.html:
href="#"
# Replace with:
href="https://your-actual-link.com"
```

### Images Not Loading?
If you add images later, use relative paths:
```html
<img src="./images/project-screenshot.png" alt="Description">
```

### Form Not Sending?
The form uses mailto: which opens email client. For a real backend:
- Use [Formspree](https://formspree.io/)
- Or [EmailJS](https://www.emailjs.com/)
- Or build a backend with Node.js

## Performance Tips

1. **Optimize Images**: Use WebP format, compress images
2. **Minify Files**: Use online tools to minify CSS/JS for production
3. **Enable Caching**: Configure server headers
4. **Use CDN**: For Font Awesome and other assets

## Next Steps

1. ✅ Customize all content
2. ✅ Add your actual project links
3. ✅ Upload your CV
4. ✅ Test on mobile devices
5. ✅ Deploy to hosting platform
6. ✅ Share on LinkedIn!

## Need Help?

- Check `README.md` for detailed documentation
- View browser console (F12) for error messages
- Test in incognito mode to rule out extensions

---

**Your portfolio is ready to impress! 🚀**

Good luck with your job search!
