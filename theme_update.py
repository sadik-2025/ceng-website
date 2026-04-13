import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update :root
root_repl = """        /* --- Premium Modern Light Theme (Indigo & Rose Mix) --- */
        :root {
            --bg-dark: #f8fafc;          
            --bg-surface: #ffffff;       
            --bg-surface-hover: #f1f5f9; 
            --text-primary: #0f172a;
            --text-secondary: #475569;
            
            /* Mix Color Accents */
            --accent-blue: #4f46e5;      
            --accent-teal: #e11d48;
            --gradient-accent: linear-gradient(135deg, var(--accent-blue), var(--accent-teal));
            
            --border-color: #cbd5e1; 
            
            --font-heading: 'Outfit', sans-serif;
            --font-body: 'Inter', sans-serif;
            
            --transition-smooth: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }"""
        
html = re.sub(r'/\* --- Premium Modern Dark Theme[^\}]+\}', root_repl, html)

# 2. Update text gradient for light mode
html = html.replace("background: linear-gradient(to right, #ffffff, #a1a1aa);", "background: linear-gradient(to right, #0f172a, #64748b);")

# 3. Update navbar backgrounds
html = html.replace("background: rgba(10, 10, 10, 0.7);", "background: rgba(255, 255, 255, 0.7);")
html = html.replace("background = 'rgba(10, 10, 10, 0.85)';", "background = 'rgba(255, 255, 255, 0.9)';")
html = html.replace("background: rgba(17, 17, 17, 0.95);", "background: rgba(255, 255, 255, 0.98);")

# 4. Outlines
html = html.replace("border: 1px solid rgba(255, 255, 255, 0.2);", "border: 1px solid rgba(0,0,0,0.2);")
html = html.replace("background-color: rgba(255, 255, 255, 0.05);", "background-color: rgba(0, 0, 0, 0.05);")
html = html.replace("background: rgba(255, 255, 255, 0.03);", "background: rgba(0, 0, 0, 0.04);")

# 5. Cards & Images
html = html.replace("background: #1a1a1a;", "background: #f1f5f9;")
html = html.replace("linear-gradient(145deg, var(--bg-surface), #0a0a0a)", "linear-gradient(145deg, var(--bg-surface), #e2e8f0)")

# 6. Hero Glow
html = html.replace("background: radial-gradient(circle, rgba(20, 184, 166, 0.3) 0%, rgba(59, 130, 246, 0.1) 40%, transparent 70%);", "background: radial-gradient(circle, rgba(79, 70, 229, 0.15) 0%, rgba(225, 29, 72, 0.05) 40%, transparent 70%);")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)
