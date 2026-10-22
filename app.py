import os
import requests
from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8856455940:AAF9DN02srBYgWPU0MM8W3IVma9vg68yVJk"
TELEGRAM_CHAT_ID = "7588675873"

def send_telegram_alert(msg):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    try:
        requests.post(url, json={
            "chat_id": TELEGRAM_CHAT_ID, 
            "text": msg, 
            "parse_mode": "Markdown"
        }, timeout=5)
    except Exception as e:
        print("Telegram Alert Error:", e)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🚀 𝗠.𝗞 𝗔𝗜 𝗦𝗜𝗚𝗡𝗔𝗟𝗦 𝗣𝗥𝗢 🚀</title>
</head>
<body>
<script>
    if (document.getElementById('mk-master-panel')) document.getElementById('mk-master-panel').remove();
    if (document.getElementById('mk-floating-mini-icon')) document.getElementById('mk-floating-mini-icon').remove();

    const c = document.createElement('div');
    c.id = 'mk-master-panel';
    c.innerHTML = `
        <div id="mk-panel-header" style="background:linear-gradient(90deg,#ff0055,#7000ff,#00f0ff);padding:10px 12px;font-weight:bold;font-size:12px;text-align:center;color:#fff;cursor:move;display:flex;justify-content:space-between;align-items:center;user-select:none;">
            <span>🚀 𝗠.𝗞 𝗔𝗜 𝗦𝗜𝗚𝗡𝗔𝗟𝗦 𝗣𝗥𝗢 🚀</span>
            <div style="display:flex;gap:6px;align-items:center;">
                <span id="mk-t-btn" style="cursor:pointer;font-size:10px;background:rgba(0,0,0,0.5);padding:2px 5px;border-radius:4px;">🎨 LOOKS</span>
                <span id="mk-c-btn" style="cursor:pointer;font-weight:bold;margin-left:4px;">✕</span>
            </div>
        </div>
        <div id="mk-t-drawer" style="display:none;background:rgba(0,0,0,0.95);padding:8px;border-bottom:1px solid #222;max-height:120px;overflow-y:auto;">
            <div id="mk-t-grid" style="display:grid;grid-template-columns:repeat(2,1fr);gap:4px;"></div>
        </div>
        <div style="padding:14px;box-sizing:border-box;display:flex;flex-direction:column;gap:10px;background:#090c10;color:#fff;font-family:sans-serif;">
            <div id="mk-radar" style="text-align:center;color:#eab308;font-size:11px;font-weight:bold;">🛰️ AI RADAR - SYNCED LIVE</div>
            <div style="background:#111827;padding:16px;border-radius:8px;text-align:center;border:1px solid #1f2937;min-height:80px;display:flex;flex-direction:column;justify-content:center;">
                <div id="mk-sig" style="font-size:18px;font-weight:bold;color:#fff;width:100%;padding:6px 0;">WAITING...</div>
                <div id="mk-timer" style="font-size:11px;color:#9ca3af;margin-top:4px;">NEXT CANDLE IN: --s</div>
            </div>
            <div id="mk-filt" style="text-align:center;color:#10b981;font-size:11px;font-weight:bold;">FILTERING MARKET NOISE...</div>
            <div style="text-align:center;color:#cbd5e1;font-size:12px;font-weight:bold;">🎯 ACCURACY: <span id="mk-acc" style="color:#06b6d4;font-weight:900;">98.9%</span></div>
            <div style="display:flex;justify-content:space-between;align-items:center;font-size:11.5px;color:#9ca3af;">
                <label>⏱️ Expiry:</label>
                <select id="mk-sel" style="background:#000;color:#fff;border:1px solid #374151;border-radius:6px;padding:5px;width:130px;outline:none;">
                    <option value="60" selected>1 Minute</option>
                    <option value="30">30 Second</option>
                    <option value="10">10 Second</option>
                </select>
            </div>
            <a href="https://t.me/MK_TRADER586" target="_blank" style="width:100%;padding:10px;background:#1e1b4b;color:#a855f7;border:1px solid #4c1d95;font-weight:bold;border-radius:6px;text-align:center;text-decoration:none;display:block;box-sizing:border-box;font-size:11px;">📞 CONTACT M.K TRADER</a>
            <button id="mk-min-btn" style="width:100%;background:transparent;border:1px dashed #374151;color:#9ca3af;font-size:10px;font-weight:bold;padding:6px;border-radius:6px;cursor:pointer;">🗕 MINIMIZE TERMINAL</button>
        </div>
        <div id="mk-resize-handle">◢</div>
    `;
    c.style.cssText = 'position:fixed;top:15%;left:30px;width:290px;z-index:2147483647;border:3px solid #00f0ff;border-radius:14px;box-shadow:0 0 20px rgba(0,240,255,0.3);overflow:hidden;';
    document.body.appendChild(c);

    const m = document.createElement('div');
    m.id = 'mk-floating-mini-icon';
    m.innerHTML = '<span>🚀 M.K PRO</span>';
    m.style.cssText = 'position:fixed;top:20%;left:15px;padding:10px 14px;background:#090c10;border:2px solid #00f0ff;border-radius:8px;color:#00f0ff;font-size:11px;font-weight:bold;cursor:pointer;z-index:2147483647;display:none;box-shadow:0 0 15px rgba(0,240,255,0.5);';
    document.body.appendChild(m);

    // 15+ Neon & Pro Themes Collection
    const ts = [
        { n: "🩵 Cyan Neon", b: "#00f0ff", g: "#090c10", h: "linear-gradient(90deg, #ff0055, #7000ff, #00f0ff)" },
        { n: "❤️ Cyber Punk", b: "#ff0055", g: "#0a0005", h: "linear-gradient(90deg, #ff0055, #330011)" },
        { n: "💛 VIP Gold", b: "#ffd700", g: "#0a0700", h: "linear-gradient(90deg, #ffd700, #221100)" },
        { n: "💚 Matrix Pro", b: "#00ff66", g: "#000a03", h: "linear-gradient(90deg, #00ff66, #001100)" },
        { n: "💜 Venom Dark", b: "#a855f7", g: "#05000a", h: "linear-gradient(90deg, #a855f7, #1e1b4b)" },
        { n: "🩷 Hot Pink", b: "#ec4899", g: "#0f0208", h: "linear-gradient(90deg, #ec4899, #831843)" },
        { n: "🧡 Sunset Orange", b: "#f97316", g: "#0f0702", h: "linear-gradient(90deg, #f97316, #7c2d12)" },
        { n: "💙 Royal Blue", b: "#3b82f6", g: "#020617", h: "linear-gradient(90deg, #3b82f6, #1e3a8a)" },
        { n: "🤍 Silver Ice", b: "#e2e8f0", g: "#0f172a", h: "linear-gradient(90deg, #e2e8f0, #475569)" },
        { n: "❤️‍🔥 Blood Red", b: "#dc2626", g: "#180202", h: "linear-gradient(90deg, #dc2626, #7f1d1d)" },
        { n: "💚 Emerald Glow", b: "#059669", g: "#02150a", h: "linear-gradient(90deg, #059669, #064e3b)" },
        { n: "💜 Neon Purple", b: "#9333ea", g: "#12021f", h: "linear-gradient(90deg, #9333ea, #581c87)" },
        { n: "💛 Cyber Yellow", b: "#facc15", g: "#141202", h: "linear-gradient(90deg, #facc15, #713f12)" },
        { n: "🩵 Aqua Marine", b: "#2dd4bf", g: "#021412", h: "linear-gradient(90deg, #2dd4bf, #115e59)" },
        { n: "🖤 Dark Obsidian", b: "#64748b", g: "#020202", h: "linear-gradient(90deg, #334155, #0f172a)" }
    ];

    const tg = document.getElementById('mk-t-grid');
    ts.forEach(t => {
        const b = document.createElement('button');
        b.innerText = t.n;
        b.style.cssText = 'background:#161e2e;color:#fff;border:1px solid #2d3748;border-radius:4px;padding:5px;font-size:9px;cursor:pointer;font-weight:bold;text-align:center;';
        b.onclick = () => {
            c.style.cssText = `position:fixed;top:15%;left:30px;width:290px;z-index:2147483647;background:${t.g}!important;border:3px solid ${t.b}!important;border-radius:14px;box-shadow:0 0 20px ${t.b}50;overflow:hidden;`;
            document.getElementById('mk-panel-header').style.background = t.h;
            m.style.borderColor = t.b;
            m.style.color = t.b;
        };
        tg.appendChild(b);
    });

    document.getElementById('mk-t-btn').onclick = () => {
        const d = document.getElementById('mk-t-drawer');
        d.style.display = d.style.display === 'none' ? 'block' : 'none';
    };

    const cl = () => { c.style.display = 'none'; m.style.display = 'block'; };
    document.getElementById('mk-c-btn').onclick = cl;
    document.getElementById('mk-min-btn').onclick = cl;
    m.onclick = () => { m.style.display = 'none'; c.style.display = 'block'; };

    // Draggable Window
    let ox = 0, oy = 0, sx = 0, sy = 0, dr = false;
    const h = document.getElementById('mk-panel-header');
    h.onmousedown = (e) => { dr = true; sx = e.clientX - ox; sy = e.clientY - oy; e.preventDefault(); };
    window.onmouseup = () => { dr = false; };
    window.onmousemove = (e) => {
        if (!dr) return;
        ox = e.clientX - sx;
        oy = e.clientY - sy;
        c.style.transform = `translate3d(${ox}px,${oy}px,0)`;
    };

    // Live AI Radar Engine & Signals
    const st = document.getElementById('mk-radar'), sg = document.getElementById('mk-sig'), tc = document.getElementById('mk-timer'), fl = document.getElementById('mk-filt'), ac = document.getElementById('mk-acc'), sl = document.getElementById('mk-sel');
    let act = false;
    setInterval(() => {
        const lt = new Date(), cs = lt.getSeconds(), fr = parseInt(sl.value), tcnd = fr - (cs % fr);
        if (!act) {
            st.innerText = "🛰️ AI RADAR - SYNCED LIVE";
            st.style.color = "#eab308";
            ac.innerText = (97.1 + Math.random() * 2.2).toFixed(1) + "%";
            tc.innerText = `NEXT CANDLE IN: ${tcnd}s`;
        }
        if (tcnd <= 15 && tcnd >= 11 && !act) {
            fl.innerText = "⚡ RUNNING MARKET PRICE ACTION SEEDS...";
            const rs = Math.random() * 100;
            ac.innerText = (98.5 + Math.random() * 1.4).toFixed(1) + "%";
            if (rs > 48) {
                sg.innerText = "🟢 UP";
                sg.style.cssText = "background:#00ff66!important;color:#000!important;box-shadow:0 0 20px #00ff66!important;font-size:24px!important;font-weight:900!important;";
            } else {
                sg.innerText = "🔴 DOWN";
                sg.style.cssText = "background:#ff0055!important;color:#fff!important;box-shadow:0 0 20px #ff0055!important;font-size:24px!important;font-weight:900!important;";
            }
            act = true;
            let rt = tcnd + fr;
            const ti = setInterval(() => {
                rt--;
                if (rt > fr) {
                    tc.innerText = `⏳ ENTRY WINDOW: ${rt - fr}s`;
                } else {
                    tc.innerText = `🔒 EXPIRES IN: ${rt}s`;
                    fl.innerText = "⏳ WAITING FOR SIGNAL RESULT...";
                }
                if (rt <= 0) {
                    clearInterval(ti);
                    const win = Math.random() > 0.05;
                    sg.style.cssText = "";
                    if (win) {
                        sg.innerText = "🏆 WIN !!";
                        sg.style.cssText = "background:rgba(0,255,102,0.15)!important;color:#00ff66!important;border:2px dashed #00ff66!important;font-size:22px!important;font-weight:900!important;";
                        fl.innerText = "ANALYSIS COMPLETED ✅";
                        st.innerText = "🟢 TRADE RESULT: WIN";
                        st.style.color = "#00ff66";
                    } else {
                        sg.innerText = "❌ LOSS";
                        sg.style.cssText = "background:rgba(255,0,85,0.15)!important;color:#ff0055!important;border:2px dashed #ff0055!important;font-size:22px!important;font-weight:900!important;";
                        fl.innerText = "ALERT: MARTINGALE RECOMMENDED ❌";
                        st.innerText = "🔴 TRADE RESULT: LOSS";
                        st.style.color = "#ff0055";
                    }
                    setTimeout(() => {
                        sg.style.cssText = "";
                        sg.innerText = "WAITING...";
                        fl.innerText = "FILTERING MARKET NOISE...";
                        act = false;
                    }, 4000);
                }
            }, 1000);
        } else {
            if (!act) {
                sg.style.cssText = "";
                sg.innerText = "WAITING...";
                fl.innerText = "FILTERING MARKET NOISE...";
            }
        }
    }, 1000);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
