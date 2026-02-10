"""
Patch Streamlit's index.html to show a custom SIVO loading screen
instead of the default blank page while the app boots.

Run this script after installing Streamlit:
    python patch_streamlit_loading.py
"""

import os
import re
import sys


def get_streamlit_index_path():
    """Find Streamlit's index.html location."""
    try:
        import streamlit
        static_dir = os.path.join(os.path.dirname(streamlit.__file__), "static")
        index_path = os.path.join(static_dir, "index.html")
        if os.path.exists(index_path):
            return index_path
    except ImportError:
        pass
    return None


SIVO_LOADING_HTML = r"""
    <style>
      @keyframes sivoFadeIn {
        from { opacity: 0; transform: translateY(16px); }
        to   { opacity: 1; transform: translateY(0); }
      }
      @keyframes sivoPulse {
        0%, 100% { opacity: 1; }
        50%      { opacity: .55; }
      }
      @keyframes sivoBar {
        0%   { left: -40%; }
        100% { left: 100%; }
      }
      @keyframes sivoDots {
        0%, 80%, 100% { opacity: .25; transform: scale(.8); }
        40%           { opacity: 1;  transform: scale(1); }
      }
      #sivo-loader {
        position: fixed; inset: 0; z-index: 999999;
        display: flex; flex-direction: column;
        align-items: center; justify-content: center;
        background: #ffffff;
        font-family: 'Arial Black', 'Helvetica Neue', Arial, sans-serif;
      }
      #sivo-loader .sivo-logo-wrap {
        animation: sivoFadeIn .7s ease-out both, sivoPulse 2.4s ease-in-out .7s infinite;
      }
      #sivo-loader .sivo-tagline {
        margin-top: 28px;
        font-family: 'Helvetica Neue', Arial, sans-serif;
        font-weight: 400; font-size: 15px; letter-spacing: .5px;
        color: #888;
        animation: sivoFadeIn .7s ease-out .35s both;
      }
      #sivo-loader .sivo-bar-track {
        margin-top: 32px; width: 180px; height: 3px;
        background: #f0f0f0; border-radius: 3px;
        overflow: hidden; position: relative;
        animation: sivoFadeIn .7s ease-out .5s both;
      }
      #sivo-loader .sivo-bar-fill {
        position: absolute; top: 0; height: 100%; width: 40%;
        background: linear-gradient(90deg, #3b82f6, #60a5fa);
        border-radius: 3px;
        animation: sivoBar 1.3s ease-in-out infinite;
      }
      #sivo-loader .sivo-dots {
        display: flex; gap: 6px; margin-top: 22px;
        animation: sivoFadeIn .7s ease-out .55s both;
      }
      #sivo-loader .sivo-dots span {
        width: 6px; height: 6px; border-radius: 50%;
        background: #3b82f6;
        animation: sivoDots 1.4s ease-in-out infinite;
      }
      #sivo-loader .sivo-dots span:nth-child(2) { animation-delay: .15s; }
      #sivo-loader .sivo-dots span:nth-child(3) { animation-delay: .3s; }
    </style>
    <div id="sivo-loader">
      <div class="sivo-logo-wrap">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="10 0 270 110" width="200" height="82">
          <defs>
            <style>.sivo-text{font-family:'Arial Black','Helvetica Neue',Arial,sans-serif;font-weight:900;font-size:72px;fill:#111111;}</style>
          </defs>
          <text x="20" y="88" class="sivo-text">S</text>
          <text x="72" y="88" class="sivo-text">I</text>
          <rect x="84" y="8" width="10" height="10" rx="1.5" transform="rotate(45 89 13)" fill="#111111"/>
          <text x="105" y="88" class="sivo-text">V</text>
          <text x="170" y="88" class="sivo-text">O</text>
          <path d="M 95,75 C 120,95 145,98 175,85 C 210,70 240,55 270,72 C 250,60 225,52 200,60 C 175,68 150,78 130,72"
                fill="none" stroke="#111111" stroke-width="4" stroke-linecap="round"/>
          <path d="M 100,82 C 130,100 160,100 190,88 C 220,75 245,62 265,78"
                fill="none" stroke="#111111" stroke-width="3" stroke-linecap="round" opacity="0.6"/>
        </svg>
      </div>
      <div class="sivo-tagline">Preparando tu experiencia &hellip;</div>
      <div class="sivo-bar-track"><div class="sivo-bar-fill"></div></div>
      <div class="sivo-dots"><span></span><span></span><span></span></div>
    </div>
"""


def patch_index(index_path):
    """Replace the empty <div id="root"> with our custom loader."""
    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    if "sivo-loader" in html:
        print("✓ SIVO loading screen already applied.")
        return True

    # Replace <title>
    html = html.replace("<title>Streamlit</title>", "<title>SIVO</title>")

    # Inject loader inside <div id="root">
    html = re.sub(
        r'(<div\s+id="root"\s*>)\s*(</div>)',
        r"\1" + SIVO_LOADING_HTML + r"\2",
        html,
        flags=re.S,
    )

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html)

    print("✓ SIVO loading screen applied successfully!")
    return True


def main():
    index_path = get_streamlit_index_path()
    if not index_path:
        print("✗ Could not find Streamlit's index.html. Is Streamlit installed?", file=sys.stderr)
        sys.exit(1)
    print(f"  Found: {index_path}")
    patch_index(index_path)


if __name__ == "__main__":
    main()
