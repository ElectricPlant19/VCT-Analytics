# Design Philosophy & UI/UX Guidelines

## Design Vision

Create a dashboard that feels like **premium esports software** — the kind of interface that professional analysts would pay $500/month to use. It should feel powerful yet approachable, data-dense yet never overwhelming, and unmistakably *Valorant*.

**Core Principles**:
1. **Competitive Edge**: Design for decision-making speed
2. **Visual Hierarchy**: Guide the eye to what matters most
3. **Contextual Clarity**: Every number tells a story
4. **Aesthetic Excellence**: Beauty enables understanding
5. **Responsive Intelligence**: Adapt to user intent

---

## Visual Identity

### Brand Alignment: Valorant + Esports

**Valorant's DNA**:
- Sleek, tactical, near-future aesthetic
- Bold angular geometry
- High contrast (dark backgrounds, bright accents)
- Clean typography (sans-serif, readable at distance)
- Vibrant accent colors (red, teal, gold)
- Subtle glows and lighting effects

**Esports Broadcast Feel**:
- Think Riot Games production quality
- ESPN stats graphics sophistication
- Twitch overlay polish
- Professional yet exciting

### Color Palette

#### Primary Colors
```
Background (Dark):
- Primary BG: #0F1923 (deep navy blue, almost black)
- Secondary BG: #1C2733 (slightly lighter panels)
- Elevated BG: #232E3C (cards, modals)
- Borders: #2E3A47 (subtle separators)

Valorant Red (Primary Accent):
- Primary Red: #FF4655 (Valorant signature red)
- Red Hover: #FF6B76 (lighter on hover)
- Red Pressed: #E63946 (darker on press)
- Red Glow: rgba(255, 70, 85, 0.3) (for glows/shadows)

Text:
- Primary Text: #FFFFFF (pure white, high contrast)
- Secondary Text: #B4BCC8 (muted blue-gray, 70% opacity)
- Tertiary Text: #6E7A8A (de-emphasized, 45% opacity)
- Disabled Text: #4A5568 (very muted, 25% opacity)
```

#### Accent Colors (Semantic)
```
Success/Positive:
- Green: #46FFA6 (bright mint green, for wins/gains)
- Green Glow: rgba(70, 255, 166, 0.2)

Warning/Neutral:
- Yellow: #FFC846 (gold, for warnings/draws)
- Yellow Glow: rgba(255, 200, 70, 0.2)

Error/Negative:
- Red: #FF4655 (same as primary, for losses/declines)

Information:
- Teal: #46D9FF (bright cyan, for info/highlights)
- Teal Glow: rgba(70, 217, 255, 0.2)

Agent Role Colors:
- Duelist: #FF4655 (red)
- Initiator: #FFC846 (gold)
- Controller: #B446FF (purple)
- Sentinel: #46FFA6 (green)
```

#### Data Visualization Colors
```
Sequential (Light to Dark):
- Use for heatmaps, choropleth maps, gradient scales
- Scale: #0F1923 → #FF4655 (dark to Valorant red)

Diverging (Negative to Positive):
- Negative: #FF4655 (red) → Neutral: #6E7A8A (gray) → Positive: #46FFA6 (green)

Categorical (Distinct):
- Team/Player comparisons: Use rainbow with enough contrast
- Palette: #FF4655, #46D9FF, #FFC846, #B446FF, #46FFA6, #FF8C46, #C846FF, #46FFED

Avoid:
- Pure colors (too harsh on dark backgrounds)
- Low-contrast combinations
- Red-green only comparisons (colorblind accessibility)
```

### Typography

#### Font Families
```
Primary Font: 'Inter', 'SF Pro Display', -apple-system, BlinkMacSystemFont, sans-serif
- Use for: Body text, data labels, UI elements
- Rationale: Clean, modern, excellent readability at all sizes

Monospace Font: 'JetBrains Mono', 'Fira Code', 'Consolas', monospace
- Use for: Numerical data, timestamps, code snippets
- Rationale: Tabular alignment, professional feel

Display Font (Optional): 'Druk Wide', 'Tungsten', 'Bebas Neue', sans-serif
- Use for: Large headers, hero text, tournament names (sparingly)
- Rationale: Bold impact, competitive energy
```

#### Type Scale
```
Massive Display: 64px / 4rem (tournament headers, hero numbers)
Large Display: 48px / 3rem (page titles)
Display: 36px / 2.25rem (section headers)
Heading 1: 28px / 1.75rem (card titles)
Heading 2: 24px / 1.5rem (subsections)
Heading 3: 20px / 1.25rem (small headers)
Body Large: 18px / 1.125rem (prominent body text)
Body: 16px / 1rem (default body text)
Body Small: 14px / 0.875rem (secondary text, labels)
Caption: 12px / 0.75rem (metadata, footnotes)
Tiny: 10px / 0.625rem (micro-labels, timestamps)
```

#### Font Weights
```
- Light (300): Rarely, only for massive display text
- Regular (400): Body text default
- Medium (500): Emphasized body, button labels
- Semibold (600): Headers, important labels
- Bold (700): Hero numbers, critical information
- Black (900): Tournament titles, massive displays
```

#### Line Height & Spacing
```
- Display text: 1.1 (tight, impactful)
- Headers: 1.2 (slightly tight)
- Body text: 1.6 (comfortable reading)
- Data labels: 1.4 (balanced)
- Captions: 1.5 (legible)
```

---

## Layout & Composition

### Grid System
```
Desktop (1920px):
- 12-column grid
- Gutter: 24px
- Margin: 64px (left/right)
- Max content width: 1792px

Laptop (1366px):
- 12-column grid
- Gutter: 20px
- Margin: 48px

Tablet (768px):
- 8-column grid
- Gutter: 16px
- Margin: 32px

Mobile (375px):
- 4-column grid
- Gutter: 12px
- Margin: 16px
```

### Spacing System (8pt Grid)
```
Micro: 4px (tight spacing, icon padding)
Tiny: 8px (compact elements)
Small: 12px (related items)
Base: 16px (default spacing)
Medium: 24px (section padding)
Large: 32px (major sections)
XLarge: 48px (page sections)
XXLarge: 64px (page margins)
Massive: 96px (hero sections)
```

### Component Hierarchy

**Z-Index Layers**:
```
Base layer (0): Background, main content
Elevated (10): Cards, panels
Dropdown (100): Dropdowns, popovers
Sticky (500): Sticky headers, filters
Overlay (1000): Modal backgrounds
Modal (1100): Modal dialogs
Tooltip (1200): Tooltips, toasts
Critical (9999): Critical alerts
```

**Visual Weight**:
1. **Hero section**: Largest, boldest, most colorful
2. **Primary KPIs**: Large numbers, high contrast
3. **Main visualizations**: Central focus
4. **Supporting data**: Smaller, less prominent
5. **Metadata**: Subtle, low contrast

---

## Component Design System

### Cards & Panels

**Base Card**:
```
Background: #1C2733
Border: 1px solid #2E3A47
Border Radius: 12px
Padding: 24px
Box Shadow: 0 4px 12px rgba(0, 0, 0, 0.3)

Hover State:
- Border: 1px solid #3D4A57
- Box Shadow: 0 6px 20px rgba(0, 0, 0, 0.4)
- Subtle lift (transform: translateY(-2px))
```

**Stat Card** (for KPIs):
```
Background: Gradient from #1C2733 to #232E3C
Border: None (use subtle inner shadow instead)
Border Radius: 16px
Padding: 32px
Large Number: 48px, Bold, White
Label: 14px, Secondary Text
Icon: Top-right, 32px, Accent Color with 20% opacity background
Trend Indicator: Small arrow + percentage
```

**Comparison Card** (side-by-side stats):
```
Split layout (50/50 or 33/33/33)
Divider: 1px vertical line, #2E3A47
Each side has own background gradient
Highlight winner with subtle accent glow
```

### Buttons

**Primary Button**:
```
Background: Linear gradient #FF4655 to #E63946
Text: #FFFFFF, 16px, Medium weight
Border Radius: 8px
Padding: 12px 24px
Box Shadow: 0 2px 8px rgba(255, 70, 85, 0.4)

Hover:
- Background: Lighter gradient #FF6B76 to #FF4655
- Box Shadow: 0 4px 12px rgba(255, 70, 85, 0.6)
- Cursor: pointer

Active:
- Background: Darker gradient #E63946 to #D62936
- Transform: scale(0.98)
```

**Secondary Button**:
```
Background: Transparent
Border: 1px solid #FF4655
Text: #FF4655, 16px, Medium weight
Border Radius: 8px
Padding: 12px 24px

Hover:
- Background: rgba(255, 70, 85, 0.1)
- Border: 1px solid #FF6B76
```

**Ghost Button**:
```
Background: Transparent
Text: #B4BCC8, 16px, Regular weight
No border
Padding: 12px 16px

Hover:
- Text: #FFFFFF
- Background: rgba(255, 255, 255, 0.05)
```

### Form Elements

**Text Input**:
```
Background: #0F1923
Border: 1px solid #2E3A47
Border Radius: 8px
Padding: 12px 16px
Text: #FFFFFF, 16px
Placeholder: #6E7A8A

Focus:
- Border: 1px solid #FF4655
- Box Shadow: 0 0 0 3px rgba(255, 70, 85, 0.2)
- Outline: none
```

**Dropdown Select**:
```
Same as text input
Right icon: Chevron down, #B4BCC8
Dropdown menu:
- Background: #232E3C
- Border: 1px solid #2E3A47
- Box Shadow: 0 8px 24px rgba(0, 0, 0, 0.5)
- Max height: 300px (scrollable)

Option:
- Padding: 12px 16px
- Hover background: rgba(255, 70, 85, 0.1)
- Selected background: rgba(255, 70, 85, 0.2)
- Selected text: #FF4655
```

**Multi-Select**:
```
Show selected items as chips/tags
Chip:
- Background: rgba(255, 70, 85, 0.2)
- Text: #FF4655, 14px
- Border Radius: 4px
- Padding: 6px 12px
- Close icon (×): Hover to remove
```

**Checkbox**:
```
Unchecked:
- Border: 2px solid #2E3A47
- Background: Transparent
- Size: 20px × 20px
- Border Radius: 4px

Checked:
- Background: #FF4655
- Checkmark: White, bold
- Border: 2px solid #FF4655
```

**Radio Button**:
```
Unchecked:
- Border: 2px solid #2E3A47
- Background: Transparent
- Size: 20px × 20px (circle)

Checked:
- Border: 2px solid #FF4655
- Inner circle: #FF4655, 10px × 10px
```

**Toggle Switch**:
```
Off:
- Background: #2E3A47
- Knob: #6E7A8A, left position
- Width: 44px, Height: 24px

On:
- Background: #FF4655
- Knob: #FFFFFF, right position
- Subtle glow around switch
```

**Slider**:
```
Track:
- Background: #2E3A47
- Height: 6px
- Border Radius: 3px

Filled Track:
- Background: Linear gradient #FF4655 to #E63946

Thumb:
- Background: #FFFFFF
- Size: 20px × 20px (circle)
- Box Shadow: 0 2px 6px rgba(0, 0, 0, 0.3)
- Hover: Scale to 24px × 24px
```

### Navigation

**Top Navigation Bar**:
```
Background: #1C2733
Height: 72px
Border Bottom: 1px solid #2E3A47
Box Shadow: 0 2px 8px rgba(0, 0, 0, 0.3)
Fixed position (sticky)

Left: Logo (Valorant icon + "VCT Analytics")
Center: Page navigation tabs
Right: Settings, User profile, Theme toggle
```

**Navigation Tabs**:
```
Inactive Tab:
- Text: #B4BCC8, 16px, Medium
- Padding: 24px 20px
- Hover: Text #FFFFFF

Active Tab:
- Text: #FF4655, 16px, Medium
- Border Bottom: 3px solid #FF4655
- Slight glow below (rgba(255, 70, 85, 0.3))
```

**Sidebar Navigation** (if used):
```
Background: #0F1923
Width: 280px
Padding: 24px
Fixed position

Menu Item:
- Padding: 12px 16px
- Border Radius: 8px
- Icon + Text layout
- Inactive: #B4BCC8
- Hover: Background rgba(255, 255, 255, 0.05)
- Active: Background rgba(255, 70, 85, 0.2), Text #FF4655
```

**Breadcrumbs**:
```
Text: 14px, #6E7A8A
Separator: "/" or "›" in #4A5568
Current page: #FFFFFF
Clickable crumbs: Hover #FF4655
```

### Data Visualization Components

**Chart Container**:
```
Background: Transparent or subtle gradient
Padding: 24px
Border: None (let chart breathe)
Title: 20px, Semibold, above chart
Subtitle: 14px, Secondary Text, below title
Legend: Bottom or right side, 14px
```

**Chart Styling**:
```
Grid Lines:
- Color: rgba(255, 255, 255, 0.05) (very subtle)
- Horizontal only (usually)
- Dashed style (2px dash, 4px gap)

Axes:
- Axis Line: 1px solid #2E3A47
- Tick Labels: 12px, #B4BCC8, Monospace font
- Axis Title: 14px, #FFFFFF, Medium weight

Data Points/Bars:
- Primary Color: Use accent colors from palette
- Border: None or 1px darker shade
- Opacity: 0.9 default, 1.0 on hover
- Hover: Glow effect (box-shadow with accent color)

Tooltips (on chart hover):
- Background: #232E3C
- Border: 1px solid #FF4655
- Border Radius: 8px
- Padding: 12px
- Text: 14px, #FFFFFF
- Box Shadow: 0 4px 12px rgba(0, 0, 0, 0.5)
- Arrow pointing to data point
```

**Table Styling**:
```
Header Row:
- Background: #1C2733
- Text: 14px, Semibold, #FFFFFF
- Padding: 16px
- Border Bottom: 2px solid #FF4655
- Sticky on scroll

Data Rows:
- Background: Alternating #0F1923 and #1C2733 (zebra striping)
- Padding: 12px 16px
- Border Bottom: 1px solid #2E3A47
- Hover: Background rgba(255, 70, 85, 0.05)

Cells:
- Text: 14px, Monospace for numbers, Regular for text
- Alignment: Numbers right-aligned, Text left-aligned
- Text Color: #FFFFFF for primary, #B4BCC8 for secondary

Sorting:
- Sortable columns: Arrow icon (↑↓) on hover
- Active sort: Arrow highlighted in #FF4655
- Click to toggle asc/desc
```

**Heatmap**:
```
Cell:
- Size: Uniform (e.g., 60px × 60px)
- Border Radius: 4px
- Padding: 8px
- Gap: 2px between cells

Color Scale:
- Low: #0F1923 (dark blue)
- Medium: #FFC846 (gold)
- High: #FF4655 (red)
- Use smooth gradient, not discrete steps

Value Display:
- Text: 14px, Monospace, contrasting color
- Show value inside cell
- Tooltip with additional context on hover
```

**Progress Bars**:
```
Container:
- Background: #2E3A47
- Height: 8px
- Border Radius: 4px

Fill:
- Background: Linear gradient based on value
  - Low (0-33%): Red gradient
  - Medium (34-66%): Yellow gradient
  - High (67-100%): Green gradient
- Height: 8px
- Border Radius: 4px
- Smooth animation (transition: width 0.3s ease)

Label:
- Percentage: Above or right of bar
- 14px, Monospace, corresponding color
```

### Iconography

**Icon Style**:
```
- Outlined style (not filled)
- Stroke width: 2px
- Size: 24px default (scale to 16px, 32px, 48px as needed)
- Color: Match text color context
- Hover: Brighten or accent color
```

**Common Icons**:
```
- Filter: Funnel icon
- Sort: Arrow up/down
- Search: Magnifying glass
- Settings: Gear
- User: Profile silhouette
- Close: X
- Expand: Arrows pointing outward
- Info: Circled "i"
- Success: Checkmark
- Warning: Triangle with "!"
- Error: Circled "X"
- Trend Up: Arrow diagonal up
- Trend Down: Arrow diagonal down
```

**Agent Role Icons**:
```
- Duelist: Crosshair
- Initiator: Lightning bolt
- Controller: Eye
- Sentinel: Shield
```

---

## Micro-Interactions & Animations

### Principles
- **Purposeful**: Every animation serves a function (feedback, orientation, delight)
- **Subtle**: Don't distract from data
- **Fast**: 200-300ms for most interactions
- **Smooth**: Use easing functions (ease-out for entrances, ease-in for exits)

### Hover States
```
- Buttons: Scale(1.02) + brightness increase + shadow growth
- Cards: Lift (translateY(-4px)) + shadow growth
- Links: Color change to accent + underline
- Icons: Scale(1.1) + color change
- Chart elements: Glow + tooltip appearance
```

### Loading States
```
Skeleton Screens:
- Use for tables, cards, charts while data loads
- Animated gradient shimmer effect
- Background: #1C2733 → #232E3C → #1C2733
- Animation: 1.5s linear infinite

Spinners:
- Use for buttons, small components
- Circular spinner in accent color (#FF4655)
- Size: 24px default
- Rotation: 360deg in 0.8s linear infinite

Progress Indicators:
- For multi-step processes
- Linear progress bar at top of screen
- Indeterminate: Sliding bar animation
- Determinate: Fill from 0% to 100%
```

### Transitions
```
Page Transitions:
- Fade in new content: opacity 0 → 1 over 300ms
- Slide in direction: from bottom (translateY(20px) → 0)
- Easing: ease-out

Filter Application:
- Smooth data refresh: opacity 1 → 0.7 → 1
- Duration: 400ms total
- New data fades in

Modal Appearance:
- Backdrop: opacity 0 → 1 over 200ms
- Modal: scale(0.95) + opacity 0 → scale(1) + opacity 1 over 300ms
- Easing: ease-out

Dropdown Menus:
- Scale(0.95) + opacity 0 → scale(1) + opacity 1
- Origin: top-left or top-right (depending on position)
- Duration: 200ms
```

### Success Feedback
```
- Checkmark animation: Draw circle, then checkmark
- Color: #46FFA6
- Duration: 500ms
- Accompanied by subtle bounce
```

### Error Feedback
```
- Shake animation: Horizontal wobble
- Color flash: #FF4655
- Duration: 300ms
- Accompanied by error icon
```

---

## Responsive Design Patterns

### Breakpoint Behavior

**Desktop (1920px+)**:
- Full multi-column layouts
- Side-by-side comparisons
- Maximum information density
- Hover-rich interactions

**Laptop (1366px - 1919px)**:
- Slightly condensed layouts
- Maintain multi-column where possible
- Reduce whitespace
- Keep all features visible

**Tablet (768px - 1365px)**:
- Two-column max layouts
- Stack some side-by-side elements
- Larger tap targets (min 44px × 44px)
- Simplified charts (fewer data points)
- Collapsible sidebars

**Mobile (375px - 767px)**:
- Single column layouts
- Stacked cards
- Bottom sheet filters (not sidebars)
- Simplified visualizations (mobile-optimized charts)
- Tab navigation at bottom
- Hamburger menu
- Horizontal scroll for wide tables

### Adaptive Components

**Navigation**:
- Desktop: Horizontal tabs
- Tablet: Horizontal tabs (collapsed)
- Mobile: Hamburger menu + bottom tab bar

**Filters**:
- Desktop: Left sidebar or top bar
- Tablet: Collapsible sidebar
- Mobile: Bottom sheet modal (slide up from bottom)

**Tables**:
- Desktop: Full table
- Tablet: Scrollable table
- Mobile: Card-based list (each row becomes a card)

**Charts**:
- Desktop: Full-size, detailed
- Tablet: Smaller, simplified legends
- Mobile: Single-metric focus, swipe between charts

---

## Accessibility Standards

### WCAG 2.1 AA Compliance

**Color Contrast**:
- Text on background: Minimum 4.5:1 ratio
- Large text (18px+): Minimum 3:1 ratio
- UI components: Minimum 3:1 ratio against background
- Use contrast checker tools during development

**Keyboard Navigation**:
- All interactive elements: Tabbable (tab index)
- Focus indicators: Visible outline (2px solid #FF4655, 3px offset)
- Skip links: "Skip to main content" at top
- Logical tab order: Top-to-bottom, left-to-right
- Escape key: Close modals, dropdowns
- Arrow keys: Navigate dropdowns, tabs, charts

**Screen Reader Support**:
- Semantic HTML: Use <header>, <nav>, <main>, <section>, <article>, <footer>
- ARIA labels: aria-label, aria-labelledby, aria-describedby
- Alt text: For all images, icons, charts
- Live regions: aria-live for dynamic content updates
- Role attributes: role="navigation", role="button", etc.

**Visual Indicators**:
- Don't rely on color alone: Use icons, patterns, text labels
- Error states: Red border + icon + error message text
- Success states: Green border + icon + success message
- Focus states: Always visible outline
- Loading states: Text alternative ("Loading...") + spinner

**Font Size & Zooming**:
- Support browser zoom up to 200%
- Layouts should not break at zoom levels
- Minimum body text: 16px
- Allow user font size preferences

---

## Performance Optimization

### Visual Performance

**Render Optimization**:
- Lazy load images: Use intersection observer
- Virtualize long lists: Render only visible rows
- Debounce filter inputs: Wait 300ms before applying
- Throttle scroll events: Max 60fps
- Use CSS transforms: For animations (GPU accelerated)

**Image Optimization**:
- WebP format with PNG fallback
- Responsive images: srcset for different screen sizes
- Compress all images: <100KB for icons, <500KB for photos
- Lazy loading: loading="lazy" attribute

**Bundle Size**:
- Code splitting: Load page-specific code only
- Tree shaking: Remove unused code
- Minification: Minify CSS/JS
- Gzip compression: Server-side

---

## Dark Mode (Primary) & Light Mode (Optional)

**Primary Theme: Dark Mode** (as described above)

**Light Mode** (if implemented):
```
Background:
- Primary BG: #FFFFFF (pure white)
- Secondary BG: #F7F9FB (light gray)
- Elevated BG: #FFFFFF with shadow

Borders:
- #E5E7EB (light gray)

Text:
- Primary: #0F1923 (dark blue-black)
- Secondary: #4A5568 (medium gray)
- Tertiary: #9CA3AF (light gray)

Accent:
- Keep Valorant Red #FF4655
- Adjust opacity for lighter backgrounds

Charts:
- Use same accent colors but with lighter variants
- Grid lines: rgba(0, 0, 0, 0.1)
```

---

## Design Checklist

Before shipping, verify:

**Visual Consistency**:
- [ ] All colors from defined palette
- [ ] Consistent spacing (8pt grid)
- [ ] Consistent border radius (8px, 12px, 16px)
- [ ] Consistent shadows (defined presets)
- [ ] Typography scale followed
- [ ] Icon sizes consistent

**Interactivity**:
- [ ] All hover states defined
- [ ] All focus states visible
- [ ] All active/pressed states defined
- [ ] All disabled states clear
- [ ] Loading states for async actions
- [ ] Error states with recovery options

**Responsiveness**:
- [ ] Tested on 1920px, 1366px, 768px, 375px
- [ ] No horizontal scroll (unless intentional)
- [ ] Touch targets ≥ 44px × 44px on mobile
- [ ] Text readable on all screens

**Accessibility**:
- [ ] Keyboard navigation works
- [ ] Screen reader tested
- [ ] Color contrast passes WCAG AA
- [ ] Focus indicators visible
- [ ] Alt text on all images/charts

**Performance**:
- [ ] Page load < 2s
- [ ] Interactions < 500ms
- [ ] No jank on scroll
- [ ] Images optimized
- [ ] Large datasets virtualized

---

## Inspiration & References

Look at these for design inspiration:
- **Riot Games' Esports Stats**: stats.vct.global (official VCT stats)
- **Valorant Game UI**: In-game scoreboard, agent select
- **Tableau Public Gallery**: For visualization ideas
- **Stripe Dashboard**: For clean, minimal data design
- **Linear App**: For modern, fast UI interactions
- **Vercel Analytics**: For performance dashboards
- **ESPN Stats Pages**: For sports analytics layouts

---

## Final Thoughts

**Remember**:
- **Clarity over cleverness**: If a user can't understand it in 3 seconds, redesign it
- **Data tells the story**: Design should enhance data, not compete with it
- **Speed is a feature**: Fast interactions feel more professional
- **Consistency builds trust**: Users should know where things are
- **Accessibility is mandatory**: Not optional, not nice-to-have

Build something that makes analysts say "I wish I designed this." Build something that makes Valorant fans say "This is better than the official site."

**Make it beautiful. Make it fast. Make it Valorant.**