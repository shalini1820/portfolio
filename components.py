# components_enhanced.py
import streamlit as st

def project_card_enhanced(title, subtitle, context, solution, impact_lines, tools, status=None, repo_link=None, metrics=None):
    """
    Enhanced project card with modern design and visual hierarchy.
    
    Args:
        title: str - Project title
        subtitle: str - Tech stack summary
        context: str - Problem statement
        solution: str - Solution description
        impact_lines: list[str] - Impact metrics
        tools: str - Tools used
        status: optional str - "Completed" or "In Progress"
        repo_link: optional URL
        metrics: optional dict - {"before": "X", "after": "Y", "improvement": "Z%"}
    """
    
    # Status badge color
    status_color = "#4ade80" if status == "Completed" else "#fbbf24"
    
    card_html = f"""
    <div class="enhanced-project-card">
        <div class="card-header">
            <div>
                <h3 class="card-title">{title}</h3>
                <p class="card-subtitle">{subtitle}</p>
            </div>
            {f'<span class="status-badge" style="background: {status_color};">{status}</span>' if status else ''}
        </div>
        
        <div class="card-section">
            <h4 class="section-label">🎯 Problem</h4>
            <p class="section-text">{context}</p>
        </div>
        
        <div class="card-section">
            <h4 class="section-label">💡 Solution</h4>
            <p class="section-text">{solution}</p>
        </div>
    """
    
    # Add metrics if provided
    if metrics:
        card_html += f"""
        <div class="metrics-container">
            <div class="metric-box">
                <span class="metric-label">Before</span>
                <span class="metric-value before">{metrics.get('before', 'N/A')}</span>
            </div>
            <div class="metric-arrow">→</div>
            <div class="metric-box">
                <span class="metric-label">After</span>
                <span class="metric-value after">{metrics.get('after', 'N/A')}</span>
            </div>
            <div class="metric-box highlight">
                <span class="metric-label">Impact</span>
                <span class="metric-value improvement">{metrics.get('improvement', 'N/A')}</span>
            </div>
        </div>
        """
    
    # Impact section
    if impact_lines:
        card_html += """
        <div class="card-section">
            <h4 class="section-label">📈 Impact</h4>
            <ul class="impact-list">
        """
        for line in impact_lines:
            card_html += f'<li class="impact-item">{line}</li>'
        card_html += """
            </ul>
        </div>
        """
    
    # Tools and repo
    card_html += f"""
        <div class="card-footer">
            <div class="tools-container">
                <span class="tools-label">Stack:</span>
                <span class="tools-text">{tools}</span>
            </div>
    """
    
    if repo_link:
        card_html += f'''
            <a href="{repo_link}" class="repo-link" target="_blank">
                <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                </svg>
                View Code
            </a>
        '''
    
    card_html += """
        </div>
    </div>
    """
    
    st.markdown(card_html, unsafe_allow_html=True)


def load_project_card_css():
    """Load CSS for enhanced project cards"""
    css = """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@400;500;700&display=swap');
    
    .enhanced-project-card {
        background: linear-gradient(135deg, rgba(244, 196, 48, 0.03) 0%, rgba(20, 27, 61, 0.5) 100%);
        border: 1px solid rgba(244, 196, 48, 0.2);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 2rem;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    
    .enhanced-project-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #f4c430 0%, #ffd700 100%);
        transform: scaleX(0);
        transition: transform 0.4s ease;
        transform-origin: left;
    }
    
    .enhanced-project-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 16px 48px rgba(244, 196, 48, 0.2);
        border-color: #f4c430;
    }
    
    .enhanced-project-card:hover::before {
        transform: scaleX(1);
    }
    
    .card-header {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        margin-bottom: 1.5rem;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .card-title {
        font-family: 'Space Mono', monospace;
        font-size: 1.5rem;
        font-weight: 700;
        color: #f4c430;
        margin: 0 0 0.5rem 0;
        letter-spacing: -0.5px;
    }
    
    .card-subtitle {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.95rem;
        color: #8892b0;
        margin: 0;
        font-weight: 500;
    }
    
    .status-badge {
        font-family: 'Space Mono', monospace;
        padding: 0.4rem 1rem;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 700;
        color: #0a0e27;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .card-section {
        margin-bottom: 1.5rem;
    }
    
    .section-label {
        font-family: 'Space Mono', monospace;
        font-size: 0.85rem;
        color: #f4c430;
        margin: 0 0 0.5rem 0;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
    }
    
    .section-text {
        font-family: 'DM Sans', sans-serif;
        font-size: 1rem;
        color: #ccd6f6;
        line-height: 1.7;
        margin: 0;
    }
    
    .metrics-container {
        display: grid;
        grid-template-columns: 1fr auto 1fr 1fr;
        gap: 1rem;
        background: rgba(244, 196, 48, 0.05);
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1.5rem 0;
        align-items: center;
    }
    
    .metric-box {
        text-align: center;
    }
    
    .metric-box.highlight {
        background: rgba(244, 196, 48, 0.1);
        padding: 0.5rem;
        border-radius: 8px;
        border: 1px solid rgba(244, 196, 48, 0.3);
    }
    
    .metric-label {
        font-family: 'Space Mono', monospace;
        font-size: 0.75rem;
        color: #8892b0;
        display: block;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .metric-value {
        font-family: 'Space Mono', monospace;
        font-size: 1.5rem;
        font-weight: 700;
        display: block;
    }
    
    .metric-value.before {
        color: #ef4444;
    }
    
    .metric-value.after {
        color: #4ade80;
    }
    
    .metric-value.improvement {
        color: #f4c430;
    }
    
    .metric-arrow {
        font-size: 2rem;
        color: #f4c430;
        text-align: center;
    }
    
    .impact-list {
        list-style: none;
        padding: 0;
        margin: 0;
    }
    
    .impact-item {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.95rem;
        color: #ccd6f6;
        padding: 0.5rem 0;
        padding-left: 1.5rem;
        position: relative;
        line-height: 1.6;
    }
    
    .impact-item::before {
        content: '▹';
        color: #f4c430;
        position: absolute;
        left: 0;
        font-size: 1.2rem;
    }
    
    .card-footer {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-top: 1.5rem;
        padding-top: 1.5rem;
        border-top: 1px solid rgba(244, 196, 48, 0.1);
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .tools-container {
        display: flex;
        align-items: center;
        gap: 0.5rem;
        flex-wrap: wrap;
    }
    
    .tools-label {
        font-family: 'Space Mono', monospace;
        font-size: 0.85rem;
        color: #8892b0;
        font-weight: 700;
    }
    
    .tools-text {
        font-family: 'DM Sans', sans-serif;
        font-size: 0.9rem;
        color: #a8b2d1;
    }
    
    .repo-link {
        font-family: 'Space Mono', monospace;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        background: rgba(244, 196, 48, 0.1);
        color: #f4c430;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        text-decoration: none;
        font-size: 0.85rem;
        font-weight: 700;
        border: 1px solid rgba(244, 196, 48, 0.3);
        transition: all 0.3s ease;
    }
    
    .repo-link:hover {
        background: rgba(244, 196, 48, 0.2);
        transform: translateX(4px);
        border-color: #f4c430;
    }
    
    @media (max-width: 768px) {
        .metrics-container {
            grid-template-columns: 1fr;
            text-align: center;
        }
        
        .metric-arrow {
            transform: rotate(90deg);
        }
        
        .card-footer {
            flex-direction: column;
            align-items: flex-start;
        }
    }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
